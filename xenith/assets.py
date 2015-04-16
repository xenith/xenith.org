# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment

css = Bundle(
    "css/skel.css",
    "css/style.css",
    Bundle(
        "sass/style.sass",
        filters="sass"
    ),
    filters="cssmin",
    output="public/css/common.css"
)

js = Bundle(
    "js/init.js",
    filters='jsmin',
    output="public/js/common.js"
)

assets = Environment()

assets.register("js_all", js)
assets.register("css_all", css)

