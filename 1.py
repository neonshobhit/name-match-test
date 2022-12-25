from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from flask import Flask
from flask import request
__name__ = "__main__"
app = Flask(__name__)
print(app)
@app.route('/')
def about():
  return "name match"
@app.route('/test', methods=['GET', 'POST'])
def home():
    print(request.json)
    entered = request.json['entered']
    original = request.json['original']
    f = fuzz.ratio(entered,original)
    print(f)

    return str(f)
# print(__name__)
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=Flask, port=3008)