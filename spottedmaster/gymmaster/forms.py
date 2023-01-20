from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 250, 'autofocus': True, 'required': True, 'class': 'form-control', 'id': 'input-1', 'name': 'message','placeholder': '...'}))
