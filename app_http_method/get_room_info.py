# -*- coding:UTF-8 -*-

from app_db.models import RoomInfo
from django.core.exceptions import ObjectDoesNotExist

def get(r_id):
    try:
        r = RoomInfo.objects.get(room_id=r_id)
        data = {'room_id':r.room_id,
                'room_name':r.room_name}
    except ObjectDoesNotExist:
        data = {'room_id':-1}


    return data