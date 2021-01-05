import pickle
import random
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

with open('friends_tokens', 'rb') as f:
    tokens=pickle.load(f)

with open('friends_titles', 'rb') as f:
    titles=pickle.load(f)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/result', methods=['POST', 'GET'])
def generate_episode():

    keyword = request.form['keyword']
    keyword_count = {}
    for serie_number,serie in tokens.items():
        for episode_number,episode in serie.items():
            for word in episode:
                if keyword == word:
                    try:
                        keyword_count[serie_number,episode_number] += 1
                    except:
                        keyword_count[serie_number,episode_number] = 1
    sorted_count = sorted(keyword_count, key=keyword_count.get, reverse=True)[:5]
    final_dict={}
    for serie_number,serie in sorted_count:
        final_dict[serie_number,serie] = titles[serie_number][serie]
    random_episode = random.choice(list(final_dict.items()))
    return str(random_episode[0]) + ': ' + random_episode[1]
