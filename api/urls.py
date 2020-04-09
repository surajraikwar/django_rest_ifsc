from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView, ListView, AboutView

urlpatterns = {
    url(r'^(?P<ifsc>[A-Za-z]{4}\w{7})$', DetailView.as_view()),
    url(r'^(?P<city>.*)/(?P<bank>.*)$', ListView.as_view()),
    url(r'^$', AboutView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
