import flask

app = flask.Flask(__name__)


#         _..._
#       .'     '.      _
#      /    .-""-\   _/ \
#    .-|   /:.   |  |   |
#    |  \  |:.   /.-'-./
#    | .-'-;:__.'    =/
#    .'=  Maberdeb_.='
#   /   _.  |2023;
#  ;-.-'|    \   |
# /   | \    _\  _\
# \__/'._;.  ==' ==\
#          \    \   |
#          /    /   /
#          /-._/-._/
#          \   `\  \
#           `-._/._/
#
#         dev by maberdeb
#         hello everyone !

@app.route('/')
def index():
    var = flask.json.load(open('config.json'))
    flask.url_for('static', filename="static/style.css")
    return flask.render_template('index.html', v=var)