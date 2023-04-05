# Python Libraries and Modules

# Extensive libraries in Python - External collections of useful functions and methods

# Python comes with some integrated libraries

from random import random
import math

print(random())

num_float = 23.66
print(math.ceil(num_float)) # rounds up

num_float = 23.66
print(math.floor(num_float)) # rounds down

print(math.pi)

# Modules
import os
import datetime, sys

working_dir = os.getcwd()
print(working_dir)

print(datetime.date.today())

print(sys.path)

def operations_system_information():
    print(os.cpu_count())

operations_system_information()

# pip - pythons package manager

import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.status_code)
print(requests_bbc.content)