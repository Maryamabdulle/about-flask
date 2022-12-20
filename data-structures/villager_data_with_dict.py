"""Functions to parse a file containing villager data.
name|species|personality|hobby|motto
"""
#make a dictionary of villager_data by villager name:
villager_data = {}
for line in open("villagers.csv"):
    line = line.rstrip()
    v_list = line.split('|')
    villager_data[v_list[0]] = {
        'species': v_list[1],
        'personality': v_list[2],
        'hobby': v_list[3],
        'motto': v_list[4]}

#tally species in a dictionary
species = {}
for name in villager_data.keys():
    spec = villager_data[name]['species']
    species[spec] = species.get(spec,0) + 1

#tally personalities in a dictionary
personalities = {}
for name in villager_data.keys():
    personality = villager_data[name]['personality']
    personalities[personality] = personalities.get(personality,0) + 1


def get_villagers_by_species(species="All", villager_data = villager_data):
    """Return a list of villagers' names by species.
    Arguments:
        - species (str): optional, the name of a species
        - villager_data (dict): optional, a dictionary of villagers
    Return:
        - list[str]: a list of names
    """

    villagers = []
    species = species.capitalize()  #handle cat/Cat/CAT as Cat

    for name in villager_data.keys():
        if species != "All":
            if villager_data[name]['species'] == species:
                villagers.append(name)
        else: villagers.append(name)
    
    return sorted(villagers)


def all_names_by_hobby(villager_data = villager_data):
    """Return a list of lists containing villagers' names, grouped by hobby.
    Arguments:
        - villager_data (dict): optional, a dictionary of villagers
    Return:
        - list[list[str]]: a list of lists containing names
    """

    
    by_hobby = [[],[],[],[],[],[]]
    hobby_idx = {
        'Fitness': 0,
        'Nature': 1,
        'Education': 2,
        'Music': 3,
        'Fashion': 4,
        'Play': 5
    }

    for name in villager_data.keys():
        by_hobby[hobby_idx[villager_data[name]['hobby']]].append(name)

    return by_hobby


def all_data(villager_data = villager_data):
    """Return all the data in a file.
    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).
    Arguments:
        - villager_data (dict): optional, a dictionary of villagers
    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """


    all_data = []

    for name in villager_data.keys():
        villagers_info = [name]
        villagers_info.extend(list(villager_data[name].values()))
        all_data.append(tuple(villagers_info))

    return all_data


def find_motto(villager_name, villager_data = villager_data):
    """Return the villager's motto.
    Return None if you're not able to find a villager with the
    given name.
    Arguments:
        - villager_name (str): a villager's name
        - villager_data (dict): optional, a dictionary of villagers
    Return:
        - str: the villager's motto or None
    """

    villager_name = villager_name.capitalize()

    if villager_name in villager_data.keys():
        return villager_data[villager_name]['motto']
    else: return None


def find_likeminded_villagers(villager_name, villager_data = villager_data):
    """Return a set of villagers with the same personality as the given villager.
    Arguments:
        - villager_name (str): a villager's name
        - villager_data (dict): optional, a dictionary of villagers
    
    Return:
        - set[str]: a set of names
    For example:
        >>> find_likeminded_villagers('Wendy')
        {'Bella', ..., 'Carmen'}
    """

    villager_name = villager_name.capitalize()
    likeminded = set()
    personality = villager_data[villager_name]['personality']

    for name in villager_data.keys():
        if villager_data[name]['personality'] == personality:
            likeminded.add(name)

    return likeminded