string = input("Enter your CSV file as a string: ")

string = string.replace(";", ",")
print(string)


def dict_maker(x):
    list_of_dicts = []
    x = x.splitlines()
    keys = x[0]  
    items = x[ 1:len(x)]
    keys_splitted = keys.split(",")
    list_of_dicts = [dict() for i in range(len(x)-1)]

    for i  in range(len(items)):
        values = items[i].split(",")
        for y in range(len(keys_splitted)):
            list_of_dicts[i][keys_splitted[y]] = [values[y]]

    new_list_of_dicts = []

    for d in list_of_dicts:
        new_dict = {}
        for key, value in d.items():
            new_dict[key.strip()] = str(value).strip("['] ")
        new_list_of_dicts.append(new_dict)

    return new_list_of_dicts
