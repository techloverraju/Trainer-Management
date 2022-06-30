from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Trainerapp.models import City, Trainer_Register, Trainer_Assign, Course


def home(request):
    return render(request,'index.html')


def log_read(request):
        user_name = request.POST["txtname"]
        user_pswd = request.POST["txtpswd"]
        user = authenticate(username=user_name,password=user_pswd)   #it will available in auth_user table.

        if user is not None:
            if user.is_superuser:
                login(request,user)
                return render(request,'admin_home.html')
        else:
            t1 = Trainer_Register.objects.get(tname=user_name)
            request.session['tid'] = t1.id
            request.session['tname'] = t1.tname
            return render(request,'trainer_home.html',{'data': t1})

# trainer registration
def trainer_register(request):
    city = City.objects.all()
    return render(request,"trainer_reg.html",{'City' : city})



def register_data(request):
    t1 = Trainer_Register()
    t1.tname = request.POST['txtname']
    t1.tage = request.POST['txtage']
    t1.tphone = request.POST['phn']
    t1.temail = request.POST['mail']
    t1.tpswd = request.POST['pswd']
    t1.tcity = City.objects.get(city_name= request.POST['ddlCity'])
    t1.save()
    return redirect('home')

def trainer_home(request):
    trainer_name = request.session['tname']
    return render(request,'trainer_home.html',{'data' : trainer_name})

# Admin home page
def admin_home(request):        # it will display admin_home page
    return render(request,'admin_home.html')


def triner_details(request):        # it will display trainer_details
    t1 = Trainer_Register.objects.all()
    return render(request,'triner_details.html',{'data' : t1})


def trainer_assign(request):        # it will display Assign batch
    t1=Trainer_Register.objects.all()
    c1=Course.objects.all()
    return render(request,'trainer_assign.html',{'Trainer':t1, 'Course':c1})


def assign_batch(request):
    t1 = Trainer_Assign()
    t1.tname = Trainer_Register.objects.get(tname=request.POST["ddlTname"])
    t1.batchno = request.POST["txtbatch"]
    t1.course = Course.objects.get(course_name=request.POST["ddlCourse"])
    t1.date = request.POST["txtDatetime"]
    t1.save()
    return redirect('trainerassign')


def batch_details(request):
    t1 = Trainer_Assign.objects.all()
    return render(request, 'batch_details.html', {'data': t1})

def trainer_batch(request):
    t1 = Trainer_Assign.objects.filter(tname=request.session['tid'])
    return render(request,'trainer_batch_details.html',{'data': t1})


def delete_batch(requset,id):
    t1=Trainer_Assign.objects.get(id=id)
    t1.delete()
    return redirect('details')


def update_batch(request,id):
    t2 = Trainer_Assign.objects.get(id=id)
    t1 = Trainer_Register.objects.all()
    c1 = Course.objects.all()

    if request.method == 'POST':
        t2.tname = Trainer_Register.objects.get(tname=request.POST["ddlTname"])
        t2.batchno = request.POST["txtbatch"]
        t2.course = Course.objects.get(course_name=request.POST["ddlCourse"])
        t2.date = request.POST["txtDatetime"]
        t2.save()
        return redirect('details')

    return render(request, 'update_batch.html', {'Trainer': t1, 'Course': c1, 'data' : t2})


