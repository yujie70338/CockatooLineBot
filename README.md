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
### app.py為主程式:
 * 我們網頁伺服器使用的method是POST，所以當推上Heroku時，用網頁瀏覽器無法打開Heroku提供的網址，但是可以利用LineDEV內的測試服務，檢查是否有建立成功，或是進Heroku的控制台內看log
 * L12、L14要填入從LineDEV得到的資料
 * L18~29確認LineBot的資訊
#PS Heroku 免費版本，在一段時間沒用時會休眠，下次使用要等約15秒重啟伺服器，所以第一次使用聊天機器人回覆訊習會比較久

