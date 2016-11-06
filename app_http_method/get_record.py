# -*- coding:UTF-8 -*-
from app_db.models import standings


#返回数据  [{'win':win,'lose':lose},{'role':role,'result':result,'other_person':{....}},{},...]

def get(u_id):
    records = standings.objects.filter(user_id = u_id)
    win_time = 0
    lose_time = 0

    roles = []
    results = []
    other_persons = []

    for i in records:
        roles.append(i.role)
        results.append(i.result)
        other_persons.append(i.other_person)
        if i.result == True:
            win_time = win_time + 1
        else:
            lose_time = lose_time + 1

    message = []
    temp = {'win':win_time,'lose':lose_time}
    message.append(temp)
    for i in range(len(roles)):
        message.append({'role':roles[i],'result':results[i],'other_person':other_persons[i]})

    return message