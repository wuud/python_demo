# -- coding: utf-8 --
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def signin_form():
    return '''<div style="text-align:center">
              <form action="/signin" method="post">
              <p>账号：<input name="username"></p>
              <p>密码：<input name="password" type="password"></p>
              <hr>
              <p><button type="submit">Sign In</button></p>    
              </form>
              </div>'''

@app.route('/', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()