from flask import Flask, request,render_template,redirect,url_for,flash,get_flashed_messages,Blueprint

web_i = Blueprint("web_i", __name__)



@web_i.route("/")
def redirect1():
    return redirect("/login")

@web_i.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        
        if username == "admin" and password == "1234":
            return 
        else:
            return("Invalid creds")
    


if __name__=="__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    web_i.run(host="0.0.0.0", debug=True,port=port)