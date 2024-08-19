from django.shortcuts import render,redirect,get_object_or_404
from . models import Note
from .forms import NoteForm
from django.contrib import messages


def index1(request):
    notes = Note.objects.all()
    return render(request,"index1.html",{"notes":notes})

# def base1(request):
#     return render(request,"base1.html")

def index(request):
    notes = Note.objects.all()
    return render(request,"index.html",{"notes":notes})

def new_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,"new_note.html",{"form":form})




def update(request,pk):
    note =Note.objects.get(id = pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,"update.html",{"form":form})

def delete(request,pk):
     note =Note.objects.get(id = pk)
     form = NoteForm(instance=note)
     if request.method == 'POST':
       note.delete()
       messages.info(request,"Note has been delete successfully")
     return render(request,"delete.html",{"form":form})
   

def search(request):
    if request.method =='POST':
      search_value = request.POST["search"]
      notes = Note.objects.filter(title__icontains = search_value)  | Note.objects.filter(text = search_value)  
      return render(request,"search.html",{"notes":notes})
    return redirect('index')

