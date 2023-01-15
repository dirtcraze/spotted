from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'required': True, 'class': 'form-control', 'id': 'textInput', 'name': 'message'}))
