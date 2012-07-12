# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    '''hello = ''
    for post in post_list:
         hello = hello + post.title + ' , '
    
    print type(post_list)
    print post_list'''
    t = loader.get_template('blog/post_list.html')
    c = Context ({'post_list': post_list})
    return HttpResponse(t.render(c))

def post_detail(request, id, showComments=False):
    p=Post.objects.get(pk=id)
    '''q=p.body
    hk=p.comment_set.all()
    pana = ''
    for comment in hk:
        pana = pana + comment.author + ':'+ comment.body'''
    t = loader.get_template('blog/post_detail.html')
    c = Context({'postbyid':p})
    return HttpResponse(t.render(c))
    
    
def post_search(request, term):
    list_of_post=Post.objects.filter(body__icontains=term)
    '''ana =''
    for i in list_of_post:
        ana = ana+i.title+ ':'+ i.body+ ' , '''
    t = loader.get_template('blog/post_search.html')
    c = Context({'postbysearch':list_of_post})   
    return HttpResponse(t.render(c)) 
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
