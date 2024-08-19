from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    if request.method =="POST":
      form = ImageForm(request.POST, request.FILES)  
      if form.is_valid():
       form.save()
       messages.success(request,'Successfully Saved')
    form = ImageForm()
    img = Image.objects.all()
    #set up pagination
    p = Paginator(Image.objects.all(),4)
    page = request.GET.get('page')
    images = p.get_page(page)

    return render(request,'myapp/home.html',{'images':images,'img':img,'form':form})

