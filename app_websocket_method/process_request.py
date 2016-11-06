# -*- coding:UTF-8 -*-
import demjson

import glob
import send_message


#   成功发送请求后 glob.room_request_id++
def process(message,data):

    type = data['type']
    room_id = data['room_id']
    user_name = data['user_name']

    message = {}
    #处理确认消息
    if type == 0:
        r_request_id = data['r_request_id']
        if r_request_id == glob.room_request_id:
            glob.room_mark[room_id][user_name] = 1
        return
    #非确认消息
    request_id = data['request_id']
    #判断该请求是否已被处理
    if request_id < glob.user_request_id['user_name']:
        # message['type'] = 1
        # message['user_name'] = user_name
        # json = demjson.encode(message)
        # send_message.send(room_id,json)
        return
    elif request_id > glob.user_request_id['user_name']:
        message['type'] = 2
        message['room_request_id'] = glob.room_request_id[room_id]
        message['user_name'] = user_name
        message['error_message'] = 'error in request_id'
        json = demjson.encode(message)
        send_message.send(room_id, json)
        return
    else:
        # if type == 1:
        #     #create_room.create()
        # elif type == 2:
        #     #join_room.join()
        # else:
        #     message['type'] = 2
        #     message['room_request_id'] = glob.room_request_id[room_id]
        #     message['user_name'] = user_name
        #     message['error_message'] = 'error in type'
        #     json = demjson.encode(message)
        #     send_message.send(room_id, json)



        return
