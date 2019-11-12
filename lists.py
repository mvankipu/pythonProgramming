# instructors = []
# instructors.extend(['Colt','Blue','Lisa'])
# print(instructors)
# instructors.pop()
# print(instructors)
# del instructors[0]
# print(instructors)
# instructors.insert(0,'Done')
# print(instructors)

# answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]
# print(answer)

# answer2 = [name.lower()[len(name)::-1] for name in ['Elie','Tim','Matt']]
# print(answer2)

# answer3 = [num for num in range(1,100) if num%12 == 0]
# print(answer3)

# answer4 = [num for num in range(12,100,12)]
# print(answer4)

answer = [[num for num in [0,1,2]] for s_num in [0,1,2]]
print(answer)

answer2 = [[num for num in range(0,10)] for num in range(0,10)]
print(answer2)
#[[i for i in range(0,3)] for num in range(0,3)]
