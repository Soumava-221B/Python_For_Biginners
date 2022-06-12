#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:03:49 2022

@author: soumava
"""

''' Intiliaze the dict with [] for each user id: '''
users = [ {"id":0, "name":"Hero"}, {"id":1,
"name":"Dunn"}, {"id":2, "name":"Sue"}, {"id":3,
"name":"Chi"}, {"id":4, "name":"Thor"}, {"id":5,
"name":"Clive"}, {"id":6, "name":"Hicks"},
{"id":7, "name":"Devin"}, {"id":8, "name":"Kate"},
{"id":9, "name":"Klein"} ]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1,3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
friendships = {user["id"]: [] for user in users}
''' And loop over friendship to populate it: '''
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
    
def no_of_friends (user):
    ''' How many does the user have? '''
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
    