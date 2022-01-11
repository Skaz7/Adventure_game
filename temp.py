class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print(f'My name is {self.name}')

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print(f'...And I am {self.hero_name}')


seb = Person('Sebastian')
seb.reveal_identity()

wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()


print(type('sebastian'))
if type('sebastian') == str:
    print('TAK')
else:
    print('NIE')


a = [1,3,5,7,9,11]
c = [x*2 for x in a]
d = [x**2 for x in range(1, 7)]
e = [x**2 for x in range(6, 0, -1)]
print(a)
print(c)
print(d)
print(e)
