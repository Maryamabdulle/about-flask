"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()
    
    for line in open(filename):
        line = line.rstrip()
        villager_data = line.split('|')
        species.add(villager_data[1])

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    species_name = []
    search_string = search_string.capitalize()  

    for line in open(filename):
        line = line.rstrip()
        villager_data = line.split('|')

        if search_string != "All":
            if villager_data[1] == search_string:
                species_name.append((villager_data[1],villager_data[0]))
            else: continue
        else: species_name.append((villager_data[1],villager_data[0]))
    
    species_name.sort()

    for tup in species_name:
        villagers.append(tup[1])

    # TODO: replace this with your code

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
     
    villagers = [[],[],[],[],[],[]]
    hobby_name = []

    for line in open(filename):
        line = line.rstrip()
        villager_data = line.split('|')
        hobby_name.append((villager_data[0],villager_data[3]))
    
    hobby_name.sort()

    for tup in hobby_name:
        if tup[1] == 'Fitness':
            villagers[0].append(tup[0])
        elif tup[1] == 'Nature':
            villagers[1].append(tup[0])
        elif tup[1] == 'Education':
            villagers[2].append(tup[0])
        elif tup[1] == 'Music':
            villagers[3].append(tup[0])
        elif tup[1] == 'Fashion':
            villagers[4].append(tup[0])
        elif tup[1] == 'Play':
            villagers[5].append(tup[0])

    return villagers


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    for line in open(filename):
        line = line.rstrip()
        tup = tuple(line.split('|'))
        all_data.append(tup)

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    villager_name = villager_name.capitalize()

    for line in open(filename):
        line = line.rstrip()
        villager_data = line.split('|') #[name, species, ...]
        if villager_data[0] == villager_name or villager_name == 'Any':
            return villager_data[-1]
    
    # print("Villager not found.") #optional
    return None

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    villagers = set()
    villager_name = villager_name.capitalize()
    personality = None

    for line in open(filename): #determine personality
        line = line.rstrip()
        villager_data = line.split('|')
        if villager_data[0] == villager_name:
            personality = villager_data[2]
            break
        
    if personality == None:
        return villagers                      #handles exception not found

    for line in open(filename):
        line = line.rstrip()
        villager_data = line.split('|')
        if villager_data[2] == personality:
            villagers.add(villager_data[0])

    return villagers