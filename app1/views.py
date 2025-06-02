from django.shortcuts import render , redirect
from .models import Db
from .forms import SampleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/admin")
def home(request):
    data = Db.objects.all()
    form = SampleForm()
    context = {"form":form, "data":data}
    if request.method == "POST":
        form_values = SampleForm(request.POST)
        if form_values.is_valid():
            form_values.save()
        return redirect("/")
    return render(request,"app1/home.html",context)

@login_required(login_url="/admin")
def update(request,pk):
    data = Db.objects.get(id=pk)
    form = SampleForm(instance=data)
    if request.method == "POST":
        form_values = SampleForm(request.POST,instance=data)
        if form_values.is_valid():
            form_values.save()
        return redirect("/")
    context = {"form":form,"data":data}
    return render(request,"app1/update.html",context)

@login_required(login_url="/admin")
def delete(request,pk):
    detail = Db.objects.get(id=pk)
    context = {"data":detail}
    if request.method == "POST":
        Db.delete(detail)
        return redirect("/")
    return render(request,"app1/delete.html",context)