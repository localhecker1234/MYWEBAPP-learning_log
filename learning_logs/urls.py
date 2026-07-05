'''Defines URL pattern for learning_logs.'''

from django.urls import path

from . import views

app_name = 'learning_logs'  ## Helps django to distinguish from file of same name in other apps whithin the project.
urlpatterns = [
    #Home page
    path('', views.index, name = 'index'), # Blank string contains the url that is matched then processes the empty denotes the base url the homepage
    #Page that shows all the topics
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name= 'edit_entry')
]