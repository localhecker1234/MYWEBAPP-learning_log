from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from . models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    '''This is homepage for learning log.'''
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    '''Shows all the topics'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''Shows a single topic and all its entries'''
    topic = Topic.objects.get(id = topic_id) # gets the topic according to its id
    check_topic_owner(request,topic)# If topic owner is now equal to user then raise error
    entries = topic.entry_set.order_by('-date_added') # - sign in front of date added reverses the order of entries
    context = {'topic': topic, 'entries': entries} # Store topics and entries in context dctionary
    return render(request, 'learning_logs/topic.html', context) # Sends context dictionary to the topic.html

@login_required
def new_topic(request):
    '''Add a new topic'''
    if request.method != 'POST': # Ye request method form par set hota hai
        #NO DATA SUBMITTED CREATE A BLANK FORM
        form = TopicForm() # Creates an instance of form and send it to user.
    else:
        #POST data submitted; process data.
        form = TopicForm(data=request.POST) # \Stores the data in request.Post
        if form.is_valid():
            new_topic = form.save(commit=False) #This doesn't save the new topic and allow to make changes to it before saving
            new_topic.owner = request.user # Set the topic making user as the owner of the platform
            new_topic.save()
            return redirect('learning_logs:topics')  # If this code run then redirect you to topics and save the form and
    # If form is valid then it is saved and redirected to topics
    # Redirect takes the name of the view and redirects the user to that view.
    # Display a blank or invalid form. 
    context = {'form': form} # If get request then give you new form.
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''Add a new entry for a particular topic'''
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        #No data submitted create a blank form.
        form = EntryForm()
    else:
        #POST data submitted and process the data
        form = EntryForm(data = request.POST)
        if form.is_valid(): # Checks the data matches all the requirements set up by us
            new_entry = form.save(commit = False) # Not save the form to the server stores it in variable
            new_entry.topic = topic # Set the topic attribute of the new_entry we pulled at the start. 
            new_entry.save() # Saves the new entry
            return redirect('learning_logs:topic', topic_id = topic_id)  ## Calling topic vies require one argument which is topic id which we fetched from the url itself.
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)
        

@login_required
def edit_entry(request, entry_id):
    '''Edit an existing entry'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(request,topic)## Allows only owner to edit the entry

    if request.method != 'POST':
        #Initial request;pre fill form with current entry
        form = EntryForm(instance=entry) # Maybe it prefills the form with current entry instancee
    else:
        #POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST) # Create a form with data from instance entry and updates any data from request.POST
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    
    context = {'entry': entry, 'topic':topic, 'form':form } # Ye topic form and entry ye three variables se associated value pahuncha dega
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(request,topic):
    if topic.owner != request.user:
        raise Http404