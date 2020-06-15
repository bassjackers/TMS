from django import forms
from django.contrib.auth.hashers import check_password
from .models import Account


class CreateAccountForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일 주소를 입력해주세요.'
        },

        max_length=64,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'E-MAIL'}),
        label="E-mail address"
    )

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'PASSWORD'}),
        label="Password"
    )

    check_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'CHECK PASSWORD'}),
        label="Repeat Password"
    )

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        check_password = cleaned_data.get('check_password')

        if password and check_password:
            if password != check_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('check_password', '비밀번호가 서로 다릅니다.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일 주소를 입력해주세요.'
        },
        max_length=64, label="Email address"
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput(), label='Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                account = Account.objects.get(email=email)
            except Account.DoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return

            if not check_password(password, account.password):
                self.add_error('password', '비밀번호가 다릅니다.')
