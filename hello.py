from flask import request
from flask import Flask

app = Flask(__name__)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if True:
#             return request.form['username']
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return "<p>Hello</p>"

@app.route('/guide', methods=["GET", "POST"])
def add_guide():
    title = request.form['title']
    return '<p>Hello!</p>'
