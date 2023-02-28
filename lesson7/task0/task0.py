from os import path
	
file_base = "base.txt"
all_data = []
id = 0
	
if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass
	
	
def read_records():
    global all_data, id
	
    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        # else: print("empty data")
        return all_data


def show_all():
    read_records()
    if not all_data:
        print("Empty data")
    else:    
        print(*all_data, sep="\n")

def add_record():
    global id
    global contact
    global string
    contact = ['surname', 'name', 'second name', 'phone number']
    string = " "
    for i in contact:
        string = string + input(f" enter {i} ") + " "
    id += 1    
    with open(file_base, 'a', encoding='utf-8') as f:
        f.write(f"{id} {string}\n" )

def search():
    find = input("Enter contact to find: ")
    with open(file_base, 'r', encoding='utf-8') as f:
        for i in f:
            if find in i:
                print(i)
            else: 
                print("Not found.")  
    # 
    # search_data = exist_contact(0, input("Enter the search data: "))
    # if search_data:
    #     print(*search_data, sep="\n")
    # else:
    #     print("The data is not correct!")  

def remove():
    global all_data
    symbol = "\n"

    show_all()
    del_contact = input("Enter id contact for remove: ")
    for i in all_data:
        if del_contact in i:
            all_data = [k for k in all_data if k[0] != del_contact]
            with open(file_base, "w", encoding="utf-8") as f:
                f.write(f'{symbol.join(all_data)}\n')
                print("Record deleted.")
        else:
            print("contact not found")        

def edit():
    dict_edit = {"1": "surname","2": "name","3": "second name","4": "phone_number"}
    show_all()
    record_id = input("Enter id for edit: ")
    if exist_contact(record_id, ""):
        while True:
            print("\n Changing: ")
            change = input("1. surname\n"
                        "2. name\n"
                        "3. second name\n"
                        "4. phone number\n"
                        "5. exit\n")
            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(dict_edit[change])
                case "5":
                    return 0
                case _:
                    print("not found, repeat:")
    else:
        print("The data is not correct!")                

def change_contact(data_tuple):
    global all_data
    symbol = "\n"
    record_id, num_data, data = data_tuple
    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[(int(num_data))] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break
    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
        print("Record changed!\n")    

def data_collection(num):
    

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name second name":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer        

def exist_contact(record_id, data):

    if record_id:
        candidates = [i for i in all_data if record_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def main_menu():
    play = True
    while play:
        # read_records()
        answer = input("Phone book:\n"
                        "1. Show all records\n"
                        "2. Add a record\n"
                        "3. Search a record\n"
                        "4. Remove a record\n"
                        "5. Edit a record\n"
                        "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                search()
            case "4":
                remove()
            case "5":
                work = edit()
                if work:
                    change_contact(work)
            case "6":
                play = False        
            case _:
                print("Try again!\n")


main_menu()