from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from Accounts.models import CustomUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('date_of_birth', 'email', 'is_a_chicken')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('identifier', 'password', 'date_of_birth',
                  'email', 'is_a_chicken', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('identifier', 'email', 'date_of_birth',
                    'is_a_chicken', 'is_admin')
    list_filter = ('is_admin','is_a_chicken')
    fieldsets = (
        (None, {'fields': ('identifier', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',
                                      'email', 'is_a_chicken')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identifier', 'date_of_birth', 'email',
                       'is_a_chicken', 'password1', 'password2')}
         ),
    )
    search_fields = ('identifier', 'email',)
    ordering = ('identifier', 'email', 'date_of_birth')
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
# Register your models here.
