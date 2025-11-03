from flask import Flask, render_template, request

#WSGI Application
app=Flask(__name__) #instance of Flask

#all routes by default are GET

@app.route("/")
def welcome():
    return "<html> <h1>Welcome to the flask app</h1> </html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/submit",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello, {name}!"
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True) #params=> debug, port etc, debug=True(like nodemon)