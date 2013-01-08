from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import Http404

def load_post(request, path):
    try:
        post = filter(lambda x: x['meta']['url'][1:] == path, settings.POSTS)[0]
        return render_to_response('post.html', {'post': post, }, context_instance=RequestContext(request))
    except IndexError, e:
        raise Http404

def archives(request):
    return render_to_response('archives.html', {'posts': settings.POSTS, }, context_instance=RequestContext(request))

def index(request):
    post = settings.POSTS[0]
    return render_to_response('index.html', {'post': post, }, context_instance=RequestContext(request))

