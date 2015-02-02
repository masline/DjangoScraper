from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django import forms
from .models import Data

# Create your views here.


class ScrapeForm(forms.Form):
	item = forms.CharField(max_length=50)
	manu = forms.CharField(max_length=50)


# Format taken from https://docs.djangoproject.com/en/1.7/topics/class-based-views/intro/#handling-forms-with-class-based-views
class StartView(View):
	form_class = ScrapeForm
	template_name = "scrape_form.html"

	# On a normal http request, the form will be passed to the template, "scrape_form.html", and the template will render the form
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {"form": self.form_class})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# Perform Kimono scraping here...either use a python based async action, or leave synchronous
			# if scraped well:
				# save to DB
			part = Data.objects.create(item=form.item, manu=form.manu)
				# redirect to an output page?
			# else:
				# redirect to an error page?
			return HttpResponseRedirect('/success/')

		# We've reached this line because the form above is *not* valid, so re-rendering the form will display the errors with it
		return render(request, self.template_name, {"form": form})