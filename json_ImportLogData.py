import json

"""
def print_nested_dict(dict_obj, indent=1):
    # Pretty Print nested dictionary with given indent level
    # Iterate over all key-value pairs of dictionary
    for key, value in dict_obj.items():
        # If value is dict type, then print nested dict
        if isinstance(value, dict):
            print(' ' * indent, key, ':', '{')
            print_nested_dict(value, indent + 4)
        else:
            print(' ' * indent, key, ':', value)

"""

with open('json_LogData.json') as log:
	logData = json.load(log)

logObject = json.load(logData)

for key, value in logObject.items():
	print(str(key) + ' : ' + str(value))

"""
# Print The Infomration
print('\nNested Data')
print_nested_dict(logData, 3)
"""
