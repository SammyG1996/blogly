import app
from unittest import TestCase

class TestRoutes(TestCase):
  '''This is a test for the routes within the application'''
  def test_home(self): 
    with app.app.test_client() as client:
        # can now make requests to flask via `client`
        resp = client.get('/')
        html = resp.get_data(as_text=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(' <div class="col-12 col-md-8 d-flex justify-content-center">', html)

  def test_users(self): 
    with app.app.test_client() as client:
        resp = client.get('/users')
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
        
  def test_profile_edit_page(self): 
    with app.app.test_client() as client: 
      resp = client.get('/users/1/edit')
      html = resp.get_data(as_text=True)
      self.assertEqual(resp.status_code, 200)
      self.assertIn('<label for="first" class="form-label fs-5 text-light">First Name</label>', html)
  

  def test_new_post_page(self): 
    with app.app.test_client() as client: 
      resp = client.get('/users/1/post/new')
      html = resp.get_data(as_text=True)
      self.assertEqual(resp.status_code, 200)
      self.assertIn('<h3 class="text-light">New Post:</h>', html)

  def test_show_specific_post_page(self): 
    with app.app.test_client() as client: 
      resp = client.get('/posts/1')
      html = resp.get_data(as_text=True)
      self.assertEqual(resp.status_code, 200)
      self.assertIn('<a href="/posts//edit" class="btn btn-success m-1">Edit</a>', html)

  def test_edit_specific_post_page(self): 
    with app.app.test_client() as client: 
      resp = client.get('/posts/1/edit')
      html = resp.get_data(as_text=True)
      self.assertEqual(resp.status_code, 200)
      self.assertIn('<h3 class="text-light">Edit Post:</h>', html)