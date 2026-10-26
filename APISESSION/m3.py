# Flask ipynb file interactive python notebook -> ipynb
from os import close, curdir

from flask import Flask, json,jsonify,Response, request
from flask_cors import CORS
import mysql.connector
app = Flask(__name__)
CORS(app=app) 


# NOTE: route "/"
@app.route("/",methods=["GET"])
def home() -> str:
    return "Student REST API is running"

# NOTE: Now let's try to connect to our database
def get_connection(password,database):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
@app.route("/students",methods=['GET'])
def get_students() -> Response:
    conn = get_connection(password="luffy",database="students")
    cursor = conn.cursor(dictionary=True)
    try :
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return jsonify(rows)
    finally:
        cursor.close()
        conn.close()
@app.route("/student/<int:id>",methods=['GET'])
def get_student_by_id(id) -> Response :
    conn = get_connection(password="luffy",database="students")
    cursor = conn.cursor(dictionary=True)
    try:
        sql_statement = "SElECT * FROM students WHERE student_id = %s"
        cursor.execute(sql_statement,(id,))
        row = cursor.fetchone()
        return jsonify(row)
    except Exception as e :
        return jsonify({
            "Error Occurend" : str(e)
        })
    finally:
        cursor.close()
        conn.close()

@app.route("/insert_student",methods=["POST"])
def insert_student() -> Response:
    conn = get_connection(password="luffy",database="students")
    cursor = conn.cursor()
    data = request.get_json()
    name = data['name']
    dept = data['dept']
    marks = data['marks']
    sql_statemt = "INSERT INTO students(name,dept,marks) VALUES(%s,%s,%s);"
    try:
        cursor.execute(sql_statemt,(name,dept,marks))
        conn.commit()
        return jsonify(cursor.lastrowid)
    except Exception as e:
        conn.rollback()
        return jsonify({
            "error" : str(e)
        })
    finally :
        cursor.close()
        conn.close()
@app.route("/update_student/<int:id>",methods=['PUT'])
def update_student_by_put(id)-> Response : 
    conn = get_connection(password="luffy",database="students")
    cursor = conn.cursor(dictionary=True)
    data = request.get_json()
    values = (
        data['name'],data['dept'],data['marks'],id
    )
    sql_statement = "UPDATE students set name=%s,dept=%s,marks=%s where student_id=%s"
    try :
        cursor.execute(sql_statement,values)
        conn.commit()
        return jsonify({"message" : "updated successfully"})
    except Exception as e :
        return jsonify({
            "Error Occured" : str(e)
        })
    finally :
        cursor.close()
        conn.close()

@app.route("/delete_student",methods=['DELETE'])
def delete_student():
    conn = get_connection(password="luffy",database="students")
    cursor = conn.cursor()
    data = request.get_json()
    student_id = data['student_id']
    sql_statement = "DELETE FROM students WHERE student_id = %s"
    try :
        cursor.execute(sql_statement,(student_id,))
        conn.commit()
        return jsonify({"message" :f"{student_id} row got deleted"})
    except Exception as e :
        conn.rollback()
        return jsonify({
            "error" : str(e)
        })
    finally :
        cursor.close()
        conn.close()
if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)


