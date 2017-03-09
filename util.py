import requests
import json
import random
import jieba
import collections
import operator

class Tuling:

    url = "http://www.tuling123.com/openapi/api"

    def __init__(self, key=None):
        self.key = key 

    def response(self, msg):
        payload = {'key':self.key, 'info':msg}
        r = requests.post(self.url, data=payload)
        result = json.loads(r.text)
        code = result['code']
        if code == 100000:
            answer = result['text']
        else:
            print("tuling wrong code: "+ str(code))
            answer = self._response_fallback
        return answer

    @property
    def _response_fallback(self):
        return random.choice((
            "在下是机器人，不是很理解啊",
            "窝是机器人，窝不懂啊",
            ))

class MohaAnswer:

    def __init__(self, filename):
        self.filename = filename

    @property
    def answer_dict(self):
        result = {}
        with open(self.filename) as f:
            lines = f.readlines()
        for line in lines:
            key = line.split(',', 1)[0]
            value = line.split(',', 1)[1]
            result[key] = value.strip('\n').split('|')
        return result

    def answer(self, msg):
        return_dict = collections.defaultdict(lambda: random.random()) # return the different value if input a short sentence
        answer_dict = self.answer_dict
        for word in jieba.cut_for_search(msg):
            if word.strip() != "" and word in answer_dict:
                answer_words = answer_dict[word]
                for answer_word in answer_words:
                    return_dict[answer_word] += 1
        return_dict = sorted(return_dict.items(), key=operator.itemgetter(1), reverse=True)
        if len(return_dict) > 0:
            return return_dict[0][0]

