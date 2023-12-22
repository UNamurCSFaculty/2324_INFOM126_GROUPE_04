from django import forms
from .models import GuestbookEntry

class GuestbookEntryForm(forms.ModelForm):
	"""Form for adding a new guestbook entry"""
	class Meta:
		"""Meta class to map model's fields to form fields"""
		model = GuestbookEntry
		fields = ['name', 'message']
		