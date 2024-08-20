from django.shortcuts import render
from.models import phonebook
# Create your views here.
def fun1(request):
    return render(request,'home.html')

def disp(request):
    return render(request,'disp.html')

def upd(request):
    return render(request,'upd.html')

def back(request):
    return render(request,'home.html')

def addphone(request):
    con={}
    try: 
        name2=request.POST['name']
        phoneno=int(request.POST['phone'])
        phnlist=phonebook.objects.filter(Name=name2)

        if phnlist.exists():
            con['key']="phone number already exists."
            return render(request,'home.html',con)
        else:
            phnlist=phonebook(Name=name2,Phone=phoneno)
            phnlist.save()
            con['key']='phone number added successfully.'
            return render(request,'home.html',con)
    except Exception as e:
        print(e)
        con['key']='An error occured while processing the request.'
        return render(request,'home.html',con)

def display(request):
    dis=phonebook.objects.all()
    return render(request,'disp.html',{'phn':dis})

def update1(request):
    try:
        oldnme=request.POST['oldname']
        newnme=request.POST['newname']
        if oldnme==newnme:
            return render(request,'home.html',{'key1':'already exist'})
        phonebook.objects.filter(Name=oldnme).update(Name=newnme)
        return render(request,'upd.html',{'key1':'Updated'})
    except Exception as b:
        print(b)
        return render(request,'upd.html',{'key1':'not Updated'})

def delete(request):
    try:
        dlt=request.POST['dlt']
        phonebook.objects.filter(Name=dlt).delete()
        return render(request,'upd.html',{'del':'deleted'})
    except Exception as b:
        print(b)
        return render(request,'upd.html',{'del':'not deleted'})
