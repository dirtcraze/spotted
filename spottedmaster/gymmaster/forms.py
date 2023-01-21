from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 250, 'autofocus': True, 'required': True, 'id': 'message-area', 'class': 'form-control', 'name': 'message', 'placeholder': '...', 'rows': '1'}))
