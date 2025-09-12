location = ["France", "Egypt", "Japan", "Thailand", "Brazil"]
original = location[:]
print(location)
alphabetical = sorted(location)
print(alphabetical)
print(original)
location.reverse()
print(location)
sorted_location = sorted(location, reverse=True) 
print(sorted_location)