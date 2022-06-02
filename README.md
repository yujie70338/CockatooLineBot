# yujie70338-CockatooLineBot 
利用 Flask、Heroku、LineDEV 建立的聊天機器人  
### Heroku 要求的三個文件:
* Procfile
  * 告訴Heroku如何執行架設我們的伺服器
  * 利用 gunicorn 當WSGI sever(Web Server Gateway Interface)
  * 要執行的app叫做app.py
* requirements.txt
  * app.py所需的套件
* runtime.txt
  * 提供程式語言和版本  

#PS Heroku 免費版本，在一段時間沒用時會休眠，下次使用要等約15秒重啟伺服器，所以第一次使用聊天機器人回覆訊習會比較久

