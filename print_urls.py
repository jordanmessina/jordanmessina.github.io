from django.conf import settings

print '/'
for page in settings.PAGES:
    print page
for post in settings.POSTS:
    print post['meta']['url']
