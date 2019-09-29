
from django.contrib import admin
from django.urls import path, include
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
