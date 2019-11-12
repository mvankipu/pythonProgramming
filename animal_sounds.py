def speak(animal='dog'):
    animals = ['pig','duck','cat','dog']
    sounds = ['oink','quack','meow','woof']
    animal_sounds = dict(zip(animals,sounds))

    if animal in animal_sounds:
        return animal_sounds[animal]
    else:
        return '?'

while(True):
    test_animal = input('Which animal? ')
    if test_animal == '':
        test_animal = 'dog'
        print('I\'ll assume you meant dog...')
    print(f'{test_animal} says {speak(test_animal).upper()}')
    var = input('Another time (y/n)? ')
    if var=='n' or var=='N':
        break
print(speak())
