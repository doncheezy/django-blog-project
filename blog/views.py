# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse('This should be a list of posts!')

def post_detail(request, id, showComments=False):
    p=Post.objects.get(pk=id)
    q=p.body
    html=''
    
    for i in p.comments.all():
        html+=str(i)
      
    return HttpResponse(str(p) + '<br/>' + str(q) +'<br/>' +html +'<br/>')
    
    
def post_search(request, term):
    return HttpResponse(term)
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
