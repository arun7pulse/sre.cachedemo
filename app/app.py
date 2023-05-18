import os
import json
import requests

from flask import Flask, request, jsonify
from config import BaseConfig
from flask_caching import Cache


# from redis import Redis
# def get_connection(name='myredis', host=None, port=None, password=None):
#     redis = Redis(host=os.environ.get("REDIS_HOST", "localhost"),
#                   port=os.environ.get("REDIS_PORT", 6379),
#                   db=0, decode_responses=True,
#                   client_name=name)
#     print("PING: ", redis.ping(), "Client_name: ", redis.client_setname(name))
#     return redis


app = Flask(__name__)
app.config.from_object(BaseConfig)
cache = Cache(app)
# dbc = get_connection()


@app.route("/")
def home():
    return "<div><div> <a href=/university> university </a></div> <a href=/square> square </a></div></div>"

# cachekey = f"weather:{location}:{startdate}:{enddate}:average"

@app.route('/info')
def info():
    # resp = {
    #     'connecting_ip': request.headers['X-Real-IP'],
    #     'proxy_ip': request.headers['X-Forwarded-For'],
    #     'host': request.headers['Host'],
    #     'user-agent': request.headers['User-Agent']
    # }
    return jsonify(json.dumps(request))

@app.route('/flask-health-check')
def flask_health_check():
    return "success"


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
@cache.cached(timeout=300)
def square(number):
    app.logger.info(f"Computing the square of {number}")
    return jsonify({"computed": number*number})


@app.route('/cube/<int:number>')
@cache.cached(timeout=300)
def cube(number):
    app.logger.info(f"Computing the cubic of {number}")
    return jsonify({"computed": number*number*number})

# import json
# @app.route('/request')
# @cache.cached(timeout=300)
# def req():
#     app.logger.info(request.__dict__)
#     return jsonify(json.dumps(request.__dict__))

# @app.route("/cube/<int:number>")
# def cubic(number):
#     cachekey = f'cubic:{number}'
#     cacheresult = dbc.get(cachekey)
#     if (cacheresult):
#         return jsonify({"computed": cacheresult, "source": "cache"})
#     app.logger.info(f"Computing the cubic square of {number}")
#     result = number*number*number
#     if (result):
#         dbc.set(cachekey, result, 300)
#     return jsonify({"computed": result, "source": "service"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
