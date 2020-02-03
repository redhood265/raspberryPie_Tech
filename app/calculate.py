from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    if request.method == 'GET':
      return jsonify({"リクエストタイプ": "GETリクエスト"}),200
    else:
      return jsonify({"リクエストタイプ": "GET以外のリクエスト"}),200

if __name__ == '__main__':
  app.run()

