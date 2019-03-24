# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1,2,3,4,5]
print(type(numbers))

numbers1= list((1,2,3,4,5))
print(numbers1)

fruits = ['Apple','banana','Oranges','Grapes']

#get fruits
print(fruits[1])

#get len
print(len(fruits))

#Append to list
fruits.append('Mangos')

#insert
fruits.insert(2, 'Straberries')

#Remove
fruits.pop(3)

#Reverse List
fruits.reverse()

#sort list
fruits.sort()

#reverse sort
fruits.sort(reverse=True)

print(fruits)