# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    teams = OrderedDict(sortedTeams)
    print(teams)

    # TODO: create an ordered dictionary of the teams
    tm, wl = teams.popitem(False)
    print("Teams:", tm, wl)

    # TODO: Use popitem to remove the top item
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # TODO: What are next the top 4 teams?
    a = OrderedDict({"a" : 1, "b" : 2, "c": 3})
    b = ({"a" : 1, "c": 3, "b": 2 })
    print("Equality test: ", a == b)

    # TODO: test for equality

if __name__ == "__main__":
    main()
