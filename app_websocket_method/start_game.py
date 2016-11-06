# -*- coding:UTF-8 -*-
#开始游戏

import glob
import assign_role
import send_message
import demjson
from app_db.models import RoomInfo
from app_db.models import PlayerInfo
from app_db.models import UserInfo
from channels import Group
from channels.sessions import channel_session

import json


def start(room_id):

    temp = glob.room_mark[room_id]
    users = temp.keys()
    #分配角色
    assign_role.assign(room_id)

    #发送房间和用户信息
    r = RoomInfo.objects.get(r_id = room_id)
    #数据库对象不能直接解析成json
    data={'r_id':r.r_id,
          'owner':r.owner,
          'player_num':r.player_num
          }
    json = demjson.encode(data)
    send_message.send(room_id,json)

    user_info = []
    data={'name':'a',
          'room_id':0,
          'role':0,
          'alive':True}
    for i in users:
        u = PlayerInfo.objects.get(name = i)
        data['name']=u.name
        data['room_id'] = u.room_id
        #...
        user_info.append(data)

    json = demjson.encode(user_info)
    send_message.send(room_id, json)

    return