# Python scripting

# Easy to understand
# Many libraries
# Large community
# language interoperatibility (Python can talk to other languages and software easily)

# Why do we care about scripting?

# Automate repetitive manual tasks using code

# Some examples of things we can write scripts for as a DevOps engineer

# Python to query a database
# Write Python to execute a shell command
# Write a Python script to create a backup
# Write Python script to fetch I.P's addresses of an autoscaling
# Python script to check the expiry date of an SSL certificate

# Seven in built modules that allow us to start to do some interesting things:

# sys
# os
# subprocess
# math
# random
# datetime
# json

# sys module
import sys

print(sys.version) # version of python on this computer

# os module
# import os
#
# # print(os.getcwd())
# # os.chdir()
#
# os.mkdir("new_dir")

# subprocess module
import subprocess

# Be careful to not create an infinite loop. Automate only after you are happy with the manual process.
subprocess.run(["python", "hello_world.py"])

# math module
import math

pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

# random module
import random

randum = random.randrange(1, 10)
print(randum)

# datetime module
import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

# Json module
import json

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)

print(y)
print(x)

