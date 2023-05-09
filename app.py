# import requests
# from flask import Flask, jsonify, request
# from flask_caching import Cache  # Import Cache from flask_caching module

# app = Flask(__name__)
# # Set the configuration variables to the flask application
# app.config.from_object('config')
# cache = Cache(app)  # Initialize Cache


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")
import requests
from flask import Flask, request, jsonify
from config import BaseConfig
from flask_caching import Cache

app = Flask(__name__)
# cache = Cache(app, config={'CACHE_TYPE': 'redis','CACHE_REDIS_URL': 'redis://localhost:6379/0'})
app.config.from_object(BaseConfig)
cache = Cache(app)


@app.route("/")
def home():
    return "<a href=/university> university </a>"


@app.route("/inst/<string:country>")
def get_university(country):
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    # r = requests.get(f"{API_URL}{search}")
    r = requests.get(f"{API_URL}{country}")
    return jsonify(r.json())


@app.route("/univ/<string:country>")
@cache.cached(timeout=300, query_string=False)
def get_univ(country):
    API_URL = "http://universities.hipolabs.com/search?country="
    # search = request.args.get('country')
    # r = requests.get(f"{API_URL}{search}")
    r = requests.get(f"{API_URL}{country}")
    return jsonify(r.json())


@app.route('/square/<int:number>')
@cache.cached(timeout=50)
def square(number):
    app.logger.info(f"Computing the square of {number}")
    return jsonify({"computed": number*number})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
