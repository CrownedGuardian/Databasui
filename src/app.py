"""import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="iliketurtles",
                     db="pythonspot")

cur = db.cursor()

cur.execute("SELECT * FROM examples")

for row in cur.fetchall():
    print row[0], " ", row[1]

db.close()"""

import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    if request.path != '/':
        if request.headers['content-type'].find('application/json'):
            return 'Unsupported Media Type', 415

@app.route('/')
def index():
    data = {"firstName":"Stephen", "lastName":"Negron"}
    return render_template("index.html", fullName = data)

@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')}
    return jsonify(ret_data)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    #your code
    return render_template("index.html", dat = projectpath)
 
if __name__ == '__main__':
    app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    