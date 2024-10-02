# import math
# --------------------------

# def sqrt(n):
#     return n**0.5
# --------------------------
# sqrt=lambda n:n**0.5
# --------------------------
# students=[
#     {
#         'name':'student1',
#         'phone':'09124798373',
#     },
#       {
#         'name':'student2',
#         'phone':'09122381964',
#     },
#       {
#         'name':'student3',
#         'phone':'09194655241',
#     },
# ]

# students_names=list(map(lambda student:student['name'],students))

# print(students_names)

# ------------------------------------
students=[
    {
        'name':'student1',
        'phone':'09124798373',
    },
      {
        'name':'student2',
        'phone':'09122381964',
    },
      {
        'name':'student3',
        'phone':'09194655241',
    },
]

students_names=list(map(lambda student:student['phone'],students))

print(students_names)