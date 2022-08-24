from flask import Flask,request,jsonify
app = Flask(__name__)
import pymongo
client = pymongo.MongoClient("mongodb+srv://vaishnavi:vaishnavi143@cluster0.dssdymw.mongodb.net/?retryWrites=true&w=majority")
database = client["api_mongo"]
collection = database["api_table"]

@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succefully inserted "))

if __name__ == "__main__":
    app.run(port=5005)




