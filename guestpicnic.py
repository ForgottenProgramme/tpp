all_guests = {
    'alice': {'apple': 5, 'biscuits': 3},
    'tom': {'drinks': 10, 'apple': 1},
    'kate': {'banana': 2, 'apple': 3, 'biscuits': 1},
    'abraham': {'drinks': 4}
}

stuff_list = ['apple', 'drinks', 'biscuits', 'banana', 'cake']

def all_stuff(guests: dict, item: str)->dict:
    number_brought=0
    for k,v in guests.items():
        number_brought+=v.get(item,0)
    
    return number_brought


def printstuff(stufflist: list, guestlist: list)-> None:
    for stuff_name in stufflist:
        print(f"{stuff_name}: {all_stuff(guestlist, stuff_name)}")

printstuff(stuff_list, all_guests)