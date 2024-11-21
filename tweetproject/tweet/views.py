from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseForbidden

def index(request):
    """
    Renders the homepage.
    """
    return render(request, 'index.html')

def tweet_list(request):
    """
    Displays a list of all tweets.
    """
    tweets = Tweet.objects.all().order_by('-created_at')  # Assuming 'created_at' is a field in the model
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    """
    Allows logged-in users to create a new tweet.
    """
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id): 
    """
    Allows the user to edit a tweet they own.
    """
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if tweet.user != request.user:
        return HttpResponseForbidden("You are not authorized to edit this tweet.")

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    """
    Allows the user to delete a tweet they own.
    """
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if tweet.user != request.user:
        return HttpResponseForbidden("You are not authorized to delete this tweet.")
    
    tweet.delete()
    return redirect('tweet_list')

def tweet_detail(request, tweet_id):
    """
    Displays details of a specific tweet.
    """
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})

def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after registration
            raw_password = form.cleaned_data.get('password1')  # Assuming 'password1' is the field in the form
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
