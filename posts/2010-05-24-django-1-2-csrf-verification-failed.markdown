---
author: Jordan Messina
date: '2010-05-24'
layout: post
comments: true
slug: django-1-2-csrf-verification-failed
status: publish
title: Django 1.2 - CSRF verification failed. Request aborted.
wordpress_id: '140'
---

I was getting this 403 error today while attempting to make a POST request to
a view: 

> 403 Forbidden

> CSRF verification failed. Request aborted.

> Help Reason given for failure:

> CSRF cookie not set.

**Edit 10/29/2010**
I've modified this post to only contain the proper way of resolving the issue. You can read about Cross Site Request Forgeries [here](http://www.squarefree.com/securitytips/web-developers.html#CSRF) and Django's protection mechanisms [here](https://docs.djangoproject.com/en/dev/ref/contrib/csrf/) 


To resolve the 403 issue, you want to add the csrf_token template tag within your form somewhere. This adds a hidden div with the value of the input as the csrf token:
``` html anything.html
<form action="..." method="POST">
    {% csrf_token %}
    ...
</form>
```

If you'd like to not protect against CSRF with Django's built in mechanisms, use the csrf_exempt decorator:

``` python views.py
from django.views.decorators.csrf import csrf_exempt 
... 
@csrf_exempt 
def my_func(request):
    ...
```
