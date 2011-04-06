'''
Created on Apr 5, 2011

@author: Mike_Edwards
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'emocaptcha',                      # Or path to database file if using sqlite3.
        'USER': 'you',                      # Not used with sqlite3.
        'PASSWORD': 'your_secret_stuff',                  # Not used with sqlite3.
        'HOST': 'your_host',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
