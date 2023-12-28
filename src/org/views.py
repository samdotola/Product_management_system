from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from org.models import Product
from org.forms import CreateBlogPostForm, UpdateBlogPostForm
from home.models import Account


def create_org_view(request):
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()

	context['form'] = form

	return render(request, "org/create_org.html", {})
    

	


def detail_org_view(request, slug):

	context = {}

	org_post = get_object_or_404(Product, slug=slug)
	context['org_post'] = org_post

	return render(request, 'org/detail_org.html', context)



def edit_org_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	org_post = get_object_or_404(Product, slug=slug)

	if org_post.author != user:
		return HttpResponse('You are not the author of that post.')

	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=org_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			org_post = obj

	form = UpdateOrgPostForm(
			initial = {
					"title": org_post.title,
					"description": org_post.description,
					"price": org_post.price,
					"image": org_post.image,
			}
		)

	context['form'] = form
	return render(request, 'org/edit_org.html', context)


def get_org_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = Product.objects.filter(
				Q(title__icontains=q) | 
				Q(description__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))