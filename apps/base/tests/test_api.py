import pytest
from rest_framework.test import APIClient
from apps.base.models import Base, Services, Tariffs

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Гарантирует, что база данных доступна во всех тестах"""
    pass

@pytest.fixture
def create_test_data():
    """Создаем тестовые данные с правильными полями"""
    Base.objects.create(
        title="Test Base",
        description="Test description",
        image="../../../media/base/photo_2025-02-20_15-36-35.jpg"
    )
    
    Services.objects.create(
        title="Test Service",
        description="Test description"
    )
    
    Tariffs.objects.create(
        title="Test Tariff",
        image="../../../media/base/photo_2025-02-20_15-36-35.jpg"
    )

@pytest.mark.django_db
def test_base_api(api_client, create_test_data):
    response = api_client.get("/ru/api/v1/base/base/")
    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]["title"] == "Test Base"

@pytest.mark.django_db
def test_services_api(api_client, create_test_data):
    response = api_client.get("/ru/api/v1/base/services/")
    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]["title"] == "Test Service"

@pytest.mark.django_db
def test_tariffs_api(api_client, create_test_data):
    response = api_client.get("/ru/api/v1/base/tariffs/")
    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]["title"] == "Test Tariff"
