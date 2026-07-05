from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta: ## Creates a form based on model topic
        model = Topic
        fields = ['text'] # CREATE text as field
        labels = {'text':''} # tells not to make a label for text

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
