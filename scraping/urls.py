from django.conf.urls import patterns
from django.views.generic import TemplateView
from .views import StartView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoScraper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	(r'^start/$', StartView.as_view()),
	(r'^success/$', TemplateView.as_view(template_name="success.html"))
)