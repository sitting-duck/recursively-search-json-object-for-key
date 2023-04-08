### Setup
Install beautiful soup and requests:
```
pip3 install requests
```

### Relevant Docs
Here is the contents of the python reponse object in the official docs:
https://requests.readthedocs.io/en/latest/user/quickstart/#response-content

Here is a SO discussion on recursive search of a JSON object
https://stackoverflow.com/questions/14962485/finding-a-key-recursively-in-a-dictionary

### Pretty JSON tips in Sublime Text
Use **Pretty JSON: Format JSON Lines** in Sublime to Format JSON prettily with proper newlines. Some formatters do nothing for newlines and indentation. Sometimes you may have to use the
**Pretty JSON: Format** command first to make it cooperate.

### Methods
We need to understand what we are doing here. First, let's understand that we cannot predict always exactly what form the object returned to us from the request (called the response) will be.
We are communicating with a server someone else controls, so we should assume that at any time they can change their code and the response may be different from what it was yesterday.

For this reason we should write code that is resistant to such changes and will not "break" or become outdated at any moment. In order to do this, we will do a "complete search" of the response object returned to us of all the keys that we are interested in.

We are using search because we can't just hardcode the path to the key:value pair that we want. A complete (sometimes called recursive search, although recursion is not necessary to achieve completeness).

We want this code to be generalized we can use it to search for any key we want. 
We will set an variable in the code "key" to the value of the key we want. Let's say we are searching for the key 'widgets'.

First we will test the response object has returned a string that can be parsed into a valid JSON object.
No use to try if what is returned to is noise or invalid data, so we exit early
if we don't get what we want. The code can be extended to use other methods if valid JSON is not found.

```
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

```

Next, once we have confirmed we can extract a valid json object from reponse, we can do the search of the object for the desired key. The implemented search method we use returns simply the first value found with matching key, and if there are multiples, these will not be returned. The code can be easily modified to return all, since the search is a complete search of the entire object.

Once we have confirmed that the key can be found, we can go ahead and print the value of that key and make sure it what we expect.

```
# next we will attempt to find the first data member in the JSON object with the requested key or if there is none
# display a message indicating that it was not found
try:
    value = find_item(response_json_object, "widgets")
except Exception as e:
    print(f'Error: Exception thrown when attempting to find widgets key in JSON object')

if value is None:
    print(f'Error: Key "{key}" was not found.')
else:
    print("Value in json response object was found successfully. Attempting to print value.")
    print(f'If values returned is array type, length of array is: {len(value)}')
    print(f'{str(value)}')

```


### Widgets value
The value for the key 'widgets' seems to be an array so keep that in mind. 