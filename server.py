from flask import Flask, render_template, redirect, request, session 
#from mysqlconnection import connectMySQL
app = Flask(__name__)
#bycrypt = bycrypt(app) 
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    print("you are in the index function!!!", flush=True)
    return render_template("index.html")

@app.route('/home')
def home():
    print("you are in the home function!!!")
    return render_template("home.html", data=30)



if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8090)
   

