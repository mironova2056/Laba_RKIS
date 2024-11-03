from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("avatar", "first_name", "username","email")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            self.add_error("password2", "Пароли должны совпадать")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UpdateForm(forms.ModelForm):
    avatar = forms.ImageField(label="Фото профиля", required=False)
    first_name = forms.CharField(label="Имя", required=False)
    username = forms.CharField(label="Логин", required=False)
    email = forms.CharField(label="Почта", required=False)

    class Meta:
        model = User
        fields = ("avatar", "first_name", "username", "email")
