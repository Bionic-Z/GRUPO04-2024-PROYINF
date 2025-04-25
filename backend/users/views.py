from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.postgres.search import TrigramSimilarity
from django.core.paginator import Paginator
from django.contrib import messages

User = get_user_model()


# @login_required
def dashboard_view(request):
    context = {
        "is_admin": request.user.groups.filter(name="admin").exists(),
    }
    return render(request, "users/dashboard.html", context)


@login_required
def profile_view(request):
    context = {
        "is_admin": request.user.groups.filter(name="admin").exists(),
    }
    return render(request, "users/profile.html", context)


@login_required
def manage_users(request):
    if not request.user.groups.filter(name="admin").exists():
        return redirect("dashboard")

    q = request.GET.get("q", "")
    qs = User.objects.all()
    if q:
        qs = (
            qs.annotate(
                similarity=TrigramSimilarity("username", q)
                + TrigramSimilarity("email", q)
                + TrigramSimilarity("first_name", q)
                + TrigramSimilarity("last_name", q)
            )
            .filter(similarity__gt=0.1)
            .order_by("-similarity")
        )
    else:
        qs = qs.order_by("username")

    paginator = Paginator(qs, 10)
    users_page = paginator.get_page(request.GET.get("page"))

    groups = Group.objects.all()
    is_admin = request.user.groups.filter(name="admin").exists()

    context = {
        "users_page": users_page,
        "groups": groups,
        "q": q,
        "is_admin": is_admin,
    }

    return render(request, "users/manage_users.html", context)


@require_POST
@login_required
def update_user_roles(request):
    if not request.user.groups.filter(name="admin").exists():
        return redirect("dashboard")

    user_id = request.POST.get("user_id")
    group_ids = request.POST.getlist("groups")
    try:
        u = User.objects.get(id=user_id)
        u.groups.set(Group.objects.filter(id__in=group_ids))
        messages.success(request, f"Roles actualizados para {u.username}")
    except User.DoesNotExist:
        messages.error(request, "Usuario no encontrado")
    return redirect("manage_users")


@login_required
def profile_view(request):
    context = {
        "is_admin": request.user.groups.filter(name="admin").exists(),
        "user_obj": request.user,
    }
    return render(request, "users/profile.html", context)


@login_required
def edit_user_role(request, pk):
    if not request.user.groups.filter(name="admin").exists():
        messages.error(request, "No tienes permiso para esto.")
        return redirect("dashboard")

    user_obj = get_object_or_404(User, pk=pk)
    groups = Group.objects.all()

    if request.method == "POST":
        role_id = request.POST.get("role")
        try:
            if role_id:
                group = Group.objects.get(pk=role_id)
                user_obj.groups.set([group])
                messages.success(
                    request, f"Rol de {user_obj.username} actualizado a {group.name}."
                )
            else:
                user_obj.groups.clear()
                messages.warning(
                    request, f"Se ha removido el rol de {user_obj.username}."
                )
            return redirect("manage_users")
        except Group.DoesNotExist:
            messages.error(request, "Rol no válido.")
            return redirect("manage_users")

    return render(
        request,
        "users/edit_user_role.html",
        {
            "user_obj": user_obj,
            "groups": groups,
        },
    )


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        reader_group, _ = Group.objects.get_or_create(name="reader")
        self.object.groups.add(reader_group)
        return response
