import graphene
from graphene_django.types import DjangoObjectType
from .models import Room, Message

class RoomType(DjangoObjectType):
    class Meta:
        model = Room

class MessageType(DjangoObjectType):
    class Meta:
        model = Message

class Query(graphene.ObjectType):
    all_rooms = graphene.List(RoomType)
    messages_by_room = graphene.List(MessageType, room_id=graphene.Int())

    def resolve_all_rooms(self, info):
        return Room.objects.all()

    def resolve_messages_by_room(self, info, room_id):
        return Message.objects.filter(room__id=room_id)

schema = graphene.Schema(query=Query)