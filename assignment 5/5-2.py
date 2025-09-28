Superhero = 'batman'
print(Superhero == 'batamn')
print(Superhero != 'superman')
print(Superhero == 'superman')

name = 'Bruce Wayne'
print(name.lower() == 'Bruce Wayne')
print(name.lower() == 'Clark Kent')

ages = 40
print(ages == 40)
print(ages != 21)
print(ages > 18)
print(ages < 18)
print(ages >= 50)
print(ages <= 58)

ages = 24
print(ages > 14 and ages < 60)
print(ages > 60 or ages < 4)

Gigs = ['250g', '500g', '850g']
print('850g' not in Gigs)
print('250g' not in Gigs)