from django.shortcuts import render
from .models import portfolio,board_members,timeline,background,client,services
# Create your views here.
from django.urls import path
from.import views

def index (request):
    portfolios=portfolio.objects.all()
    team = board_members.objects.all()
    obj = timeline.objects.all()
    bg=background.objects.all()
    clients=client.objects.all()
    service=services.objects.all()
    return render(request,'index.html',{'portfolio':portfolios,'team_members':team,'timeline':obj,'bg_img':bg,'clients':clients,'service':service})
