from flask import Flask

# TODO: use versions
server = Flask(__name__)

@server.route('/')
def health():
   return 'OK'
