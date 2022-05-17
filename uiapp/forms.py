from django import forms
from uiapp.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['email', 'comment']

        widgets = {
            'comment': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }