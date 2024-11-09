import shelve
with shelve.open ('my_data.db')as shelf:
    shelf['name']= 'alice'
    shelf['age']= 30
    shelf['hobbies']= ['reading', 'hiking', 'coding']
with shelve.open('my_data.db')as shelf:
    print(shelf['name'])
    print(shelf['age'])
    print(shelf['hobbies'])

