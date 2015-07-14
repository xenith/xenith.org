# -*- coding: utf-8 -*-
import datetime as dt
from hashlib import md5

from flask_login import UserMixin

from xenith.extensions import bcrypt
from xenith.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)


class Role(SurrogatePK, Model):
    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = ReferenceCol('users', nullable=True)
    user = relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        return '<Role({name})>'.format(name=self.name)


class User(UserMixin, SurrogatePK, Model):
    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)
    full_name = Column(db.String(100), nullable=True)
    active = Column(db.Boolean(), default=True)
    admin = Column(db.Boolean(), default=False)
    #posts = relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username, email, password=None, **kwargs):
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    def is_active(self):
        return self.active

    def is_admin(self):
        return self.admin

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def avatar(self, size=128):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    @property
    def first_name(self):
        return "{0}".format(self.full_name)

    def __repr__(self):
        return '<User({username!r})>'.format(username=self.username)

    def __unicode__(self):
        return self.username
