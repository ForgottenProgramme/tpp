birthdays = {'mahe': '1 april', 'john': '2 april', 'molly': '5 august', 'timonthy': '13 june'}

while True:
    print("Enter a name: (black to quit).")
    name= input()
    if name == '':
        break

    if birthdays.get(name):
        print(f"{name}'s birthday is on {birthdays[name]}.")
    else:
        print(f"Couldn't find {name}'s birthday in the database. When is their birthday?")
        new_bd = input()
        birthdays[name]=new_bd
        print("birthday added to database.")
        