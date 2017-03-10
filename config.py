# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# administrator list
ADMINS = ['suffianhamzah@gmail.com']

# pagination limit
POSTS_PER_PAGE = 3

# whoosh
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# email server
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# admin list
ADMINS = ['suffian_aris@yahoo.com']

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = ''
MS_TRANSLATOR_CLIENT_SECRET = ''