from django.shortcuts import render, redirect,get_object_or_404
from .models import Assigned, addAssigned, addBillable
from resource.models import Resource
from datetime import date, timedelta, datetime


def choose_date(request, id):
    resource = Resource.objects.get(id=id)
    data={
        "resource" : resource
    }
    return render(request, "date.html", data)
    

def _Assigned_id(request):
    assign = request.session.session_key
    if not assign:
        assign = request.session.create()
    return assign

def Assigned1(request, id):
    if request.method == "POST":
        selectedDate = request.POST["date"]
        print(selectedDate,"this is the select date") 
        date_object = datetime.strptime(selectedDate, '%Y-%m-%d').date()
        # print(date_object,"date object")
        resource = Resource.objects.get(id=id)
        # print(resource)
        dateObjMonth = date_object.strftime("%m")

        print(date_object.strftime("%d"), "date-obj")
        date1 = date.today()
        date2 = date1 + timedelta(days=7)
        date3 = date2.strftime("%d")
        todayMonth = date2.strftime("%m")
        print(date2,"date2")
        try:
            assign_re = Assigned.objects.get(resource_id=_Assigned_id(request))
        except Assigned.DoesNotExist:
            assign_re= Assigned.objects.create(resource_id=_Assigned_id(request))
        assign_re.save()
        if dateObjMonth == todayMonth:            
            if date3 <= date_object.strftime("%d"):
                assign_resource = addAssigned.objects.create(
                    resource=resource,
                    assigned=assign_re,
                    select_date=date_object
                )
        
                assign_resource.save()
                # remAvailable = Resource.objects.get(name = resource.name)
                # remAvailable.delete()
                return redirect('home')
        
            if date1.strftime("%d") == date_object.strftime("%d"):
                assign_resource = addBillable.objects.create(
                    resource=resource,
                    select_date=date_object
                )
                assign_resource.save()
                # remAvailable = Resource.objects.get(name = resource.name)
                # remAvailable.delete()
                return redirect('home')
        
        if dateObjMonth > todayMonth:
            print("date is happening ")
            if int(dateObjMonth)%2 == 0:
                print("even date");
                even_date = 30 - int(date3) + int(date_object.strftime("%d"))
                if even_date >= 7:
                    assign_resource = addAssigned.objects.create(
                    resource=resource,
                    assigned=assign_re,
                    select_date=date_object
                    )
                    assign_resource.save()
                    return redirect('home')
            if int(dateObjMonth)%2 != 0:
                print("odd date")
                print(date2.strftime("%d"),"date2")
                print(date_object.strftime("%d"), "dateobjmonthhh")
                odd_date = 31 - int(date1.strftime("%d")) + int(date_object.strftime("%d"))
                if odd_date >= 7:
                    assign_resource = addAssigned.objects.create(
                    resource=resource,
                    assigned=assign_re,
                    select_date=date_object
                    )
                    assign_resource.save()
                    return redirect('home')

        return redirect('home')

    

def AssignedRemove(request,id):
    assign = Assigned.objects.get(resource_id=_Assigned_id(request))
    resource = get_object_or_404(Resource, id=id)
    assigned_resource = addAssigned.objects.get(resource=resource, assigned=assign)
    assigned_resource.delete()
    res = Resource.objects.create(name = resource.name, desc = resource.desc)
    res.save()
        
   
    return redirect('home')

def billable(request, id):
    date1 = date.today()
    # date2 = date1 + timedelta(days=7)

    resource = Resource.objects.get(id=id)
    try:
        assign_resource = addAssigned.objects.filter(resource=resource)
        if assign_resource.exists():
            assign_resource_bill = addBillable.objects.create(
            resource=resource,
            )
            assign_resource_bill.save()
        
            assign = Assigned.objects.get(resource_id=_Assigned_id(request))
            resource = get_object_or_404(Resource, id=id)
            assigned_resource = addAssigned.objects.get(resource=resource, assigned=assign)
            assigned_resource.delete()
    except addAssigned.DoesNotExist:
        pass
    return redirect('home')

    

def billableRemove(request,id):
    resource = get_object_or_404(Resource, id=id)
    assigned_resource = addBillable.objects.get(resource=resource)
    assigned_resource.delete()
    # res = Resource.objects.create(name = resource.name, desc = resource.desc)
    # res.save()
        
    return redirect('home')
