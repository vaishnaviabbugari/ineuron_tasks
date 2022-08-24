from flask import Flask,request,jsonify
import mysql.connector as conn
app = Flask(__name__)

mydb = conn.connect(host="localhost",user="root",password="vaishnavi143")
cursor=mydb.cursor()
cursor.execute("create database if not exists api_task")
cursor.execute("create table if not exists api_task.api_table (name varchar(30),number int)")

@app.route("/insert",methods =["POST"])
def insert():
    if request.method== "POST":
        name = request.json["name"]
        number = request.json["number"]
        cursor.execute("insert into api_task.api_table values(%s,%s)",(name,number))
        mydb.commit()
        return jsonify("succesfully inserted the data given ")

@app.route('/update',methods=["POST"])
def update():
    if request.method=="POST":
        get_name = request.json["get_name"]
        cursor.execute("update api_task.api_table set number = number + 10 where name = %s",(get_name,))
        mydb.commit()
        return jsonify("succesfully updated the values given")

@app.route('/delete',methods=['POST'])
def delete():
    if request.method == "POST":
        name_delete = request.json["name_delete"]
        cursor.execute("delete from api_task.api_table where name = %s ",(name_delete,))
        mydb.commit()
        return jsonify("succesfully deleted record")

@app.route('/fetch',methods=['post'])
def fetch():
    if request.method== "POST":
        cursor.execute("select * from api_task.api_table")
        l = [ ]
        for i in cursor.fetchall():
            l.append(i)
        mydb.commit()
        return jsonify(str(l),"fetched succesfully")

if __name__ == '__main__':
    app.run()


