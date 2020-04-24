import unittest
import requests
url = 'http://218.17.39.34:7909/AuthService/oauth/token'
headers = {'Authorization': 'Basic TUFOQUdFUjoxMjM0NTY='}
class MyTestCase(unittest.TestCase):
    def test_login(self):
        data = {'username': 'zhou', 'password': '123456', 'grant_type': 'password'}
        res = requests.post(url=url, headers=headers, data=data)
        self.assertIn('access_token',res.json())

    def test_login_error(self):
        data = {'username': 'zhou', 'password': '123', 'grant_type': 'password'}
        res = requests.post(url=url, headers=headers, data=data)
        self.assertIn('access_token',res.json())

if __name__ == '__main__':
    unittest.main()
