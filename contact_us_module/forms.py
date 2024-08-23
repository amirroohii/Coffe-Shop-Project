from .models import ContactUs
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['fullname', 'email', 'subject', 'message']
        widgets = {
            'fullname': forms.TextInput(
                attrs={
                    'class': 'form-control bg-transparent py-3 px-4',
                    'placeholder': 'Enter Your Fullname',
                    'id': 'name',
                    'required': 'required',
                    'data-validation-required-message': 'please enter your fullname'

                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control bg-transparent py-3 px-4',
                    'placeholder': 'Enter Your Email',
                    'id': 'email',
                    'required': 'required',
                    'data-validation-required-message': 'please enter your Email'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control bg-transparent py-3 px-4',
                    'placeholder': 'Enter Your Subject',
                    'id': 'subject',
                    'required': 'required',
                    'data-validation-required-message': 'please enter your Subject',

                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control bg-transparent py-3 px-4',
                    'placeholder': 'Enter Your Message',
                    'rows': 5,
                    'id': 'message',
                    'required': 'required',
                    'data-validation-required-message': 'please enter your Subject',

                }
            )
        }
