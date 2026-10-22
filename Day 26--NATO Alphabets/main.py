# # numbers = [1, 2, 3]
# # new_list = [n*2 for n in range(1, 5)]
# # print(new_list)


# short_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)

# file1 = [3,
#          6,
#          5,
#          8,
#          33,
#          12,
#          7,
#          4,
#          72,
#          2,
#          42,
#          13
#          ]

# file2 = [3,
#          6,
#          13,
#          5,
#          7,
#          89,
#          12,
#          3,
#          33,
#          34,
#          1,
#          344,
#          42,
#          ]


# print(result)

import random

names = ["Mark", "Beth", "Mercy", "Freddie", "John"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
