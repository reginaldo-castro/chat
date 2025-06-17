from django.urls import path

from .views import RoomListView, MessageListView, MessageCreateView, index, room, sign_in, sign_out, auth_receiver, dashboard
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from chat.schema import schema


urlpatterns = [
    #path('', index, name='index'),
    #path('<str:room_name>/', room, name='room'),
    path('api/rooms', RoomListView.as_view(), name='api_rooms'),
    path('api/rooms/<int:room_id>/messages/', MessageListView.as_view(), name='api_room_messages'),
    path('api/messages/new/', MessageCreateView.as_view(), name='api_create_message'),
    path('', sign_in, name='sign_in'),
    path('sign-out', sign_out, name='sign_out'),
    path('auth-receiver', auth_receiver, name='auth_receiver'),
    path('dashboard/', dashboard, name='dashboard'),
]

urlpatterns += [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]