from django import forms

class YourForm(forms.Form):
    your_field = forms.CharField()

    submit_button = forms.CharField(widget=forms.TextInput(attrs={'type': 'submit'}))


class DateForm(forms.Form):
    date = forms.DateField(label='Select a date', input_formats=['%Y-%m-%d'])
