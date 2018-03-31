from flask import Flask
app = Flask(__name__)

from flask import request
from flask import render_template
from flask import redirect, url_for

from fluiddata import Fluid

app.config.from_object('settings')

FLUID_TOKEN = app.config['FLUID_TOKEN']
FLUID_RSS_URL = app.config['FLUID_RSS_URL']

fluid = Fluid(FLUID_TOKEN)
collection = fluid.feed_to_collection(FLUID_RSS_URL)
collection_id = collection['result']['id']

@app.route('/')
def root():
    return redirect(url_for('search'))

@app.route('/search')
def search():
    query = request.args.get('q', None)

    result = fluid.query(query=query, collection_id=collection_id)
    return render_template('search.html', result=result)
