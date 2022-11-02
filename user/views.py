from urllib import request
from django.shortcuts import redirect, render
from Account.models import Post
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def home(request):
    users=Post.objects.all()
    context={'users':users}
    return render (request,'user/feed.html',context)

def post_feed(request):
    if request.method=="POST":
        caption=request.POST.get('caption')
        image=request.FILES.get('image')
        user=request.user
        user=Post(caption=caption,image=image,user=user)
        user.save()
        return redirect ('homepage')
    return render(request,'user/post.html')
        
def delete(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('homepage')

def profile_view(request,username):
    getuser=User.objects.filter(username=username)
    if getuser:
        profile=Profile.objects.get(user=getuser[0])
        context={
            'profile':profile
        }
        return render(request,'user/profile.html',context)
    else:
        return redirect('homepage')
