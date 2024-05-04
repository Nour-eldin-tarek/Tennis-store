from django.shortcuts import render
from .models import Post
from .models import Racet
from .models import Racet2
from .models import Cloth
from .models import Shose
from .models import Mix

# Create your views here.
def index(request):
    posts = Post.objects.all()
    postss = Racet.objects.all()
    posts3 = Racet2.objects.all()
    posts4 = Cloth.objects.all()
    posts5 = Shose.objects.all()
    posts6 = Mix.objects.all()
    return render(request, 'blog/index.html',{'posts': posts,'postss':postss,'posts3':posts3,'posts4':posts4,'posts5':posts5,'posts6':posts6})
def prouduct(request):
    posts = Post.objects.all()
    postss = Racet.objects.all()
    posts3 = Racet2.objects.all()
    posts4 = Cloth.objects.all()
    posts5 = Shose.objects.all()
    posts6 = Mix.objects.all()
    return render(request, 'blog/prouduct.html',{'posts': posts,'postss':postss,'posts3':posts3,'posts4':posts4,'posts5':posts5,'posts6':posts6})
def apout(request):
    return render(request, 'blog/apout.html')


