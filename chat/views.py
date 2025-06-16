from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Message, Room
from .serializers import RoomSerializer, MessageSerializer
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import HttpResponse
import os
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chat/index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
    
@cache_page(60 * 15)
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})

class RoomListView(APIView):
    permission_class = [IsAuthenticated, TokenHasReadWriteScope]
    
    def get(self, request):
        rooms = Room.objects.all()
        data = RoomSerializer(rooms, many=True).data
        return Response(data)

class MessageListView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(room__id=room_id)

class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer
    
@csrf_exempt
def sign_in(request):
    return render(request, 'login.html')

@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)

    # In a real app, I'd also save any new user here to the database.
    # You could also authenticate the user here using the details from Google (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
    request.session['user_data'] = user_data

    return redirect('sign_in')

def sign_out(request):
    del request.session['user_data']
    return redirect('sign_in')