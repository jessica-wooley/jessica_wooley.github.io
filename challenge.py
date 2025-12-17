"""
This is my Data Analysis Project where I answered the question "How many Baseball Players 
who were at bat more than 10 times hit the ball more than 5 times?" At first I wanted to see what 
players at bat hit the ball but I fixed the question ask more about players who have hit more than once.
"""
import csv

#Function 1: get_csv_data (csv_filename)
"""
In this function it imports the .csv file in order for it to turn
into a python data type. Where it returns the list of dictionaries
which is list_of_dicts.
"""
def get_csv_data(csv_filename):
    list_of_dicts = []
    with open(csv_filename, "r") as f:
        contents = csv.DictReader(f)
        for row in contents:
            list_of_dicts.append(row)
    return list_of_dicts

#Function 2: get_players_at_bat(dataset)
"""
In this function it goes through the dataset of the csv file
in order to find when "AB" = at-bat is greater than 10, if it is then
it will append these rows to the list called players_at_bat. Then it returns
players_at_bat.
"""
def get_players_at_bat(dataset):
    players_at_bat = []
    for row in dataset:
        if int(row["AB"])>10:
            players_at_bat.append(row)
    return players_at_bat

#Function 3: get_players_hit(players_at_bat)
"""
In this function it uses the return from function 2 called "players_at_bat".
In which the function goes through the list ("players_at_bat" where at-bat is greater than 10)
and if "H" = hits is greater than 5 it will append that to the list called players_hit,
which represents the number of players that were at-bat more than 10 times and hit more than
5 times. Where it returns this list (players_hit)
"""
def get_players_hit(players_at_bat):
    players_hit = []
    for row in players_at_bat:
        if int(row["H"])> 5:
            players_hit.append(row)
    return players_hit

#Function 4: hit_per_player(players_at_bat)
"""
In this function it similarly uses the return from function 2(player_at_bat)
in which it creates a dictionary called hit_dict where for every row it will collect the 
player ids of those who were at bat more than 10 times and hit the ball more than 5 times. In which it
will return hit_dict.
"""
def hit_per_player(players_at_bat):
    hit_dict = {}
    for row in players_at_bat:
        player_id = row["playerID"]
        hits = int(row["H"])
        hit_dict[player_id] = hits
    return hit_dict

# Function 5: write_csv(txtname, players_hit)
"""
In this function it will create a new txt (text) file that will display the player ids of 
players who were at bat more than 10 times and hit the ball more than 5 times. 
"""
def write_csv(filename, players_hit):
    with open(filename, "w") as f:
        f.write("Players that were at-bat more than 10 times and hit more than 5 times: \n")
        for row in players_hit:
            player_id = row["playerID"]
            hits= row["H"]
            f.write(f"PlayerID: {player_id} : Hits: {hits}\n")

#Main Body
csv_data= get_csv_data("Batting.csv")
players_at_bat = get_players_at_bat(csv_data)
players_hit = get_players_hit(players_at_bat)
hit_dict = hit_per_player(players_hit)
write_csv("results.txt", players_hit)

