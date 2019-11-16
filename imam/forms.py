from django import forms
from .models import Script, Video, Comment


class ScriptForm(forms.ModelForm):

    class Meta:
        model = Script
        fields = ('title', 'name', 'genre', 'logline', 'upload',)

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ["script", "comment",]