from flask import *
import json
import time
# from main1 import *
print("imports done")
app = Flask(__name__)

path = 'out_json/processed_Defence Ministry_data.json'


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        return {"error": str(e)}


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home',
                'Message': 'Successfully located the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))
    # /user/?user="query"
    data = read_json_file(path)
    print(user_query)
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=7777)