import json
from datetime import datetime
from flask import Flask, request, abort

from database import db_session
from models import Visit

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/append", methods=['POST'])
def append():
    try:
        payload = json.loads(request.data.decode('utf-8'))
    except json.JSONDecodeError:
        return abort(400)

    for v in payload:
        visit = Visit(
            url=v['url'],
            time=datetime.strptime(v['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ"),
            raw_dom=v['html']
        )
        db_session.add(visit)
    db_session.commit()
    print("Logged %i urls" % len(payload))
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, port=4200)
