from flask import Flask, request, abort
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/append", methods=['POST'])
def append():
    try:
        payload = json.loads(request.data.decode('utf-8'))
    except json.JSONDecodeError:
        return abort(400)

    print("\n".join([x['url'] for x in payload]))
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, port=4200)
