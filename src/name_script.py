for letter in 'KelleyShann':
    print('The letter: ', letter)
    
print('That is my name!')

#defining name and age lists
names = ['kelley','sarah','john','james']
ages = [28,28,34,21]

for n, a in zip(names, ages):
    print(n, "is", a)

#determining who the oldest is
oldest = max(ages)

for n, a in zip(names, ages):
    if a == oldest:
    print(n, "is the oldest")

