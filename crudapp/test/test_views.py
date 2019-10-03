from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer
from django.test import Client

from crudapp.views import show
import pytest

@pytest.mark.django_db
class TestViews:

    #test whether we can access when we are autheicated
    def test_show_autheticated(self):
        path = reverse('show')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = show(request)
        assert response.status_code == 200

    #test whether we can access when we are unautheicated
    def test_show_unautheticated(self):
        path = reverse('show')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = show(request)
        assert response.status_code == 302 # redirect code

    def test_superuser(self):
        c = Client()
        response = c.post('/accounts/login/', {'username': 'superuser', 'password': '123'})
        assert response.status_code == 200
