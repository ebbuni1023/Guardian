from flask import Flask, render_template, url_for, request, redirect
# import facerec
import keyboard_settings_fam
import keyboard_settings_nur
import facerec


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="GUARDIAN")

#@app.route("/docs/<lol>")
# def docs(lol):
    

@app.route("/about")
def about():
    return render_template("about.html", title="about page")

@app.route("/nurse")
def nurse():
    if request.method == "POST":
        print(request.get_data)
        stuff = request.get_data()
        keyboard_settings_nur.rewrite(stuff)
    return render_template("nurse.html", title="about page")

@app.route("/settings", methods=["POST", "GET"])
def family():
    if request.method == "POST": 
        # stuff = request.form['Field1_name']
        print(request.get_data())
        stuff = request.get_data()
        keyboard_settings_fam.rewrite(stuff)
    return render_template("settings.html", title="settings")

if __name__ == "__main__":
    app.run(debug=True)
