from django.shortcuts import render, redirect
from .forms import ExpertForm
from .models import Expert
from django.core.paginator import Paginator



# Create your views here.


def collections(request):
    context = {'collections':Expert.objects.all()}

    return render(request, "expert_register/collections.html",context)

def show_experts(request,id):
    expert = Expert.objects.get(pk=id)
    return render(request,'expert_register/show_experts.html',{'expert':expert})


def searchbar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        experts = Expert.objects.all().filter(expertname__contains=searched)
        return render(request, 'expert_register/search_expert.html',{'searched':searched,'experts':experts})
    else:
        return render(request, 'expert_register/search_expert.html', {})

def home(request,id=0):

    if request.method == "GET":
        if id==0:
            form = ExpertForm()
        else:
            expert = Expert.objects.get(pk=id)
            form = ExpertForm(instance=expert)
        return render(request, "expert_register/home.html",{'form':form})
    else:
        if id==0:
            form = ExpertForm(request.POST)
        else:
            expert = Expert.objects.get(pk=id)
            form = ExpertForm(request.POST,instance= expert)
        if form.is_valid():
            form.save()
        return redirect('/home/collections')




def delete(request,id):
    expert = Expert.objects.get(pk=id)
    expert.delete()
    return redirect('/home/collections')

