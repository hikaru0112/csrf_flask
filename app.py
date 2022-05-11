from tokenize import Number
from flask import Flask, render_template, session, request,jsonify,redirect
import os
from flask_cors import CORS
import MySQLdb
from datetime import timedelta



app = Flask(__name__)
CORS(
    app,
    supports_credentials=True,
)


app.config.update(
    #Laxを指定すると同一オリジンでしかcookieにアクセスできなくなる
    #Noneを指定すると一部ブラウザがセッションを保持しなくなる
    #SESSION_COOKIE_SAMESITE='',
)
# セッション
app.secret_key =  "SEC_KEY"
# セッションの持続時間
app.permanent_session_lifetime = timedelta(minutes=15)



@app.route("/")
def index():
    return render_template('index.html')

#ログインは既存ユーザーがいる場合はアカウント作成、パスワードとメールアドレスが一致すればログイン処理となる
@app.route("/payment", methods=["POST"])
def payment():
   mail = request.form.get('mail')
   pw = request.form.get('pass')
   conn = connect()
   cur = conn.cursor()
   sql = 'select user_id from users where mail = %s and password = %s'
   cur.execute(sql, (mail,pw,))
   user_id = cur.fetchone()
   cur.close()
   cur = conn.cursor()
   print(user_id)
   if not user_id:
         sql = "INSERT INTO users(mail, password) VALUES(%s, %s)"
         cur.execute(sql, (mail,pw))
         cur.close()
         cur = conn.cursor()
         sql = 'select user_id from users where mail = %s and password = %s'
         cur.execute(sql, (mail,pw,))
         user_id = cur.fetchone()
         print("ssss")
         print(user_id)
         cur.close()
         cur = conn.cursor()
         sql = "INSERT INTO money(user_id) VALUES(%s)"
         cur.execute(sql, (user_id))
         cur.close()
         cur = conn.cursor()
   

   
   sql =  'select money from money where user_id = %s'
   cur.execute(sql, (user_id))
   money = cur.fetchone()        
   session['user'] = user_id
   cur.close()
   conn.commit()
   conn.close()
   
   return render_template('pay.html',money=money[0],mail=mail)


#攻撃先ルート
@app.route("/transfer", methods=["POST"])
def transfer():
   if not session:
      return redirect('/')
   pay = request.form.get('pay')
   if(str(pay).isdigit):
      conn = connect()
      cur = conn.cursor()
      sql =  'select money from money where user_id = %s'
      cur.execute(sql,(session['user'][0],))
      money = cur.fetchone()
      cur.close()
      cur = conn.cursor()
      print(session['user'][0])
      sql = 'UPDATE money SET money = %s WHERE user_id = %s'
      cur.execute(sql, (int(pay) + int(money[0]),session['user'] ))
      cur.close()
      conn.commit()
      conn.close()
      return redirect("/payment")
   return 


@app.route("/payment")
def paymentnoP():
   if not session:
      return redirect('/')
   conn = connect()
   cur = conn.cursor()
   sql =  'select money from money where user_id = %s'
   cur.execute(sql, (session['user'] ))
   money = cur.fetchone()        
   session['user'] 
   cur.close()
   cur = conn.cursor()
   sql = 'select mail from users where user_id = %s'
   cur.execute(sql,(session['user'][0],))
   mail = cur.fetchone()
   conn.close()
   
   return render_template('pay.html',money=money[0],mail=mail[0])




def connect():
    pw = os.environ['DATABASE_PASS']
    return MySQLdb.connect(user='admin', passwd=pw, host='db', db='csrf',
                           charset="utf8")

