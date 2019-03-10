import requests
import json
import os


fname = "C:/Users/rd281/Documents/filework.txt"
if os.path.isfile(fname):
    '''comment'''
    '''println("Found file '{}'".format(fname))'''
    with open(fname, 'r') as f:
        for line in f:
            print(line)
nexfile = "C:/Users/rd281/Documents/"
file_name = os.path.join(nexfile, "filework.txt")
my_file = open(file_name)
my_file_contents = my_file.read()
print(my_file_contents)
'''print(my_file_contents)'''
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
parameters = {"lat": 40.71, "lon": -74}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.content)
data = response.json()
print(type(data))
data_string = json.dumps(data)
print(type(data_string))

