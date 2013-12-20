# coding=utf-8
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from uerp.apps.hr.models import Employee


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmployeeCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ("work_email", )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Пароли не совпадают"
            raise forms.ValidationError(msg)

    def save(self, commit=True):
        user = super(EmployeeCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EmployeeChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee

    def clean_password(self):
        return self.initial["password"]