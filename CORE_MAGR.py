import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

random_id = random.getrandbits(64)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.getrandbits(64)})


token = "3e74622d620b002171c24dbbcbe1f40d97df3b45b1ff128e358b24223202f6b728e322aa03b0778a74ae3"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            GHK = open("BASE_NKL.txt", 'a', encoding='utf-8')
            request = event.text
            GHK.write(str(event.user_id))
            GHK.write(":")
            GHK.write(str(event.text))
            GHK.write('\n')
            GHK.close()
            print(str(event.user_id))
            print(str(event.text))
            print('\n')

            if request == "1":
                write_msg(event.user_id,
                          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ \nМихаил Варкулевич является основоположником канала и данной группы. Он проходит интересные игры и показывает их прохождение своим зрителям\n≈≈≈≈≈≈≈≈≈ВОПРОСЫ≈≈≈≈≈≈≈≈≈≈\n1 - Кто создатель канала MAGR/этой группы?\n 2 - Что канал/группа может мне предложить?\n 3 - Кто тебя создал?\n 4 - Кто я?\n")

            elif request == "2":
                write_msg(event.user_id,
                          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\nДанная группа, как и канал MAGR, может вам предложить прохождение игр и веселое настроение\n≈≈≈≈≈≈≈≈≈ВОПРОСЫ≈≈≈≈≈≈≈≈≈≈\n1 - Кто создатель канала MAGR/этой группы?\n 2 - Что канал/группа может мне предложить?\n 3 - Кто тебя создал?\n 4 - Кто я?\n")

            elif request == "3":
                write_msg(event.user_id,
                          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\nКоманда \"БИЗЗАРНЫЕ НИББЫ\"\n ≈≈≈≈≈≈≈≈≈ВОПРОСЫ≈≈≈≈≈≈≈≈≈≈\n1 - Кто создатель канала MAGR/этой группы?\n 2 - Что канал/группа может мне предложить?\n 3 - Кто тебя создал?\n 4 - Кто я?\n")

            elif request == "4":
                write_msg(event.user_id,
                          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\nНадеюсь, что подписчик этой группы или канала MAGR. Михаил выпускает отличный контент, не подведем же его, друзья!\n≈≈≈≈≈≈≈≈≈ВОПРОСЫ≈≈≈≈≈≈≈≈≈≈\n1 - Кто создатель канала MAGR/этой группы?\n 2 - Что канал/группа может мне предложить?\n 3 - Кто тебя создал?\n 4 - Кто я?\n")

            else:
                write_msg(event.user_id,
                          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\nПожалуйста, попробуйте еще раз!\n≈≈≈≈≈≈≈≈≈ВОПРОСЫ≈≈≈≈≈≈≈≈≈≈\n1 - Кто создатель канала MAGR/этой группы?\n 2 - Что канал/группа может мне предложить?\n 3 - Кто тебя создал?\n 4 - Кто я?\n")