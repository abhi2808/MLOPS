from flask import Flask

#WSGI Application
app=Flask(__name__) #instance of Flask

@app.route("/")
def welcome():
    return "Welcome to Flask Application..."

if __name__=="__main__":
    app.run(debug=True) #params=> debug, port etc, debug=True(like nodemon)