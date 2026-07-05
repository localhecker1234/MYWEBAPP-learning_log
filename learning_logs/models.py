from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    '''A topic the user is learning about'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   #If user is deleted all the models with him will be deleted as well
    
    def __str__(self):
        '''Return a string representation of the model.'''  
        return self.text  ## Returns  string stored in text attribute
    

class Entry(models.Model):
    '''Something specific learned about a topic.'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: # This class holds special info for managing a class.
        verbose_name_plural = 'entries'  # Tells django to refer to multiple entries as entries not entrys

    def __str__(self):
        '''Return a string representation of the model.'''
        if len(self.text) >=50:
            return f"{self.text[:50]}..." ## Shows 50 words from the start of entry
        else:
            return f""