from django.test import TestCase

# Create your tests here.
import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from review.models import *
from review.serializers import *


class CopmanyTestCase(APITestCase):
    url = reverse("review:company")

    def setUp(self):
        self.username = "john"
        self.password = "dough"
        self.user = User.objects.create_user(self.username, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_company(self):
        response = self.client.post(self.url, {"name": "Consumers"})
        self.assertEqual(201, response.status_code)

    def test_create_company_fail(self):
        response = self.client.post(self.url, {"name": "Consumers"})
        response_fail = self.client.post(self.url, {"name": "Consumers"})
        self.assertEqual(400, response_fail.status_code)


class UserCreateTestCase(APITestCase):
    url = reverse("review:create")

    def test_create_user(self):
        response = self.client.post(self.url, {"username": "john", "password": "dough"})
        self.assertEqual(201, response.status_code)


class ReviewTestCase(APITestCase):
    url = reverse("review:reviews")

    def setUp(self):
        self.username = "john"
        self.password = "dough"
        self.user = User.objects.create_user(self.username, self.password)
        self.create_company()
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def create_company(self):
        self.company = Company.objects.create(name="Consumers")

    def test_create_review(self):
        response = self.client.post(self.url, {"title": "Review Title",
                                               "rating": 4,
                                               "summary": "This is a summary part, this an be long, two lines added.",
                                               "ip_address": "192.168.0.0.1",
                                               "submission_date": "2019-04-09",
                                               "company": "Consumers"
                                               })
        self.assertEqual(201, response.status_code)

    def test_create_review_fail(self):
        response = self.client.post(self.url, {"title": "Review Title",
                                               "rating": 2,
                                               "summary": "This is a summary part, this an be long, two lines added.",
                                               "ip_address": "192.168.0.0.1",
                                               "submission_date": "2020-04-10",
                                               "company": "not exists"
                                               })
        self.assertEqual(400, response.status_code)

    def test_get_reviews(self):
        review = Review.objects.create(user=self.user, title="Review Title", rating=4,
                                       summary="This is a summary part, this an be long, two lines added.",
                                       ip_address="192.168.0.0.1", company=Company.objects.get(name="Consumers"),
                                       submission_date="2020-04-11")
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(json.loads(response.content)), Review.objects.count())

    def test_get_reviews_fail(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertFalse(len(json.loads(response.content)), Review.objects.count())
