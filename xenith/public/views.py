# -*- coding: utf-8 -*-
"""Public section, including homepage and static pages."""
from flask import (Blueprint, request, render_template, flash, url_for,
                   redirect, session, abort)
from flask_login import login_user, login_required, logout_user, current_user

from xenith.extensions import login_manager
from xenith.user.models import User
from xenith.public.forms import LoginForm
from xenith.utils import flash_errors
from xenith.database import db

blueprint = Blueprint('public', __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(int(id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    user = current_user
    form = LoginForm()
    return render_template("public/home.html", form=form, user=user)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for("public.home"))
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            session['remember_me'] = form.remember_me.data
            login_user(form.user, remember=form.remember_me.data)
            flash("You are logged in.", 'success')
            next = request.args.get('next')
            #if not next_is_valid(next):
            #    return abort(400)
            return redirect(next or url_for("public.home"))
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
