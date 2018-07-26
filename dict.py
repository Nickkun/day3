person = {'name':'Nick', 'address':'cheonan', 'email':'jang@ancle.kr'}
print(person)
print(person['name'])
print(person['email'])

person['name'] = 'Jay' 

print(person.items())
for key, value in person.items():
    print('\nKey \\ "' + key + '"')
    print('Value \\ "' + value + '"')

# Key \ "name"
# Value \ "Nick"