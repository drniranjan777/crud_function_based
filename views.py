from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request): 
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pw = fm.cleaned_data['password']
        reg = User(name=nm, email=em, password=pw)
        reg.save()
        fm = StudentRegistration()
      #  fm.save()
      
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'add&show.html', {'form':fm, 'stu':stud})
  
  #Update&Edit views
  
def update_data(request,id):
  if request.method == 'POST':
    ui = User.objects.get(pk=id)
    fm = StudentRegistration(request.POST, instance=ui)
    if fm.is_valid():
      fm.save()
    return redirect('add&show')
  else:
    ui = User.objects.get(pk=id)
    fm = StudentRegistration(instance=ui)
    return render(request,'updates.html', {'form':fm})
      
  
  #delete data views
def delete_data(request,id):
  if request.method == 'POST':
    ui = User.objects.get(pk=id)
    ui.delete()
    return HttpResponseRedirect('/')
    
    
