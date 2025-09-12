spanish = [ "perro", "gato", "playa"]
english = ["dog", "cat", "beach"]

for i in range(len(spanish)):
    print(spanish[i])
    print("What is this word in English?")
    answer = input()
    if answer == english[i]:
        print("You got it!")
    else:
        print(f"No, the right answer is {english[i]}")