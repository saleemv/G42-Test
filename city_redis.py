from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

REDIS_SERVER = os.getenv("REDIS_SERVER")
red = redis.Redis(host=REDIS_SERVER, port=6379, db=0, charset="utf-8", decode_responses=True)
@app.route('/')
def landing():
    return jsonify(message='This is the G42 Assignment!')

@app.route('/health')
def health_check():
    return jsonify(message='OK')


@app.route('/city', methods=['POST'])
def add_or_update_city():
    data = request.get_json()
    city_name = data['city']
    population = data['population']
    red.set(city_name, population)
    return jsonify({'status': 'success'})


@app.route('/city/<name>', methods=['GET'])
def get_population(name):
    popu = red.get(name)
    if not popu:
        return jsonify({'error': 'city not found'})
    return jsonify(name, popu)


if __name__ == '__main__':
    app.run(debug=True)
