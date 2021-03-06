from django.shortcuts import redirect
from ..views.common import *
import json

class User_middleware(object):
	"""Checks if the user is allowed to access the page they are requesting."""

	def process_request(self, request):
		"""The main part of the middleware, called each time a user makes a request."""
		# Initialization.
		url = request.path
		urls = url.replace("//", "/").split("/")
		first_url = urls[1]

		not_required_session = [
			"register",
			"login",
			"logout",
		]

		no_action = [
			"logout",
			"",
			"/",
		]

		return True


