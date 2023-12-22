from django.shortcuts import render
from .forms import GuestbookEntryForm
from .models import GuestbookEntry

def guestbook(request):
	if request.method == 'POST':
		form = GuestbookEntryForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = GuestbookEntryForm()
	entries = GuestbookEntry.objects.all().order_by('-date_posted')
	print(entries)
	return render(request, 'index.html', {'form': form, 'entries': entries})


# Create your views here.
