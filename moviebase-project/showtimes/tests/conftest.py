import pytest
from showtimes.models import Cinema, Screening

@pytest.fixture
def fake_cinema_data():
    a = Cinema()
    a.name = 'example1'
    a.city = 'example1a'
    a.save()
    return a




