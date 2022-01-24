from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.Home,name = 'home'),
    path('home',views.Home,name = "home"),
    path('cat',views.category,name = "cat"),
    path('view/<int:id>',views.View_options,name = "view"),
    path('reg',views.Register_form,name ="reg"),
    path('log',views.Login,name = "log")

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
