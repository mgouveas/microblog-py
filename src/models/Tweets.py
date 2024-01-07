import datetime

tweet = {
    "author": str,
    "content": str,
    "likes": 0,
    "createdAt": datetime.datetime.now()
}



@app.route("/likes/:id", methods=['POST'])
def like():
    try:
        tweet_list = 'tweet'
    except IndexError:
        return jsonify({'status': 'Error', 'message': 'Tweet not found'})
    except Exception:
        return jsonify({'status': 'Error', 'message': 'Unknown error'})
    return jsonify(tweet_list)


    elif request.method == 'POST':
        request_data = request.get_json()
        new_tweet = {
            "author": request_data["Author"],
            "content": request_data["Content"],
            "likes": 0,
            "createdAt": datetime.datetime.now()
        }