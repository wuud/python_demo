import random
random.seed(10)
print(random.random())
print(random.random())

print(random.randint(0,55))
print(random.uniform(0,55))
print(random.choice([2,5,8,3]))
s=[1,2,3,4,5]
random.shuffle(s)
print(s)
