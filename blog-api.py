import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error
from addentry import insert_post
app = flask.Flask(__name__)
app.config['DEBUG'] = True

'''
posts = [
    {   'id': 0,
        'title': 'My first blog post!',
        'body': 'This is my first blog post! I think it is very epic and poggers...',
        'author': 'Brennan',
        },
        {   'id': 1,
        'title': 'My second blog post!',
        'body': 'This is my second blog post! David has a hearthstone addiction!',
        'author': 'Brennan'
        }
]
'''

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "Api successful"

@app.route('/api/v1/blog/posts/titles/all', methods=['GET'])
def api_all():

    conn = sqlite3.connect('posts.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_posts = cur.execute('SELECT id, title, author FROM posts').fetchall()

    '''
    titles = []
    for post in all_posts:
        titles += [{'id': post['id'], 'title': post['title'], 'author': post['author']}]
    '''

    return jsonify(all_posts)

@app.route('/api/v1/blog/posts', methods=['GET'])
def api_id():
    id = request.args.get('id')
    query = "SELECT * FROM posts WHERE "
    if id:
        query += f"id={id};"
    else:
        return "Please provide a post ID"      

    conn = sqlite3.connect('posts.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    post = cur.execute(query).fetchall()
    
    return jsonify(post)

app.run()