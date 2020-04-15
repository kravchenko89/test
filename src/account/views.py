from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView


from account.forms import UserCreationForm, UserChangeForm
from account.models import User, SaveIP, SaveSignals


class UserCreate(CreateView):
    form_class = UserCreationForm
    queryset = User.objects.all()
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('account:login')


class UserLogin(LoginView):
    model = User
    fields = ['username', 'password']
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class UserShow(ListView):
    template_name = 'index'
    queryset = User.objects.all()
    model = User

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(id=self.request.user.id)


class ChangeProfile(UpdateView):
    template_name = 'change_profile.html'
    queryset = User.objects.filter(is_active=True)
    form_class = UserChangeForm
    success_url = reverse_lazy('index')

    model = SaveIP

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        SaveIP.objects.create(user=request.user.username,
                              user_ip=request.META['REMOTE_ADDR'],
                              data_saved=SaveIP.data_saved)
        # breakpoint()
        return response


class SaveSignalsShow(ListView):
    model = SaveSignals
    template_name = 'save_signals.html'
    paginate_by = 20
    context_object_name = 'data_show'
