import datetime

from django.conf import settings

import PyRSS2Gen

import markdown

rss = PyRSS2Gen.RSS2(
    title = "Jordan Has a Blog",
    link = "http://jordanmessina.com",
    description = "Jordan Messina's Blog",

    lastBuildDate = datetime.datetime.now(),

    items = [
       PyRSS2Gen.RSSItem(
         title = post['meta']['title'],
         link = "http://jordanmessina.com{post_url}".format(post_url=post['meta']['url']),
         description = markdown.markdown(post['post'].decode('UTF-8')),
         guid = PyRSS2Gen.Guid("http://jordanmessina.com{post_url}".format(post_url=post['meta']['url'])),
         pubDate = post['meta']['date'])
    for post in settings.POSTS]
)

rss.write_xml(open("feed.xml", "w"))
