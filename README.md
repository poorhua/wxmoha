# wxmoha
微信公众平台帐号mycrouchred(如果闷声发大财不被发现的话)  
这是一个自动回复的公众号，大致上会回复一些蛤蛤的语录。 
![qr_mycrouchred](https://github.com/crouchred/wxmoha/raw/master/assets/qr_mycrouchred.jpg)

### 蛤蛤语录(欢迎各界人士补充)
[answer_data.csv](https://github.com/crouchred/wxmoha/blob/master/answer_data.csv)  

以下面这句为例：

```
支持,当然啦|无可奉告 
```

即：如果用户输入的句子中包含"支持"，那么结果可能为"当然啦"或者"无可奉告"

### 配置
需要在bash中输入如下命令，建议使用[autoenv](https://github.com/kennethreitz/autoenv)进行环境变量设置  

1. export WXTOKEN="你的微信token" (必须)(您需要去[微信公众平台](https://mp.weixin.qq.com)申请自己的公众号)  
2. export TULINGKEY="你的图灵key" (可选)(您可以去[图灵机器人](http://www.tuling123.com)申请一枚图灵key)  

### 运行
python3 moha.py

### 特点
1. 开发框架使用WeRoBot
2. 对于输入的语句采用结巴分词进行分词处理
3. 采用类似搜索引擎的倒排索引进行匹配
4. 维护一个csv的蛤蛤语料库([answer_data.csv](https://github.com/crouchred/wxmoha/blob/master/answer_data.csv))
5. 如果没有匹配上蛤蛤语录，会调用图灵的接口，还蛮有趣的。。

### 其他资料
其他技术细节和踩过的坑，可以参见我的blog(其实还没写好。。)
