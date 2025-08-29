From flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient

app = Flask(__name__)
CONNECTION_STRING = "mongodb+srv://tarehosty:cheruiyot8711@cluster0.9ezx159.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(CONNECTION_STRING)
collection = client["nameapp"]["names"]

@app.route(/)
def home():
    return send_from_directory('.','edit.html')

@app.route('/<path:filename>')
def files(filename):
    return send_from_directory('.','filename')

@app.route('/api/name', methods = ['GET'])
def get_name():
    doc = collection.find_one({"id":"current_name"})
    return jsonify({'name':doc['name'] if doc else ""})

@app.route('/api/name', methods = ['POST'])
def save_name():
    name = request.json['name']
    collection.update_one({"id":"current_name"},{"$set":{"name":name}}, upsert=True)

app.run(port=5000)


