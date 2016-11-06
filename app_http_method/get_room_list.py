# -*- coding:UTF-8 -*-
from app_db.models import RoomInfo

def get():
    #返回的是一个QuerySet
    rooms = RoomInfo.objects.all().values_list('room_id', 'room_name')
    message = []
    for r in rooms:
        message.append({'id':r[0],'name':r[1]})

    return message