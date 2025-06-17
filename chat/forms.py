from django import forms
from .models import Message

class MessageAdminForm(forms.ModelForm):
    class Meta:
        model= Message
        fields = ['room', 'user', 'content']
        
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError("Content must be at least 5 characters long.")
        return content
    
