from django.shortcuts import render,redirect
from .models import addRestaurants,addMenu

# Main Views...
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Packages(request):
    return render(request, 'packages.html')

def AddRestaurants(request):
    all_restaurants = addRestaurants.objects.all()
    return render(request, 'addrestaurants.html', {'datas':all_restaurants}) 

    
#Operations....

def addRestaurantsDetails(request):
    if request.method == 'POST':
           
      name=request.POST.get('r_name')
      ownername=request.POST.get('r_ownername')
      mobileno=request.POST.get('r_mobileno')
      address=request.POST.get('r_address')
      R_type=request.POST.get('r_type')
      
      data=addRestaurants(R_name=name,R_ownername=ownername,R_mobileno=mobileno,R_adress=address,R_type=R_type)
      data.save()
      
      ms='RESTAURANT Added!!'
    
        
      all_restaurants = addRestaurants.objects.all()
      
      return render(request, 'addrestaurants.html', {'msg':ms,'datas':all_restaurants}) 

    else:
        return redirect('/addrestaurants')


def res_Delete(request,id):
    instance = addRestaurants.objects.get(id=id)
    instance.delete()
    print("deleted")
    return redirect('/addrestaurants')

def res_Edit(request,id):
    data=addRestaurants.objects.get(id=id)
    return render(request, 'edit.html',{'data':data})

def res_Update(request,id):
    if request.method == 'POST':
           
      name=request.POST.get('r_name')
      ownername=request.POST.get('r_ownername')
      mobileno=request.POST.get('r_mobileno')
      address=request.POST.get('r_address')
      R_type=request.POST.get('r_type')
      
      data=addRestaurants(id,R_name=name,R_ownername=ownername,R_mobileno=mobileno,R_adress=address,R_type=R_type)
      data.save()
      
      ms='Data Updated!!'
    
        
      all_restaurants = addRestaurants.objects.all()
      
      return render(request, 'addrestaurants.html', {'msg':ms,'datas':all_restaurants}) 

    else:
      return redirect('/edit_res')

def res_Menu(request,id):
    
    return render(request, 'menu.html',{'data':id})

def Add_menu(request,data):
    if request.method == 'POST':
      id=addRestaurants.objects.get(id=data)
      print(id)
      m=addMenu()  
           
      m.id = request.POST.get(id)
      m.Dish_name=request.POST.get('dishname')
      m.Dish_type=request.POST.get('dishtype')
      m.Dish_price=request.POST.get('dishprice')
      m.save()

    msg="added!!"
    return render(request, 'menu.html',{'msg':msg})


       