#3-1
names = ['Jaden', 'TiyDye', 'Theo', 'Kiyah']
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])

#3-2
message = f"My best friend's name is {names[0]}."
print(message)
message = f"I gave my friend Tiyesha the nickname {names[1]}."
print(message)
message = f"My friend {names[-1]} is afashion model."
print(message)
message = f"I've been friends/brother {names[-2]} since we were kids in church."
print(message)

#3-3
transportation = ['ice cream truck', 'clown car', 'banana car']
message = f"I can fit into a {transportation[1]}", f"I am scared our nieghborhood {transportation[0]}" , f"I wanna drive a {transportation[2]} to college"
print(message)

#3-4
guest_list = ['Timmy', 'Tommy', 'Jimmy']
message = f"Dear {guest_list[0]}, your invited to dinner this evening at my humble housing."
print(message)
message = f"Dear {guest_list[1]}, your invited to dinner this evening at my humble housing."
print(message)
message = f"Dear {guest_list[2]}, your invited to dinner this evening at my humble housing."
print(message)

#3-5

guest_list = ['Timmy', 'Tommy', 'Jimmy']
guest_backup = ['Doofy', 'Goofy']

message = f"Dear {guest_list[0]}, your invited to dinner this evening at my humble housing."
print(message)
message = f"Dear {guest_list[1]}, your invited to dinner this evening at my humble housing."
print(message)
message = f"Dear {guest_list[2]}, your invited to dinner this evening at my humble housing."
print(message)
message = f"Sadly {guest_list[0]} couldn't make it."
print(message)
message = f"So {guest_backup[1]} is coming in their place."
print(message)
message = "Hello, everyone attending we have located a bigger table on the market," \
" so I wil be extending the list a bit"
print(message)

#3-6
guest_reform = ['Brad', 'Chad', 'Rick']
guest_reform.insert(0, 'Henry')

message = "Sadly my friends our newer found talbe wont be arriving on time so we only have space for two guests."
print(message)

#3-7
guest_list = ['Timmy', 'Tommy', 'Jimmy']
guest_reform = ['Brad', 'Chad', 'Rick']
guest_backup = ['Doofy', 'Goofy']


message = f"Dear {guest_reform[1]}, I am sorry I can't invite you to dinner this evening."
print(message)
message = f"Dear {guest_reform[2]}, I am sorry I can't invite you to dinner this evening."
print(message)
message = f"Dear {guest_backup[1]}, I am sorry I can't invite you to dinner this evening."
print(message) 
message = f"Dear {guest_list[2]}, I am sorry I can't invite you to dinner this evening."
print(message) 

message = f"Dear {guest_reform[0]}, still your invented to dinner this evening."
print(message)
message = f"Dear {guest_list[1]}, still your invented to dinner this evening."
print(message)