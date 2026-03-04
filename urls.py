from django.urls import path
from . import views

app_name = "productes"

urlpatterns = [
    path('', views.productes_list, name='productes_list'),
    path('crear/', views.productes_create, name='productes_create'),
    path('<int:pk>/editar/', views.productes_update, name='productes_update'),
    path('<int:pk>/eliminar/', views.productes_delete, name='productes_confirm_delete'),
]