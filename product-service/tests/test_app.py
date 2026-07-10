from app_factory import create_app


def test_health_endpoint():
    
    app = create_app()

    client = app.test_client()

    response = client.get("/api/v1/health")

    assert response.status_code == 200

    assert response.get_json() == {
        "success": True,
        "data": {
            "status": "healthy"
        }
    }