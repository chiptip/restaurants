from django.shortcuts import render
from django.views.generic import TemplateView
from restaurants.settings import ORDRIN_MODE, ORDRIN_SECRET

import ordrin

# Create your views here.


class MenuView(TemplateView):
	template_name = "menu.html"

	def mode(self):
		'''
			default to use test instance
		'''
		if ORDRIN_MODE == 'prod':
			return ordrin.PRODUCTION 
		return ordrin.TEST

	def lookup_menu(self):
		# -- Init api connection
		
		ordrin_api = ordrin.APIs(ORDRIN_SECRET, self.mode())
		# -- Rhong Tiam = 25940		
		RID = '25940'
		details = ordrin_api.restaurant_details(RID)

		menu = details['menu']
		return menu
		
	def get(self, request, *args, **kwargs):
		menu = self.lookup_menu()
		return render(request, self.template_name, {'menu': menu})
