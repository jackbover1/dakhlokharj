from  django.conf.urls import url
from .import views
urlpatterns=[
    
    url(r'^sabte/kharj/$',views.sabte_kharj,name="sabte_kharj"),
    url(r'^sabte/dakhl/$',views.sabte_dakhl,name="sabte_dakhl")
    
    ]