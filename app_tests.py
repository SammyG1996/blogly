import app
from unittest import TestCase

class TestRoutes(TestCase):
  '''This is a test for the routes within the application'''
  def test_home(self): 
    with app.app.test_client() as client:
        # can now make requests to flask via `client`
        resp = client.get('/', follow_redirects=True)
        html = resp.get_data(as_text=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<div class="card m-1" style="width: 18rem;">', html)

  def test_users(self): 
    with app.app.test_client() as client:
        resp = client.get('/', follow_redirects=True)
        html = resp.get_data(as_text=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('<div class="card m-1" style="width: 18rem;">', html)

  def test_profile_page(self): 
    with app.app.test_client() as client: 
      resp = client.get('/users/1')
      html = resp.get_data(as_text=True)
      self.assertEqual(resp.status_code, 200)
      self.assertIn('<h5 class="card-title">Samuel Gonzalez</h5>', html)
       

  def test_add_user(self): 
    with app.app.test_client() as client:
      resp = client.get('/users/new')
      html = resp.get_data(as_text=True)
      self.assertEqual(resp.status_code, 200)
      self.assertIn('<h3 class="text-light">Create A New User:</h>', html)
        