#!/usr/bin/env python3

from flask import Flask, request, current_app, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
    '''

@app.route('/status')
def status():
    response = make_response('<h1>Success!</h1>', 200)
    return response

@app.route('/headers')
def headers():
    response = make_response('<h1>Custom headers set!</h1>')
    response.headers['Custom-Header'] = 'FlatironSchool'
    return response

@app.route('/json')
def json_route():
    response = make_response('{"message": "This is JSON"}', 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/easy-json')
def easy_json():
    data = {"message": "This is easier!"}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)


