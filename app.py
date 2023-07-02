# flask is a module (always lowercase)
# Flask is a class inside the module
from flask import Flask, render_template
# app is an object of the class Flask (creates a flask application and assigning it to app)
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Job one',
    'location': 'Remote',
    'salary': '$10'
  },
  {
    'id': 2,
    'title': 'Job two',
    'location': 'Remote',
    'salary': '$10'
  },
  {
    'id': 1,
    'title': 'Job three',
    'location': 'Remote',
    'salary': '$10'
  }
]

# register a route to application (/ is homepage)
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS, company_name='AMS Corp. ') 

# we've defined a function that returns hello world, but by adding the decorator (@) when the url / is accessed it
# shows the return from the function


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)