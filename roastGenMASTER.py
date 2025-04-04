# this is the file that will be used to handle the process of getting the data for the roast and sending it in to be generated and retrieving the generated roast
# the directories of the files
spotifyFile = "spotifyroastinator/spotify"
geminiFile = "spotifyroastinator/gemini"

import sys
import os

# make it possible for the file to grab from the spotify and gemini files
sys.path.append(os.path.abspath(spotifyFile))
sys.path.append(os.path.abspath(geminiFile))

# print(os.path.abspath(spotifyFile))

# import them
from spotify import getData
from gemini import generateRoast


# NOTE: the below is like this for now but might change/ due to not currently knowing what form the data and roast will be saved as
data = getData() # call the function in the spotify file that gets and returns the data
roast = generateRoast(data) # send the data to be generated

# use Flask's render template to send in the generated roast directly to the loaded page to be more secure and straight forward