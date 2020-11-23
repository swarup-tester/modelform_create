from django.urls import path
from app_product import views


urlpatterns = [
    # path('',views.info,name='info'),
    path('create/',views.create,name='create'),
    # path('retrieve/',views.retrieve,name='retrieve'),
    # path('update/<int:id>',views.update,name='update'),
    # path('delete/<int:id>',views.delete,name='delete'),
]

