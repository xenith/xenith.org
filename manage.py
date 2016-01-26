#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from flask_script import (Manager, Shell, Server, prompt,
                          prompt_bool, prompt_pass)
from flask_script.commands import Clean, ShowUrls
from flask_migrate import MigrateCommand, Migrate
from flask import url_for

from xenith.app import create_app
from xenith.user.models import User
from xenith.settings import DevConfig, ProdConfig
from xenith.database import db

if os.environ.get("XENITH_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)
migrate = Migrate(app, db)
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
    import urllib.parse
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}"
                              .format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.command
def add_user():
    print('Set up a new user:')
    username = prompt('Username')
    email = prompt('E-mail')
    full_name = prompt('Full name')
    password = prompt_pass('Password')
    is_admin = prompt_bool('Admin user')

    user = User(username=username, email=email, password=password,
                full_name=full_name, admin=is_admin)

    db.session.add(user)

    try:
        db.session.commit()
    except DatabaseError as exc:
        print('Error creating user: \'{}\''.format(exc.message))
        sys.exit(1)

    print('User "{}" created.'.format(user.email))


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == '__main__':
    manager.run()
