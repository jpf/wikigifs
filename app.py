import os
import random
import urllib
import json
from flask import Flask, request, Response, url_for, render_template
app = Flask(__name__)
data = []


def load_data():
    file = open('animated-gifs', 'ro')
    for line in file.readlines():
        data.append(line.strip())


@app.route("/random")
def randompick():
    callback = request.args.get('callback')
    choice = random.choice(data)
    rv = json.dumps({'image': choice})
    if callback:
        rv = "%s(%s)" % (callback, rv)
    return Response(rv, mimetype='application/json')


@app.route("/")
def index():
    return render_template('index.html', random_service=url_for('randompick', _external=True))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    load_data()
    app.debug = True
    app.run(host='0.0.0.0', port=port)
