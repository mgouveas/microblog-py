import pprint
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import logging
import routes
from flask import Flask, request, jsonify, Response
import datetime
from bson.objectid import ObjectId

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

uri = "mongodb+srv://mgs:908621@twitter.jmvtvue.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.twitter
collections = db.tweets
posts = db.tweets

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    logging.warning(e)

app = Flask(__name__)


# Listar e Criar Tweets
@app.route("/tweets", methods=['GET', 'POST'])
def tweet():
    if request.method == 'GET':
        for post in posts.find():
            pprint.pprint(post)
        return jsonify()
    elif request.method == 'POST':
        request_data = request.get_json()
        author = request_data['author']
        content = request_data['content']
        tweet_data = {
            "author": author,
            "content": content,
            "likes": 0,
            "createdAt": datetime.datetime.now()
        }
        new_tweet = posts.insert_one(tweet_data).inserted_id
        return jsonify()


# Dar like
@app.route("/likes/:id", methods=['POST'])
def like():
    params = request.get_data()
    pprint.pprint(params)
    return jsonify()


if __name__ == '__main__':
    logging.info("Server on!")
    app.run()
