# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#simple dict
person = {
    'first_name': 'Arti',
    'last_name': 'sain',
    'age': 23
}

#using constructer
person1 = dict(first_name='Arti',last_name='sain',age=23)
print(person1)

#access val
print(person['first_name'])
print(person.get('last_name'))

#add
person['phone'] = '387465'

#get keys
print(person.keys())

#get values
print(person.items())

#copy
person2 = person.copy()
person2['city'] = 'Newyork'
print(person2)

#remove item
del(person['age'])
person.pop('phone')

#clear
person.clear()
#get length
print(len(person2))
print(person)

#list of dict
people = [{'fname':'Arti','age':23},{'fname':'pooja','age':22}]
print(people)