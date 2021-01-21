from django.urls import path
from app1.views import Home,About,Contact,Packages,AddRestaurants,addRestaurantsDetails,res_Delete,res_Edit,res_Update,res_Menu,Add_menu

urlpatterns = [

    path("", Home),
    path("about", About),
    path("packages", Packages),
    path("contact", Contact),
    path("addrestaurants", AddRestaurants),
    path("AddRestaurantdetails",addRestaurantsDetails),
    path('delete_res/<int:id>',res_Delete),
    path('edit_res/<int:id>',res_Edit),
    path('UpdateRestaurantdetails/<int:id>',res_Update),
    path('addmenu/<int:data>',Add_menu),
    path('menu/<int:id>',res_Menu),
]