from flask import Flask, render_template, redirect, request, session 
#from mysqlconnection import connectMySQL
app = Flask(__name__)
#bycrypt = bycrypt(app) 
app.secret_key = "keep it secret, keep it safe"

user = {
    "username":"kevinolson07" }
# print(user['username'])

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        print("you are in the index function!!!", flush=True)
        print(user["username"], flush=True)
        userN = request.form["username"]
        print(userN, flush=True)
        if userN == user["username"]:
            return render_template('home.html')
        else:
            return redirect("/")
    # uname = request.form["uname"]
    # if(uname== user["username"]):
    #     print("you are in the home function!!!")
    #     return render_template("home.html", data=30)
    else:
        return render_template("index.html")

@app.route('/registration')
def registration():
    print("you are in the registation function!!!", flush=True)
    return render_template("registration.html")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8090)
   

