from server import create_app


def test_api_is_ok():
	app = create_app()
	with app.test_client() as client:
		response = client.get('/api')
		assert response.status_code == 200
