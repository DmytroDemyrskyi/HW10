from django import forms
import re


class SMSForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', max_length=15)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^\+38\d{10}$', phone_number):
            raise forms.ValidationError('Номер должен быть в формате +38XXXXXXXXXX')
        return phone_number

    def clean_message(self):
        message = self.cleaned_data['message']
        if not message:
            raise forms.ValidationError('Это поле обязательно для заполнения')
        return message
