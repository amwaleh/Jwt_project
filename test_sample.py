import pytest
from autofixture import AutoFixture
from django.contrib.auth.models import User
import json




@pytest.fixture(scope='session')
def greet(request):
    fixture = AutoFixture(User, field_values={"username":"admin"})
    entry = fixture.create_one(True)
    return entry


@pytest.mark.django_db
def test_my_user(greet):
#check that both the assert object and the user model have the same data
    me = User.objects.first()
    assert me == greet
    assert me == greet

@pytest.mark.django_db
def test_my_mon(greet):
    be = greet
    assert be is not None


def test_login_redirect(client):
    # Check that unauthorised users are redirected to the LOgin page
    response = client.get('/')
    assert 302 == response.status_code
    assert'/accounts/login/' in response.url

@pytest.mark.django_db
def test_login(greet, client):
    #test if login is possible
    username = greet.username
    password =greet.password
    data ={'username': username,'password':password, 'email':greet.email}

    response = client.post("/api/users/", json.dumps(data), format="json", content_type="application/json")
    print (response)
    response = client.post("/api/api-token-auth/", json.dumps(data), format="json", content_type="application/json")
    print(response.data)
    assert 'token' in response.data


