import requests
import json
import jsonpath
import get_id_list
from delete_card import vKey, vToken


def createBoard():

   url = "https://api.trello.com/1/boards/"
   query = {
      'key': vKey,
      'token': vToken,
      'name': 'FirstBoard',
      'defaultLabels': 'false',
      'defaultLists': 'true',
      'desc': 'Description for the board',
      'prefs_permissionLevel': 'public',
      'prefs_voting': 'members',
      'prefs_comments': 'public',
      'prefs_invitations': 'members',
      'prefs_selfJoin': 'true',
      'prefs_cardCovers': 'true',
      'prefs_background': 'orange',
      'prefs_cardAging': 'regular'
   }
   response = requests.request(
      "POST",
      url,
      params=query
   )
   
   print('************* 1ST STEP: CREATE A BOARD *************')
   print("This is response status code: " + str(response.status_code))
   assert response.status_code == 200
   print("This is respone boolean status: " + str(response.ok))
   assert response.ok == True
   json_response = json.loads(response.text)
   name = ''.join(jsonpath.jsonpath(json_response, 'name'))
   print("This is board name: " + name)
   assert name == 'FirstBoard'
   description = ''.join(jsonpath.jsonpath(json_response, 'desc'))
   print ("This is board description: " + description)
   assert description == 'Description for the board'
   print ("This is 'idBoard': " + ''.join(jsonpath.jsonpath(json_response, 'id')))
   boardId = ''.join(jsonpath.jsonpath(json_response, 'id'))

   #GET LIST ID
   get_id_list.getIdList(boardId)

   return boardId
   
#CREATE BOARD
createBoard()

