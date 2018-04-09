<p align="center"><img src="https://cache.btpl.io/cache/landing_logo.svg" /></p>

# FluidDATA Flask Example


## About

The FluidDATA Python API can be used to search for spoken word phrases in
millions of podcast episodes.  This tutorial will show you how to setup the
FluidDATA API and integrate it with a simple Flask application that allows you
to search a single podcast channel.

Checkout the running demo of this app at <https://flask-demo.bitplatter.com>.

When you are done with this tutorial you can read the full API documentation here:
[FluidDATA python API](https://docs.bitplatter.com/fluiddata-python/)


## Installation

In order to run this example we will need to gather three things:

1. flask
2. fluiddata python library
3. FluidDATA API Token


### Flask

In this tutorial we are using flask 0.12.2. Older version of flask will work,
but the command to start the example application may be different. 

```bash
pip install flask
```


### FluidDATA python library

The FluidDATA python API is compatible with both python 2 and python 3.  It can
be installed via pip below.

```bash
pip install fluiddata
```


### FluidDATA API Token

You will need a FluidDATA API token to use the FluidDATA API.  By registering for an
account at https://accounts.bitplatter.com/register you will be automatically
enrolled in our free plan which allows up to 100 free searches per month.

After you have created an account navigate to
https://accounts.bitplatter.com/home/security to view your token.  You can
also view your remaining search quota or sign up for a larger plan at
https://accounts.bitplatter.com/home/subscriptions.

<p align="center"><img src="https://cache.btpl.io/cache/flask_example/token.png" /></p>


#### Validating the Token (optional)

You can use the **Fluid.subscription_info** method to verify that your API
token is working correctly.  Fire up a python interpreter and try calling the
**Fluid.subscription_info** method.  You should see output similar to what is
given below.

```python
>>> from fluiddata import Fluid
>>> token = '' # paste FluidDATA token here
>>> fluid = Fluid(token)
>>> fluid.subscription_info()
    {u'result': {
        u'canceled': False,
        u'fluid_search': 100,
        u'fluid_search_remaining': 100,
        u'period_end': u'2018-04-13T04:02:30Z',
        u'plan': u'fluid-free-monthly',
        u'price': u'0.00',
        u'status': u'active',
        u'stripe_id': u'fluid-free-monthly'},
     u'status': True}
```

## Setup Flask Application

Once you have your FluidDATA API token you will need to checkout and configure the Flask
application

```bash
git clone https://github.com/BitPlatter/fluiddata_flask_example.git
cd fluiddata_flask_example
```

### Configure the Flask Application

To configure the flask application we need to navigate to the
**fluiddata_flask_example** directory and edit the **settings.py** file.  

Open the settings.py file and fill in the values for **FLUID_TOKEN** and
**FLUID_RSS_URL**.  The **FLUID_TOKEN** will be your FluidDATA API token you
obtained in the [FluidDATA API Token](#fluiddata-api-token) section.  The
**FLUID_RSS_URL** can be any valid podcast RSS url.

```python
FLUID_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
FLUID_RSS_URL = 'http://your.rss.feed.url.here'
```

If you don't know a podcast feed url off the top of your head you can try one
of the example rss feeds below.

| Podcast       | FLUID RSS URL |
| ------------- | ------------- |
| Planet Money  | https://www.npr.org/rss/podcast.php?id=510289 |
| Joe Rogan Experience | http://joeroganexp.joerogan.libsynpro.com/rss |
| StarTalk Radio | http://feeds.soundcloud.com/users/soundcloud:users:38128127/sounds.rss |


## Running the Flask Application

Once the settings.py file has been populated we are ready to run the flask
application.  From the **fluiddata_flask_example** directory run the following
command to start flask.

```bash
FLASK_APP=fluiddata_flask.py flask run
```

You should now be able to point your browser to http://127.0.0.1:5000/ and view the webpage.

<p align="center"><img src="https://cache.btpl.io/cache/flask_example/asteroid.png" /></p>


## Troubleshooting

### Flask Exception: FluidDATA has not indexed this channel

We have indexed over 150,000 podcast channels, so its likely the podcast you
are interested in has already been indexed.  However, if your podcast feed is
not recognized then send us an email at <support@bitplatter.com> with a link to
the podcast channel and we will add it to our database.

### Flask returns "Something Went Wrong"

You may have used all of your FluidDATA API credits for the month.  The free
plan allows up to 100 free searches per month.  If you require a more search
credits please see our other plans at <https://www.bitplatter.com/fluiddata> or
<https://accounts.bitplatter.com/home/subscriptions>.

### Some audio doesn't play or when I skip to a search result it is several seconds off

We link back to the original source of the podcast as specified in the RSS
feed.  This means that if the audio file has been updated since we first
indexed it you may not get the exact right result.  Many podcasters only make
their podcasts free for a limited time or dynamically insert ads which can skew
the timestamps.  While we could serve the podcast episodes ourselves we want
to respect the podcast author's right to remove, edit, or correct their
podcast.

# Want to learn more?

This example only shows a subset of the full FluidDATA API functionality. The
full documentation for the API can be found at
<https://docs.bitplatter.com/fluiddata-python/>.


To learn more about BitPlatter please visit our website at <https://www.bitplatter.com>.

 
<p align="center"><a href="https://www.bitplatter.com/fluiddata"><img src="https://cache.btpl.io/cache/bitplatter-trans.png" /></a></p>
