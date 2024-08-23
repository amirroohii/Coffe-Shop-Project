from django import forms
from .models import CoffeTableReservation

class ReservationForm(forms.ModelForm):
    people_count = forms.ChoiceField(
        choices=CoffeTableReservation.NumberOfPeople.choices,  # Assuming you have this defined in your model
        widget=forms.Select(
            attrs={
                'class': 'custom-select bg-transparent border-primary px-4',
                'style': 'height: 49px;',
                'required': 'required',
            }
        )
    )

    class Meta:
        model = CoffeTableReservation
        fields = ['name', 'phone_number', 'email', 'reserve_date', 'people_count', 'notes']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control bg-transparent border-primary p-4',
                    'placeholder': 'Enter Your Name',
                    'id': 'name',
                    'required': 'required',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control bg-transparent border-primary p-4',
                    'placeholder': 'Enter Your Email',
                    'type': 'email',
                    'required': 'required',
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control bg-transparent border-primary p-4',
                    'placeholder': 'Enter Your Phone Number',
                    'required': 'required',
                }
            ),
            'reserve_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control bg-transparent border-primary p-4 datetimepicker-input',
                    'placeholder': 'reserve date',
                    'type': 'datetime-local',
                    'data-toggle': 'datetimepicker',
                }
            ),

        }
