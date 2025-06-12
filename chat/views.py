from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Message, Room
from .serializers import RoomSerializer, MessageSerializer

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
    
class RoomListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageListView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(room__id=room_id)

class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer