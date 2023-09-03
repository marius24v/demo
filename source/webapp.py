#!flask/bin/python
from flask import Flask, jsonify, request
app = Flask(__name__)

# we want all request types:
HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route('/', methods=HTTP_METHODS)
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None: 
        s = request.environ.get('REMOTE_ADDR')
        ip  = s.split('.')
        return jsonify({'ip': '.'.join(ip[::-1])}), 200
    else:
        s = request.environ.get('HTTP_X_FORWARDED_FOR')
        ip = s.split('.')
        return jsonify({'ip': '.'.join(ip[::-1])}), 200


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
