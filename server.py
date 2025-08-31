from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

CONNECTION_STRING = "mongodb+srv://tarehosty:cheruiyot8711@cluster0.9ezx159.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(CONNECTION_STRING)
collection = client["nameapp"]["names"]


@app.route('/api/name', methods=['GET'])
def get_name():
    doc = collection.find_one({"id": "current_name"})
    return jsonify({'name': doc['name'] if doc else ""})

@app.route('/api/name', methods=['POST'])
def save_name():
    name = request.json['name']
    collection.update_one({"id": "current_name"}, {"$set": {"name": name}}, upsert=True)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)