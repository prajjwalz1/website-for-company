from django.contrib import admin
from django.shortcuts import render
from .models import portfolio,board_members,timeline,background,client,services

# Register your models here.
admin.site.register(portfolio)
admin.site.register(board_members)
admin.site.register(timeline)
admin.site.register(background)
admin.site.register(client)
admin.site.register(services)