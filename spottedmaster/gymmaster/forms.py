from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 250, 'oninput':'textAreaAdjust(this)', 'resize': False, 'autofocus': True, 'required': True, 'class': 'form-control', 'id': 'input-1', 'name': 'message','placeholder': '...'}))
