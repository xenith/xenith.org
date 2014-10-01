#!/usr/bin/python
import os
from xenith.app import create_app
from xenith.settings import DevConfig, ProdConfig

if os.environ.get("XENITH_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)
