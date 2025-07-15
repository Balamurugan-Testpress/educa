from .base import *

print("✅ Loaded PRO settings")
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "yourdomain.com"]

ADMINS = [("admin", "rbalamurugan1000@hot.com")]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "educa",
        "USER": "educa",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
