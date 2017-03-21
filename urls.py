from rest_framework import routers

urlpatterns = [
    url(r'^share-redirect-url/(?P<slug>[-\w]+)/$', SocialShare.as_view(), name='rich_share_redirect'),
]
