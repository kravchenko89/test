from django import forms
# from django.forms import SelectDateWidget

from account.models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'bio', 'birth_date',
                  'country', 'email', 'phone', 'password', 'password_confirm')
        # widgets = {
        #     'birth_date': SelectDateWidget(years=range(1940, 2016))
        # }

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password_confirm']:
                raise forms.ValidationError('Passwords do not match!')
        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'bio', 'birth_date',
                  'country', 'email', 'phone')
        # widgets = {
        #     'birth_date': SelectDateWidget(years=range(1940, 2014))
        # }
