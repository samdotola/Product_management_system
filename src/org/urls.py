from django.urls import path
from org.views import (
	create_org_view,
	detail_org_view,
	edit_org_view,
)

app_name = 'org'

urlpatterns = [
    path('create/', create_org_view, name="create"),
    path('<slug>/', detail_org_view, name="detail"),
    path('<slug>/edit/', edit_org_view, name="edit"),
 ]