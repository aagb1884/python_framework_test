from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    username = forms.CharField(required=True)
    avatar = forms.CharField(required=False)
    content = forms.CharField(required=True)
    pub_date = forms.DateTimeField(required=True)

    class Meta:
        model = Message
        fields = ["username", "avatar", "content", "pub_date"]

