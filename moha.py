import werobot
import os
from util import Tuling, MohaAnswer

token=os.environ.get('WXTOKEN')
tuling_key = os.environ.get('TULINGKEY')

if token is None:
    raise Exception("token should be set as environment variable")
robot = werobot.WeRoBot(token=token)
robot.config['HOST'] = '0.0.0.0'
# 默认80端口，如果采用端口转发，可以设置其他端口
robot_port = os.environ.get('ROBOTPORT')
robot.config['PORT'] = robot_port or 80
tuling = Tuling(tuling_key)

@robot.text
def reply(msg, session):
    content = msg.content
    moha = MohaAnswer("./answer_data.csv")
    answer = moha.answer(content)
    if answer is None:
        answer = tuling.response(content)
    return answer

@robot.subscribe
def subscribe(msg):
    return '吼啊，又加了1s，请先念一句诗~'

robot.run()
