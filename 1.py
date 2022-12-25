from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from flask import Flask
from flask import request
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