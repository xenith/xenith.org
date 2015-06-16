#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from flask_script import (Manager, Shell, Server, prompt
                          prompt_bool, prompt_pass)
from flask_migrate import MigrateCommand
from flask import url_for

from xenith.app import create_app
from xenith.public.models import User
from xenith.settings import DevConfig, ProdConfig
from xenith.database import db

if os.environ.get("XENITH_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)
TEST_CMD = "py.test tests"


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db, 'User': User}


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main(['tests', '--verbose'])
    return exit_code


@manager.command
def list_routes():
    """List all the routes configured in the application."""
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}"
                              .format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line


@manager.command
def add_user():
    print(u'Set up a new user:')
    username = prompt('Username')
    email = prompt('E-mail')
    first_name = prompt('First name')
    last_name = prompt('Last name')
    password = prompt_pass('Password')
    is_admin = prompt_bool('Admin user')

    user = User(username=username, email=email, password=password,
                first_name=first_name, last_name=last_name, is_admin=is_admin,
                is_active=True)

    db.session.add(user)

    try:
        db.session.commit()
    except DatabaseError as exc:
        print(u'Error creating user: \'{}\''.format(exc.message))
        sys.exit(1)

    print(u'User "{}" created.'.format(user.email))


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
