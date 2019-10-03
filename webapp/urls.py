
from django.contrib import admin
from django.urls import path, include
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('emp', views.emp, name='emp'),
    path('show', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete),
]
