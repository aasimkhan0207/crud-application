from django.urls import reverse, resolve

class TestUrls:
    def test_detail_url(self):
        path = reverse('show')
        assert resolve(path).view_name == 'show'

    def test_emp(self):
        path = reverse('emp')
        assert resolve(path).view_name == 'emp'

    def test_user_index(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'

    def test_edit(self):
        path = reverse('edit', kwargs={'id':1})
        assert resolve(path).view_name == 'edit'

    def test_update(self):
        path = reverse('update',  kwargs={'id':1})
        assert resolve(path).view_name == 'update'

    def test_register(self):
        path = reverse('register')
        assert resolve(path).view_name == 'register'

    def test_edit(self):
        path = reverse('edit',kwargs={'id':10})
        assert resolve(path).view_name == 'edit'
