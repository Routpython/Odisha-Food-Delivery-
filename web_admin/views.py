from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render,redirect
from web_admin.models import AdminLoginModel,StateModel,CuisineModel,CityModel
from web_admin.admin_forms import StateForms,CuisineForms,CityForms
def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):

    return render(request,"pwn/openstate.html",{'state':StateForms(),'state_view':StateModel.objects.all()})


def openCity(request):
    return render(request,"pwn/opencity.html",{'city':CityForms(),'city_view':CityModel.objects.all()})


def openCusine(request):
    return render(request,"pwn/opencuisine.html",{'cuisine':CuisineForms(),'cui_view':CuisineModel.objects.all()})


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")

# State Section
def state_save(request):
    try:
        if request.method == 'POST':
            res=StateForms(request.POST,request.FILES)
            if res.is_valid():
                res.save()
                messages.success(request,'Saved Successfully')
                return  redirect('state')
            else:
                messages.error(request,res.errors)
                return redirect('state')
  #              return render(request, 'pwn/openstate.html',{"error":"State Already Exists",'state':StateForms(),'state_view':StateModel.objects.all()})
    except StateModel.DoesNotExist:
        return render(request, 'pwn/openstate.html',
                      {"error": "State Does Not Exist", 'state': StateForms(), 'state_view': StateModel.objects.all()})

def update(request):
    try:
        id = request.GET.get('state_id')
        state_update = StateModel.objects.get(id=id)
        sf=StateForms(instance=state_update)
        state_forms = StateForms(request.POST,request.FILES,instance=state_update)
        if request.method == 'POST':
            if state_forms.is_valid():
                state_forms.save()
                messages.success(request,'Updated Successfully')
                return redirect('state')
            else:
                messages.success(request,sf.errors)
                return redirect('state')
        return  render(request,'pwn/openstate.html',{'res':sf,'state_view':StateModel.objects.all()})

    except StateModel.DoesNotExist:
            return render(request, 'pwn/openstate.html', {'res': StateForms(),"error":"Enter Correct State",'state_view':StateModel.objects.all()})


def delete_state(request):
   try:
        if request.method ==  'GET':
            id = request.GET.get('state_id')
            StateModel.objects.get(id=id).delete()
            return render(request, 'pwn/openstate.html', {'state': StateForms(),"msg":"Deleted Successfully",'state_view':StateModel.objects.all()})
   except StateModel.DoesNotExist:
       return render(request, 'pwn/openstate.html',
                     {'state': StateForms(), "error": "Enter Correct State", 'state_view': StateModel.objects.all()})


#City Section


def city_save(request):
    try:
        if request.method == 'POST':
            city=CityForms(request.POST,request.FILES)
            if city.is_valid():
                city.save()
                return render(request, "pwn/opencity.html", {"msg":"City Saved Successfully",'city': CityForms(),'city_view':CityModel.objects.all()})
            else:
                messages.success(request,'City Already Exists')
                return  redirect('city')
    except CityModel.DoesNotExist:
        return render(request,"pwn/opencity.html",{'city':CityForms(),"error": "Enter Correct City"})


def update_city(request):
    try:
        id = request.GET.get('city_id')
        city=CityModel.objects.get(id=id)
        cf=CityForms(instance=city)
        city_forms=CityForms(request.POST,request.FILES,instance=city)
        if city_forms.is_valid():
            city_forms.save()
            messages.success(request,'Updated Successfully')
            return redirect('city')

        return render(request, 'pwn/opencity.html',{ 'up_city':cf ,'city_view': CityModel.objects.all()})
    except CityModel.DoesNotExist:
        return render(request, 'pwn/opencity.html',
                      {"error": "City Doesnot Exists", 'city': CityForms(), 'city_view': CityModel.objects.all()})


def delete_city(request):
    try:
        id = request.GET.get('city_id')
        qs = CityModel.objects.get(id=id)
        qs.delete()
        return render(request, 'pwn/opencity.html',
                  {'city': CityForms(), 'city_view': CityModel.objects.all(),
                   "msg": "Deleted Successfully", })
    except CityModel.DoesNotExist:
        return render(request, 'pwn/opencity.html',{'city': CityForms(), 'city_view': CityModel.objects.all(),
                       "msg": "Does Not Exist", })


#   Cusinie Part

def cuisine_save(request):
    try:
        if request.method == 'POST':
            cui=CuisineForms(request.POST,request.FILES)
            if cui.is_valid():
                cui.save()
                messages.success(request, 'Cuisine Saved Successfully ')
                return redirect('cuisine')

            else:
                return render(request, "pwn/opencuisine.html",
                              {"msg": "Cuisine Already Exists", 'cuisine': CuisineForms(),
                               'cui_view': CuisineModel.objects.all()})

    except CityModel.DoesNotExist:
        return render(request,"pwn/opencuisine.html",{'cuisine': CuisineForms(),"error": "Enter Correct Cuisine",'cui_view':CuisineModel.objects.all()})


def update_cui(request):
    try:
        id = request.GET.get('cui_id')
        cui=CuisineModel.objects.get(id=id)
        cui_fr=CuisineForms(instance=cui)
        cui_forms=CuisineForms(request.POST,request.FILES,instance=cui)
        if cui_forms.is_valid():
            cui_forms.save()
            messages.success(request,'Updated Successfully')
            return redirect('cuisine')
        return render(request, 'pwn/opencuisine.html',{ 'up_cui':cui_fr,'cui_view':CuisineModel.objects.all()})
    except CityModel.DoesNotExist:
        return render(request, 'pwn/opencuisine.html',
                      {"error": "City Doesnot Exists", 'cuisine': CuisineForms(),'cui_view':CuisineModel.objects.all()})


def delete_cui(request):
    try:
        id = request.GET.get('cui_id')
        qs=CuisineModel.objects.get(id=id)
        qs.delete()
        return render(request, 'pwn/opencuisine.html',
                      {'cuisine': CuisineForms(), 'cui_view': CuisineModel.objects.all(),
                       "msg": "Deleted Successfully", })

    except CuisineModel.DoesNotExist:
        return render(request, 'pwn/opencuisine.html',{'cuisine': CuisineForms(), 'cui_view': CuisineModel.objects.all(),
                       "msg": "Does Not Exist", })
