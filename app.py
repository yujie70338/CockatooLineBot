# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('Chennel access token')
# 聊天機器人的 Chennel access token
handler = WebhookHandler('Channel secret')
# 聊天機器人的 Channel secret

# 建立callback路由，檢查LineBot資訊是否正確
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 學你說話程式碼
@handler.add(MessageEvent, message=TextMessage) 
# 當收到LINE的MessageEvent(信息事件)，而且信息是屬於TextMessage，執行。
# LINE的事件有：MessageEvent(信息事件)、FollowEvent(加好友事件)、UnfollowEvent(刪好友事件)、JoinEvent(加入聊天室事件)、LeaveEvent(離開聊天室事件)、MemberJoinedEvent(加入群組事件)、MemberLeftEvent(離開群組事件)

def echo(event): # echo函數會接收一個LINE發送過來的資訊，並貼上event的標籤。
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef": # 如果是Line官方傳的測試訊息，就不回應
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )
        # reply_message方法為回傳訊息給使用者，push_message為主動推播訊息給使用者
        # 可以回傳的種類有Text, Image, Video, Audio, Location, Sticker, Template等等

if __name__ == "__main__":
    app.run()
