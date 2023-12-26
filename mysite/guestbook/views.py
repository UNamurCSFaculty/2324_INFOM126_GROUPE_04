"""Views for the guestbook app."""
from django.shortcuts import redirect, render
from .forms import GuestbookEntryForm
from .models import GuestbookEntry

def guestbook(request):
	"""View function for home page of site."""
	if request.method == 'POST':
		form = GuestbookEntryForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('guestbook')
	else:
		form = GuestbookEntryForm()
	entries = GuestbookEntry.objects.all().order_by('-date_posted')
	return render(request, 'index.html', {'form': form, 'entries': entries})


# Create your views here.
