from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')

@login_required
def manage_users(request):
    if not request.user.groups.filter(name='admin').exists():
        return redirect('dashboard')  # Redirigir si no es admin

    users = User.objects.all().select_related()
    groups = Group.objects.all()

    return render(request, 'users/manage_users.html', {
        'users': users,
        'groups': groups
    })


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        reader_group, _ = Group.objects.get_or_create(name='reader')
        self.object.groups.add(reader_group)
        return response
