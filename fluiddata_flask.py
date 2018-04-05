"""
Example FluidDATA API Flask application.
"""

from flask import Flask

from flask import request
from flask import render_template
from flask import redirect, url_for

from fluiddata import Fluid

app = Flask(__name__)

app.config.from_object('settings')

FLUID_TOKEN = app.config['FLUID_TOKEN']
FLUID_RSS_URL = app.config['FLUID_RSS_URL']

# Initialize the Fluid object with your FluidDATA API Token
fluid = Fluid(FLUID_TOKEN)

# Get the FluidDATA collection object associated with the RSS feed url.  We
# will use this to limit searches to only this RSS feed in our example page.
collection = fluid.feed_to_collection(FLUID_RSS_URL)

# Every API response contains a status variable indicating the success or
# failure of the API call
if not collection['status']:
    raise Exception(
        "FluidDATA has not indexed this channel: %s" % FLUID_RSS_URL)

# Get the FluidDATA collection id for this RSS feed.
collection_id = collection['result']['id']

@app.route('/')
def root():
    """ Redirect to /search url"""

    return redirect(url_for('search'))

@app.route('/search')
def search():
    """ Parse search query from user and return result template"""

    # Get the query term passed in by the user
    query = request.args.get('q', None)

    # Query the FluidDATA API for the query term passed in by the user,
    # limiting searches to the RSS channel this app is configured for
    result = fluid.query(query=query, collection_id=collection_id)

    if result['status']:
        # FluidDATA query was a success!  Pass the template to the user.
        return render_template('search.html', result=result)
    else:
        # Something went wrong with the FluidDATA API.  Check the
        # result['msg'] element for a possible explaination.
        return "Something Went Wrong"
