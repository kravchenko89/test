from django.contrib import admin

from account.forms import UserCreationForm, UserChangeForm
from account.models import User, SaveIP


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    fields = ('username', 'password', 'first_name', 'last_name', 'bio', 'birth_date',
              'country', 'email', 'phone', 'is_staff', 'is_active', 'is_superuser')
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', )
    readonly_fields = ('password', )


@admin.register(SaveIP)
class UserAdmin(admin.ModelAdmin):
    model = SaveIP
    # list_display = ('user', 'user_ip', 'data_saved')
    readonly_fields = ('user', 'user_ip', 'data_saved')
