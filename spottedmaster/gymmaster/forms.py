from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'id': 'textInput', 'name': 'message'}))
