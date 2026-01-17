string1 = """product_id, product_name, product_price
1, doom, 10
2, cake, 25"""

string2 = """team_id, team_name, team_tsales
3, Hello United, 14
5, FootballFC, 20
7, Team, 3"""

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


print(dict_maker(string1))
#print(dict_maker(string2))
