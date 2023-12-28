from django.shortcuts import render
from home.models import Account
from org.models import Product
# Create your views here.
def home_view(request):
    context={}
    accounts = Account.objects.all()
    context['accounts']=accounts

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    
    if request.user.is_authenticated:
        blog_posts = Product.objects.filter(author=request.user)
        context['blog_posts'] = blog_posts
    else:
        context['blog_posts'] = []
    return render(request, 'base.html', context)