# -*- coding: utf-8 -*-
import os

os_env = os.environ


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    SECRET_KEY = os_env.get('XENITH_SECRET', 'secret-key')  # TODO: Change me
    SQLALCHEMY_DATABASE_URI = 'postgresql://typhoon.xenith.org/xenith.org'
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    ASSETS_DEBUG = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    SECRET_KEY = "sekrit!"
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SECRET_KEY = "sekrit!"
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing
