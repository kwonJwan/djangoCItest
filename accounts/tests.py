from rest_framework.test import APIClient, APITestCase


# Create your tests here.
class AccountsUserInfoTestCase(APITestCase):
    def test_authorization(self):
        client = APIClient()
        response = client.get("/accounts/user-info/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "test success"})
