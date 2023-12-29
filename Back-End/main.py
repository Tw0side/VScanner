import flask
from flask import request, jsonify, render_template
import mysql.connector
import config

app = flask.Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True

def get_mysql_connection():
    return mysql.connector.connect(
        host=config.db_host,
        user=config.db_user,
        database=config.db_name,
        password=config.db_password
    )

def listapikeys():
    try:
        mydb = get_mysql_connection()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM apikeys")
        myresult = mycursor.fetchall()
        mycursor.close()
        apis = jsonify(myresult)
        return apis
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mydb.close()

def delete(api_key):
    try:
        mydb = get_mysql_connection()
        mycursor = mydb.cursor()
        sql = "DELETE FROM apikeys WHERE apikeys = %s"
        values = (api_key,)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.close()
        return "OK"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mydb.close()

@app.route('/', methods=['GET'])
def home():
    return "<h1>API</h1><p>API for the Back-End</p>"

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/api/keys', methods=['GET'])
def api_key():
    return listapikeys()

@app.route('/api/deletekeys', methods=['POST'])
def delete_keys():
    api_keylist = request.get_json()
    for api_key in api_keylist:
        delete(api_key)
    return "OK"
@app.route('/api/addkeys', methods=['POST'])
def add_keys():
    apikey = request.get_json()
    try:
        mydb = get_mysql_connection()
        mycursor = mydb.cursor()
        sql = "INSERT INTO apikeys (apikeys) VALUES (%s)"
        values = (apikey,)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.close()
        return "OK"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mydb.close()
@app.route('/random_api', methods=['GET'])
def random_api():
    try:
        mydb = get_mysql_connection()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM apikeys ORDER BY RAND() LIMIT 1")
        myresult = mycursor.fetchall()
        mycursor.close()
        apis = jsonify(myresult)
        return apis
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mydb.close()


if __name__ == '__main__':
    app.run()
