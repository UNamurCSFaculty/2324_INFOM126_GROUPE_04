from django.apps import AppConfig
from django.shortcuts import render, redirect

class GuestbookConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'guestbook'
