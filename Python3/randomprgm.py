import random

x = [i for i in range(1,11)]

print("Random sample of 5 elements")
print(random.sample(x,5))

print("Choice",random.choice(x))

print("Random number 1 to 100 using random()")
print(round(random.random()*100))

print("Random number between 1 to 10 using randint():",random.randint(1,10))

print("Random even number 1 to 100 using randrange()")
print(random.randrange(1,100,2),end=" ")

print("Before shuffle:",x)
random.shuffle(x)
print("After shuffle:",x)