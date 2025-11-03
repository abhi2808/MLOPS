#building dynamic url
#variable rule
#jinja 2 template engine

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

## Variable rule
@app.route("/success/<int:score>") #by default value is string
def success(score):
    #return f"the marks obtained are {score}"

    res=""
    if score>50:
        res="pass"
    else:
        res="fail"
    return render_template("result.html",result=res)

"""
jinja2 template engine
{{}} expression to print variable
{% %} statements for control flow
{# #} comments
"""

## dynamic url-> create using url_for, use redirect to redirect to another route  

if __name__=="__main__":
    app.run(debug=True) #params=> debug, port etc, debug=True(like nodemon)