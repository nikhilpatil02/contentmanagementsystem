from django.test import TestCase, Client
import unittest
import json
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import random
from api.constants import *

# Create your tests here.
c = Client()
class ContentTestCases(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.data_to_save = {
        "first_name": "Rajiv","last_name": "Patil","email_id": "nikhil@gmail.com","password": "Password@123",
        "phone": 8605184858,"pincode": 411014,"address": "Pune","city": "Pune","state": "MH","country": "IND",
        "type_of_user": "Author"}
        self.data_with_wrong_mob = {"first_name": "Rajiv","last_name": "Patil","email_id": "nikhil@gmail.com","password": "Password@123",
        "phone": 860518485,"pincode": 411014,"address": "Pune","city": "Pune","state": "MH","country": "IND",
        "type_of_user": "Author"}
        self.data_with_wrong_pin = {"first_name": "Rajiv","last_name": "Patil","email_id": "nikhil@gmail.com","password": "Password@123",
        "phone": 8605184858,"pincode": 41014,"address": "Pune","city": "Pune","state": "MH","country": "IND",
        "type_of_user": "Author"}
        self.data_with_wrong_password = {"first_name": "Rajiv","last_name": "Patil","email_id": "nikhil@gmail.com","password": "password@123",
        "phone": 8605184858,"pincode": 410143,"address": "Pune","city": "Pune","state": "MH","country": "IND",
        "type_of_user": "Author"}
        self.data_content_save = {"user_id": 1, "title": "Demo check","body":"Demo Body","summary": "Demo summmary","categories": ["Category1","Category2"]}
        self.data_to_save_admin = {
        "first_name": "Rajiv","last_name": "Patil","email_id": "nikhil@gmail.com","password": "Password@123",
        "phone": 8605184858,"pincode": 411014,"address": "Pune","city": "Pune","state": "MH","country": "IND",
        "type_of_user": "Admin"}
    
    def test_save_user(self):
        self.user = User.objects.create_user(                                   
            username='test'+str(random.randint(10, 100000)),                                                                                   
            email='test@email.com',                                                                   
            password='test',                                                    
        )      
        token, created = Token.objects.get_or_create(user=self.user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/user/save',self.data_to_save)
        response_to_validate = response.content.decode('utf-8')
        self.assertEqual(json.loads(response_to_validate)['status'],SUCCESS )

    def test_save_user_mobile_check(self):
        self.user = User.objects.create_user(                                   
            username='test'+str(random.randint(10, 100000)),                                                                                   
            email='test@email.com',                                                                   
            password='test',                                                    
        )      
        token, created = Token.objects.get_or_create(user=self.user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/user/save',self.data_with_wrong_mob)
        response_to_validate = response.content.decode('utf-8')
        self.assertEqual(json.loads(response_to_validate)['status'], FAILURE)
    
    def test_save_user_pin_check(self):
        self.user = User.objects.create_user(                                   
            username='test'+str(random.randint(10, 100000)),                                                                                   
            email='test@email.com',                                                                   
            password='test',                                                    
        )      
        token, created = Token.objects.get_or_create(user=self.user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/user/save',self.data_with_wrong_pin)
        response_to_validate = response.content.decode('utf-8')
        self.assertEqual(json.loads(response_to_validate)['status'], FAILURE)
    
    def test_save_user_password_check(self):
        self.user = User.objects.create_user(                                   
            username='test'+str(random.randint(10, 100000)),                                                                                   
            email='test@email.com',                                                                   
            password='test',                                                    
        )      
        token, created = Token.objects.get_or_create(user=self.user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/user/save',self.data_with_wrong_password)
        response_to_validate = response.content.decode('utf-8')
        self.assertEqual(json.loads(response_to_validate)['status'], FAILURE)
        
    def test_save_content_check(self):
        self.user = User.objects.create_user(                                   
            username='test'+str(random.randint(10, 100000)),                                                                                   
            email='test@email.com',                                                                   
            password='test',                                                    
        )      
        token, created = Token.objects.get_or_create(user=self.user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/user/save',self.data_to_save)
        response_to_validate = response.content.decode('utf-8')
        response = self.client.post('/content/save',self.data_content_save)
        response_to_validate = response.content.decode('utf-8')
        self.assertEqual(json.loads(response_to_validate)['status'], SUCCESS)
        
    def test_save_content_check_admin(self):
        self.user = User.objects.create_user(                                   
            username='test'+str(random.randint(10, 100000)),                                                                                   
            email='test@email.com',                                                                   
            password='test',                                                    
        )      
        token, created = Token.objects.get_or_create(user=self.user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/user/save',self.data_to_save_admin)
        response_to_validate = response.content.decode('utf-8')
        data = {}
        data['user_id'] = json.loads(response_to_validate)['data']['id']
        data['title'] = "Test cases"
        data['body'] = "Test cases"
        data['summary'] = "Test cases"
        data['categories'] = ["Category1","Category2"]
        response = self.client.post('/content/save',data)
        response_to_validate = response.content.decode('utf-8')
        self.assertEqual(json.loads(response_to_validate)['status'], FAILURE)
    
    def test_update_content(self):
        self.user = User.objects.create_user(                                   
            username='test'+str(random.randint(10, 100000)),                                                                                   
            email='test@email.com',                                                                   
            password='test',                                                    
        )      
        token, created = Token.objects.get_or_create(user=self.user)                
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/user/save',self.data_to_save)
        response_to_validate = response.content.decode('utf-8')
        data = {}
        user_id = json.loads(response_to_validate)['data']['id']
        data['user_id'] = user_id
        data['title'] = "Test cases"
        data['body'] = "Test cases"
        data['summary'] = "Test cases"
        data['categories'] = ["Category1","Category2"]
        response = self.client.post('/content/save',data)
        response_to_validate = response.content.decode('utf-8')
        content_id = json.loads(response_to_validate)['data']['id']
        data_to_update = {}
        data_to_update['user_id'] = user_id
        data_to_update['title'] = "Test cases Update"
        data_to_update['body'] = "Test cases"
        data_to_update['summary'] = "Test cases"
        data_to_update['categories'] = ["Category1","Category2"]
        data_to_update['content_id'] = content_id
        response = self.client.post('/content/update',data_to_update)
        response_to_validate = response.content.decode('utf-8')
        print(response_to_validate)
        self.assertEqual(json.loads(response_to_validate)['status'], SUCCESS)