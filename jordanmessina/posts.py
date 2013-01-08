import os
import datetime
from jordanmessina.filehelpers import path, ROOT

def get_posts():
    posts = []
    for post in os.listdir(path(ROOT, '../posts/')):
        post_dict = {'meta': {}}
        post_content = open(path(ROOT, '../posts/', post)).read()
        if post_content.index('---') == 0:
            meta = post_content[3:post_content[1:].index('---')]
            for meta_attr in meta.split('\n')[1:]:
                meta_attr = meta_attr.split(':')
                post_dict['meta'][meta_attr[0]] = meta_attr[1].strip()
            post_dict['post'] = post_content[post_content[1:].index('---')+4:]
            if 'date' in post_dict['meta']:
                post_dict['meta']['date'] = datetime.datetime.strptime(post_dict['meta']['date'], "'%Y-%m-%d'")
                post_dict['meta']['url'] = '/' + post_dict['meta']['date'].strftime('%Y/%m/%d') + '/' + post_dict['meta']['slug']
            else:
                post_dict['url'] = '/' + post['meta']['slug']
        else:
            post_dict['post'] = post_content
        posts.append(post_dict)
    return sorted(posts, key=lambda x: x['meta']['date'], reverse=True)
