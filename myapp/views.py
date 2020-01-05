from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Computer
from myapp.forms import ComputerForm,ComputerSearch
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method=='POST':
        form=ComputerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'The computer has been added successfully!!')
            return HttpResponseRedirect('/comp/list/')
            form=ComputerForm()
    else:
        form=ComputerForm()
    context={
    'form':form
    }

    return render(request,'myapp/home.html',context)
@login_required
def ComputerList(request):
    comps=Computer.objects.all().order_by('-timestamp')
    form=ComputerSearch(request.POST or None)
    if request.method=='POST':
        queryset=Computer.objects.all()
        #.order_by('-timestamp').filter(computer_name__icontains=form['computer_name'].value().Users_name__icontains=form['Users_name'].value())
    context={
    'comps':comps,
    'form':form,
    }
    return render(request,'myapp/list.html',context)
@login_required
def ComputerEdit(request,pk):
    instance=Computer.objects.get(pk=pk)
    form =ComputerForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"The computer's details have been updated!")
        return HttpResponseRedirect('/comp/list/')
    context={
    'form':form
    }
    return render(request,'myapp/home.html',context)
@login_required
def computer_delete(request,pk):
    instance=Computer.objects.get(pk=pk)
    instance.delete()
    messages.warning(request,"The Computer have been deleted successfully!!")
    return HttpResponseRedirect('/comp/list/')
