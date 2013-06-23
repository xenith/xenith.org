"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blog


class BlogTest(TestCase):
    """ Test the Blog model """
    def test_str(self):
        blog = Blog(title="Test Blog", owner=User())

        self.assertEquals(
            str(blog),
            'Test Blog',
        )
