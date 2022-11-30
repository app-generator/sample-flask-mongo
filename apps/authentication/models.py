# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

class Users(db.Document, UserMixin):
    meta = {'collection': 'users'}
    username = db.StringField(required=True)
    email = db.EmailField(required=True)
    password = db.StringField(required=True)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(user_id):
    return Users.objects(pk=user_id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.objects(username=username).first()
    return user if user else None
