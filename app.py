# flask is a module (always lowercase)
# Flask is a class inside the module
from flask import Flask
# app is an object of the class Flask (creates a flask application and assigning it to app)
app = Flask(__name__)

# register a route to application (/ is homepage)
@app.route("/")
def hello_wold():
  return "Hello, Andrew!"

# we've defined a function that returns hello world, but by adding the decorator (@) when the url / is accessed it
# shows the return from the function


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)