from django.urls import path

from .views import RoomListView, MessageListView, MessageCreateView, index, room
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from chat.schema import schema

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
    path('api/rooms', RoomListView.as_view(), name='api_rooms'),
    path('api/rooms/<int:room_id>/messages/', MessageListView.as_view(), name='api_room_messages'),
    path('api/messages/new/', MessageCreateView.as_view(), name='api_create_message'),
]