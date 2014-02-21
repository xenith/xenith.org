# -*- coding: utf-8 -*-
# Python3 compatability
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail


# Subclass AbstractUser
@python_2_unicode_compatible
class User(AbstractUser):
    def __str__(self):
        return self.username


# @python_2_unicode_compatible
# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#         db_index=True,
#     )
#     username = models.CharField(_('username'), max_length=30, unique=True, blank=True,
#         help_text=_('Required. 30 characters or fewer. Letters, digits and '
#                     '@/./+/-/_ only.'),
#         validators=[
#             validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
#         ])
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=50, blank=True)
#     is_staff = models.BooleanField(_('staff status'), default=False,
#         help_text=_('Designates whether the user can log into this admin '
#                     'site.'))
#     is_active = models.BooleanField(_('active'), default=True,
#         help_text=_('Designates whether this user should be treated as '
#                     'active. Unselect this instead of deleting accounts.'))
#     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#     is_admin = models.BooleanField(default=False)

#     #objects = MyUserManager()
#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_absolute_url(self):
#         return "/users/%s/" % urlquote(self.username)

#     def get_full_name(self):
#         """
#         Returns the first_name plus the last_name, with a space in between.
#         """
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         "Returns the short name for the user."
#         return self.first_name

#     def email_user(self, subject, message, from_email=None):
#         """
#         Sends an email to this User.
#         """
#         send_mail(subject, message, from_email, [self.email])

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
