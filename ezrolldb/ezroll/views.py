from django.shortcuts import render, redirect
from .models import Member
from .models import Course
from .forms import MemberForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from django.contrib import messages

# Create your views here.
def home(request):
    all_members= Member.objects.all
    return render(request, 'index.html', {'all': all_members}) #passing stuff into the main webpage 
@csrf_exempt


def register(request):
    if request.method=="POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            name = request.POST['name']
            duid = request.POST['duid']
            major = request.POST['major']
            minor = request.POST['minor']
            PoCRN = request.POST['PoCRN']
            PrCRN = request.POST['PrCRN']
            elec = request.POST['elec']

            messages.success(request, ('Your form has errors!'))
            return render(request, 'register.html', {'name':name,
            'duid':duid,
            'major':major,
            'minor':minor,
            'PoCRN':PoCRN,
            'PrCRN':PrCRN,
            'elec':elec,
                                                     
                                                     
                                                     })
        messages.success(request, ('Success!'))
        return render(request, 'schedule.html', {})
    else:
        return render(request, 'register.html', {}) #passing stuff into the main webpage 
    


def search_courses(request):
    if request.method=="POST":
            
        PoCRN=request.POST['PoCRN']
        schedule = Course.objects.filter(CRN__contains=PoCRN)


        return render(request, 'schedule.html', 
                  {'PoCRN':PoCRN, 'schedule':schedule})
    else:
        return render(request, 'schedule.html', 
                  {})