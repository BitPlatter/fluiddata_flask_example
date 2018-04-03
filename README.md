
About
=====

The FluidDATA python API can be used to query millions of podcast episodes.  This tutorial will show you how to integrate the FluidDATA python API with a simple flask application that can search a single podcast channel.


Installation
============

pip
---

The FluidDATA python API can be installed via pip below

```bash
pip install fluiddata
```

FluidDATA API Token
---------------------

To use the FluidDATA python API you will need an API Token which you can get by creating an account at [https://accounts.fluiddata.com/register]

![alt text]("https://cache.btpl.io/cache/fb.png" "Account Creation")
![alt text]("https://cache.btpl.io/cache/fb.png" "FluidDATA Token")


Validating the Token
--------------------

You can use the ``subscription_info`` method to verify that your API token is working correctly.

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

Setup Flask Application
-----------------------

Once you have your FluidDATA Token you will need to configure the Flask application

```bash
git clone <path>
```

Setup Flask Application
=======================

```bash
cd fluiddata_flask_example
```

Open the settings.py file and fill in the values for `FLUID_TOKEN` and `FLUID_RSS_URL`



```python
FLUID_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
FLUID_RSS_URL = 'https://www.npr.org/rss/podcast.php?id=510289'
```

| Podcast       | FLUID RSS URL |
| ------------- | ------------- |
| Planet Money  | https://www.npr.org/rss/podcast.php?id=510289 |
