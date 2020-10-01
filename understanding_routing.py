from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def dojo():
    return "Dojo"
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    return "Hi " + name
@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return int(num)*word
# @app.errorhandler(404)
# def error(e):
#     return "Sorry! No repsonse. Try Again"
@app.route('/<this>')
def anything(this):
    return "Sorry! No response. Try again."
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
