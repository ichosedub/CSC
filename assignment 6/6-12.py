person0 = {"First_name" : "Jake", 
         "Last_name" : "Rowley",
         "Age" : "49",
         "City" : "New York",
         "Born" : "11/15/2004"}
person1 = {"First_name" : "Greg", 
          "Last_name" : "Heffley",
         "Age" : "14",
          "City" : "Los Angeles",
          "Born" : "05/25/2015"}
person2 = {"First_name" : "Kobe", 
         "Last_name" : "Bryant",
         "Age" : "41",
         "City" : "philadelphia",
         "Born" : "09/23/1978"}
people = [person0, person1, person2]

for person in people:
    print (f"\n{person['First_name']} {person['Last_name']}")
    print(f"Age: {person['Age']}")
    print(F"City: {person['City']}")
    print(F"Born: {person['Born']}")