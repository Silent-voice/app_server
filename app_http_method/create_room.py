# -*- coding:UTF-8 -*-
# 创建一个新房间，并为房主创建玩家信息

from app_db.models import RoomInfo
from app_db.models import UserInfo
from django.core.exceptions import ObjectDoesNotExist
import app_websocket_method.glob

def create(user_id,r_name):
    # 获取一个未使用的房间号
    mark = False
    room_id = 0
    for i in range(len(app_websocket_method.glob.room_id)):
        if app_websocket_method.glob.room_id[i] == 0:
            room_id = i
            mark = True
            break
    if mark == False:
        room_id = len(app_websocket_method.glob.room_id)
        app_websocket_method.glob.room_id.append(1)



    # 操作数据库

    user = UserInfo.objects.get(id = user_id)

    newRoom = RoomInfo(room_id=room_id,room_name=r_name,owner_id=user_id,player_num=1,
                       player_id=str(user_id),player_nick=user.nick_name,player_role="village",player_alive="true")
    newRoom.save()

    #newPlayer = PlayerInfo(name=user_name,room_id=room_id,alive=True)
    #newPlayer.save()


    # glob添加新对象
    app_websocket_method.glob.room_request_id[room_id] = 0
    #glob.room_player_num[room_id] = player_num
    app_websocket_method.glob.room_mark[room_id] = {user_id:0}

    return room_id