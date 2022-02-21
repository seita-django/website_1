from django.conf.urls import url
from homepage import views

# TEMPLATE TAGGING
app_name = "homepage"
urlpatterns = [
    # url(r'^$', views.IndexViews.as_view(), name='index'), # not use CBV this time
    url(r'^$', views.index, name='index'),
    url(r'^complete/$', views.complete, name='complete'),  # Contact_result page
    url(r'^QandA/$', views.QandA, name='QandA'), # Q and A page
]



