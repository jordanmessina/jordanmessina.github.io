---
author: Jordan Messina
date: '2010-06-12'
layout: post
comments: true
slug: django-allow-users-to-log-in-using-email-rather-than-username
status: publish
title: Django - Allow users to log in using email rather than username
wordpress_id: '145'
---

One of the annoying things about Django is that it doesn't allow logins via
email out of the box if you're using their built-in user authentication . You
must create your own authentication backend in order to accomplish this.
However, one of the things I love about Django is the ability to create
authentication backends without too much of a headache. This comes in handy
when dealing with things like allowing users to log in via Twitter, Facebook
Connect, any OpenID providers, or allowing them to login via email and
password.

Django authentication backends are quite simple, essentially whenever you call
the `django.contrib.auth.authenticate()` function, Django uses the
authenticate method in any of the classes specified by the
`AUTHENTICATION_BACKENDS` tuple set in your settings.py. If one of the classes
fails to authenticate the user, Django moves on to the next one until either
one successfully returns a user object or there are no other backends to
attempt, in which case it results in a failed login. A very simple
authentication backend which allows users to login via email rather than
username is the following code in backends.py:

    from django.conf import settings 
    from django.contrib.auth.models import User

    class EmailModelBackend(object): 
        def authenticate(self, username=None, password=None): 
            try: 
                user = User.objects.get(email=username)
                if user.check_password(password): 
                    return user 
            except User.DoesNotExist: 
                return None

        def get_user(self, user_id): 
            try: 
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None

And you simply need to add to your settings.py: 

    AUTHENTICATION_BACKENDS = (
        'path.to.this.backends.EmailModelBackend',
        'django.contrib.auth.backends.ModelBackend', 
    )

I generally place my backends in whatever app I create to store extra user
info, but you can put it anywhere, just make sure it's in your PYTHONPATH.

