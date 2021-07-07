#Part 1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x [1][0] = 15
# print(x)

# students  = [
#     {'first_name': 'Michael','last_name' : 'Bryant'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
#     ]
# print(students)

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer']);

# z[0]['y'] = 30
# print(z[0])


#Part 2
students = [

        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key, val in list[i].items():
            output += f"{key} - {val},"
        print(output)

iterateDictionary(students)

#part 3

# def iterateDictionary2(key_name, some_list):
#     for student in some_list:
#         print(student[key_name])

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

#part 4

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for key, value in some_dict.items():
#         print(f"{len(value)} {key}")
#         for i in range(0, len(value)):
#             print(value[i])
# printInfo(dojo)

