# My microservice!
import requests
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

# create Flask app
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

# GET request to ip.jsontest.com
def home():
    return render_template('home.html')

def rest_request_example():
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/0/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/1/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/2/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/3/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/4/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/5/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/6/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/7/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/8/pink/colinkobes").text)
    print (requests.get("http://140.86.15.104:3000/reactorCore/45/9/pink/colinkobes").text)


def read_db_SQL_example():
    conn = db.get_engine().connect()
    sql = "SELECT * FROM SecretTable"
    results = conn.execute(sql)
    rows = ""
    for row in results:
        rows = rows + ','.join(row) + "<br/>"
    print(rows)
	
rest_request_example()
try:
	read_db_SQL_example()
except:
	print ('Could not connect to database')
	
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
