prefix = "/api/v1"


def test_health(test_app):
    response = test_app.get(f"{prefix}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
