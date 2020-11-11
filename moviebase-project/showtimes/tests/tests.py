import pytest
from showtimes.models import Cinema


@pytest.mark.django_db
def test_post_cinema(client, fake_cinema_data):
    cinemas_before = Cinema.objects.count()
    new_cinema = {"name": "aaa", "city": "bbb"}
    response = client.post("/cinemas/", new_cinema, format='json')
    assert response.status_code == 201
    assert Cinema.objects.count() == cinemas_before + 1



@pytest.mark.django_db
def test_get_cinema_list(client):
    response = client.get("/cinemas/", {}, format='json')

    assert response.status_code == 200
    assert Cinema.objects.count() == len(response.data)


#@pytest.mark.django_db
#def test_get_cinema_detail(client):
#    response = client.get("/cinemas/1", {}, format='json')

#    assert response.status_code == 200
#    for field in ("name", "city"):
#        assert field in response.data



