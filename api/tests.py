from django.test import SimpleTestCase
from rest_framework.test import APIClient


class HealthEndpointTests(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_endpoint_returns_ok(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_health_endpoint_rejects_post(self):
        response = self.client.post("/api/health/")

        self.assertEqual(response.status_code, 405)
