from time import sleep
from random import randint
from vk_api import VkApi
from config import ACCESS_TOKEN, POST_ID, TEXT, MSG_TEXT, TRIGGER

vk_session = VkApi(token=ACCESS_TOKEN)

vk = vk_session.get_api()


def post():
    vk.wall.post(message=TEXT)


def pin():
    vk.wall.pin(post_id=POST_ID)


def main():
    offset_сount = vk.wall.getComments(post_id=POST_ID)['count']
    while True:
        sleep(3)
        comments = vk.wall.getComments(offset=offset_сount,post_id=POST_ID)
        count = comments["count"]
        if count > offset_сount:
            for comment in comments['items']:
                text = comment["text"]
                print(text)
                if text.lower() == TRIGGER:
                    user_id = comment['from_id']
                    user = vk.users.get(user_ids=user_id, fields ="first_name")[0]
                    username = user['first_name']         
                    comment_id= comment['id']
                    msg = f"{username}, {MSG_TEXT}"
                    try:
                        vk.messages.send(user_id=user_id, random_id = randint(1, 1000), message=msg)
                    except:
                        vk.wall.createComment(post_id=POST_ID, message=msg,reply_to_comment=comment_id)
            offset_сount = offset_сount+count
        elif count < offset_сount:
            offset_сount = count
 
if __name__ == "__main__":
    # post()
    main()
    # pin()
