from django import forms

from org.models import Product 


class CreateBlogPostForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['title', 'description', 'price', 'image']


class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['title', 'description', 'price', 'image']

	def save(self, commit=True):
		org_post = self.instance
		org_post.title = self.cleaned_data['title']
		org_post.description = self.cleaned_data['description']
		org_post.price = self.cleaned_data['price']
		
        
		if self.cleaned_data['image']:
			org_post.image = self.cleaned_data['image']

		if commit:
			org_post.save()
		return org_post