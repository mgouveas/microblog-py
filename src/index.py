import pprint

import bson.objectid
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import logging
import routes
from flask import Flask, request, jsonify
import datetime
import random

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
            return jsonify(pprint.pprint(post))
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
        new_tweet = posts.insert_one(tweet_data)
        return jsonify(pprint.pprint(tweet_data))


# Dar like
@app.route("/likes", methods=['POST'])
def like():
    request_data = request.get_json()
    tweet_id = request_data['id']
    data_likes = posts.find_one({"_id": bson.objectid.ObjectId(request_data['id'])}, {"likes"})
    n_likes = data_likes["likes"]
    tweet_like = posts.update_one(
        {"_id": bson.objectid.ObjectId(request_data['id'])},
        {"$set": {"likes": n_likes+1}}
    )
    return jsonify()


if __name__ == '__main__':
    logging.info("Server on!")
    app.run()
