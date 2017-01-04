#!flask/bin/python
from flask import Flask, jsonify, request, Response
import psycopg2
import sys
import json
db_conn = None

app = Flask(__name__)

@app.route('/api/registration/signup', methods=['GET','POST'])
def insert_data():
     #if request.headers['Content-Type']=='application/json':
     #    return json.dumps(request.get_json(request.json))
     #jsonUserData = request.get_json()
     #resp = Response(response=jsonUserData)
     try:
         db_conn = psycopg2.connect(database='postgres', user='postgres', password='password', host='localhost',
                                    port='5432')
         cursor = db_conn.cursor()
         # cursor.execute("Insert INTO tbl_farmers (name, mobile, password, state, district, tehsile, village, pin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"("",))
         # ver = cursor.fetchone()
         # print(ver)
     except psycopg2.DatabaseError as e:
         print('Error %s' % e)
         sys.exit(1)
     finally:
         if db_conn:
             db_conn.close();
     #return(resp)
     return json.dumps(request.get_json(json))

if __name__ == '__main__':
    app.run(debug=True)