from fastapi.testclient import TestClient
from src.fast_zero.app import app
from http import HTTPStatus

def test_read_root_retorna_ok_e_ola_mundo():
    client = TestClient(app) # Arrange (Organização)
    response = client.get('/') # Act (Ação)
    assert response.status_code == HTTPStatus.OK # Assert (Verificação)
    assert response.json() == {'message': 'Hello, mundis!'}
