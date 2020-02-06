from flask import Flask, jsonify
import getNikkeiTop

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return jsonify({
    "message": "テスト!!",
    "スクレイピング結果":getNikkeiTop.getScrapingResult()
  })

if __name__ == '__main__':
  app.run()

