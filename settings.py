import os

# Get your FluidDATA Token at https://accounts.bitplatter.com/home/security
FLUID_TOKEN = None

# Place a valid RSS feed url here
FLUID_RSS_URL = None

if FLUID_TOKEN is None:
    FLUID_TOKEN = os.environ.get('FLUID_TOKEN', None)

if FLUID_RSS_URL is None:
    FLUID_RSS_URL = os.environ.get('FLUID_RSS_URL', None)
