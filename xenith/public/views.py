# -*- coding: utf-8 -*-
"""Public section, including homepage and static pages."""
from flask import (Blueprint, request, render_template, flash, url_for,
                   redirect, session)
from flask_login import login_user, login_required, logout_user

from xenith.extensions import login_manager
from .models import User
from xenith.public.forms import LoginForm
from xenith.utils import flash_errors
from xenith.database import db

blueprint = Blueprint('public', __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm()
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", 'success')
            redirect_url = request.args.get("next") or url_for("public.home")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", 'success')
            redirect_url = request.args.get("next") or url_for("public.home")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/login.html", form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route("/about/")
def about():
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)


@blueprint.route("/calendar/")
def calendar():
    form = LoginForm(request.form)
    return render_template("public/calendar.html", form=form)


@blueprint.route("/contact/")
def contact():
    form = LoginForm(request.form)
    return render_template("public/contact.html", form=form)
