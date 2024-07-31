calls = 0

def count_calls():
    global calls
    calls=calls+1
def string_info(string):
    count_calls()
    tuple_=(len(string),string.upper(),string.lower())
    return tuple_
def is_contains(string ,list_to_saarch):
    count_calls()
    for i in list_to_saarch:
        if i.upper() == string.upper():
            return True
    return False

print(string_info('Afoniia'))
print(string_info('Sirprais'))
print(is_contains('Horse',['dOg','hoRsE', 'caT']))
print(is_contains('Meaning',['purpose', 'principle', 'appeal' ]))
print(calls)

