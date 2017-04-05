from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='*1hvq1ebcfy2w(bj@efvv-gu@*i^%k-=73@1mrqxys1mru&gyt')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
