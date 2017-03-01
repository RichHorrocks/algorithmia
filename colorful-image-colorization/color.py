#!/usr/bin/env python

import sys
import Algorithmia

# Set the client.
client = Algorithmia.client('simrCXPNNPYiQOclGHFh9a1VVm+1')
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.5')

# Get the directory to use from the user.
user_dir = raw_input("Enter the Dropbox directory to use: ")
dir_path = "dropbox://Public/Algorithmia/" + user_dir

# Check if a specific directory exists
if client.dir(dir_path).exists():
    # The .dir() method takes a Data URI path and returns an Algorithmia.datadirectory.DataDirectory 
    # object for the child directory.
    dir = client.dir(dir_path)
    for file in dir.files():
        print "Converting: " + file.path
        print algo.pipe(file.path)
else:
    print("Directory doesn't exist - exiting")