from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Add at top
from django import forms
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


def index(request):
    breaking_news = News.objects.all().order_by('-created_at')  # No slicing: get all news
    # or if you don't have a special field, just latest 10 news:
    # breaking_news = News.objects.all().order_by('-created_at')[:10]

    news = News.objects.all().order_by('-created_at')
    context = {
        'breaking_news': breaking_news,
        'news': news,
    }
    return render(request, 'pages/index.html', context)


from .forms import CommentForm
from .models import Comment

def news_detail(request, slug):
    news_item = News.objects.get(slug=slug)
    comments = Comment.objects.filter(news=news_item).order_by('-created_at')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.user = request.user
            comment.save()
            return redirect('news_detail', slug=slug)
    else:
        form = CommentForm()
    
    data = {
        'news': news_item,
        'latest_news': News.objects.exclude(id=news_item.id).order_by('-id')[:5],
        'comments': comments,
        'form': form,
    }
    return render(request, 'pages/news_detail.html', data)

def national(request):
    data = {
        'news': News.objects.filter(category__slug='national'),
    }
    return render(request, 'pages/national.html', data)

def international(request):
    data = {
        'news': News.objects.filter(category__slug='international'),
    }
    return render(request, 'pages/international.html', data)

def business(request):
    data = {
        'news': News.objects.filter(category__slug='business'),
    }
    return render(request, 'pages/business.html', data)

def sports(request):
    data = {
        'news': News.objects.filter(category__slug='sports'),
    }
    return render(request, 'pages/sports.html', data)

def entertainment(request):
    data = {
        'news': News.objects.filter(category__slug='entertainment'),
    }
    return render(request, 'pages/entertainment.html', data)

def technology(request):
    data = {
        'news': News.objects.filter(category__slug='technology'),
    }
    return render(request, 'pages/technology.html', data)

def health(request):
    data = {
        'news': News.objects.filter(category__slug='health'),
    }
    return render(request, 'pages/health.html', data)

def education(request):
    data = {
        'news': News.objects.filter(category__slug='education'),
    }
    return render(request, 'pages/education.html', data)

def travels(request):
    data = {
        'news': News.objects.filter(category__slug='travels'),
    }
    return render(request, 'pages/travels.html', data)

def music(request):
    data = {
        'news': News.objects.filter(category__slug='music'),
    }
    return render(request, 'pages/music.html', data)

def search(request):
    query = request.GET.get('query', '')
    if query:
        news = News.objects.filter(title__icontains=query)
    else:
        news = News.objects.none()
    
    data = {
        'news': news,
        'query': query,
    }
    return render(request, 'pages/search.html', data)

# views.py
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'layouts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'layouts/login.html')

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'layouts/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'layouts/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')




from django.shortcuts import render

def terms_of_service(request):
    return render(request, 'Other/terms_of_service.html')

def privacy_policy(request):
    return render(request, 'Other/privacy_policy.html')




