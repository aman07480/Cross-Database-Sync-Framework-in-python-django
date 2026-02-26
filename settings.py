DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'main_db.sqlite3',
    },
    'replica': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'replica_db.sqlite3',
    }
}

TEMPLATES='BASE/DIR'