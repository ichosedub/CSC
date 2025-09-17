evens = [n for n in range(2, 21)][0: :2]
print(evens)
evens = [n * 2 for n in range (1, 11)][0::2]
print(evens)
evens = [n for n in range(2, 21)[0:19:2]]
print(evens)
# can you rewrite the evens list comprehension using the mod (%) operator?
evens = [n if n % 2 == 0 else 0 for n in range(2,21)]
print(evens)
evens = [ n for n in range(2,21) if n % 2 == 0]
