from django.apps import AppConfig
from django.shortcuts import render, redirect
from .forms import GuestForm
from .models import GuestEntry


class AppLivreOrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_livre_or'

	
def guest_book(request):
	if request.method == 'POST':
		form = GuestForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('guest_book')
	else:
		form = GuestForm()
	
	entries = GuestEntry.objects.all()
	context = {'form': form, 'entries': entries}
	return render(request, 'guest_book.html', context)
