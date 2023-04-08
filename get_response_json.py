import logging
import requests
import os
import json

def find_item(obj, key):
    """
    Recursively search a dictionary (passed in as obj) for a key (passed in as key)
    :param obj: a dictionary object
    :param key: a string value with the key you are looking for
    :return: the value found at the key or None if the key is not found
    """
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = _finditem(v, key)
            if item is not None:
                return item


print('Starting ... ')


client = client()

# Make sure we don't miss any error
client.errors_as_exceptions(True)

logging.basicConfig(filename='sample.log', level=logging.INFO)

url = "https://api.example.com"

payload={}
headers = {
    'Authorization': 'Bearer 6R9Ctez7pwSyl7qaKU',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

# first we will test that the result that comes back is valid json and throw an exception if not.
# if the response, isn't a JSON object, then we will have use a different logic to extract what we want
# it is valid json, then we proceed to extract the value at the requested key if it exists.
response_json_object = None
key = 'widgets' # @developer: set this to the desired key
try:
    response_json_object = response.json()
except Exception as e:
    print(f'Error: response does not contain a valid json object, extract key: "{key}" using another method')
    print(f'atempting to print response {str(response)} type is: {type(response)}')

if response_json_object is None:
    print("Exiting early. Unable to extract JSON object from response. Try another method.")
    quit()
else:
    print(f'confirmed that response contains a valid json object.')
    #print(response_json_object)

# next we will attempt to find the first data member in the JSON object with the requested key or if there is none
# display a message indicating that it was not found
try:
    value = find_item(response_json_object, key)
except Exception as e:
    print(f'Error: Exception thrown when attempting to find widgets key in JSON object')

if value is None:
    print(f'Error: Key "{key}" was not found.')
else:
    print("Value in json response object was found successfully. Attempting to print value.")
    print(f'If values returned is array type, length of array is: {len(value)}')
    print(f'{str(value)}')

print('Done')
