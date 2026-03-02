people = []
for i in range(1,31):
    people.append(i)
for i in range(28):
    number = int(input())
    people.remove(number)
for i in range(2):
    print(people[i])