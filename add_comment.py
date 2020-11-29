import requests
import json
import jsonpath
import edit_card
from delete_card import vKey, vToken


def addComment(aCardId):

    print('************* 5TH STEP: ADD A COMMENT TO ONE OF THE CARDS *************')
    url = "https://api.trello.com/1/cards/" + aCardId + "/actions/comments"
    vComment = 'Comment was added'
    query = {
    'key': vKey,
    'token': vToken,
    'text': vComment,
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )

    print("This is response status code: " + str(response.status_code))
    assert response.status_code == 200
    print("This is respone boolean status: " + str(response.ok))
    assert response.ok == True
    json_response = json.loads(response.content)
    comment = (json_response.get('display').get('entities').get('comment').get('text'))
    print ("This is added comment: " + comment)
    assert comment == vComment

commit1

1
2
3
4
5
6
7
8
9
10
11