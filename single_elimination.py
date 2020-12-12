class FindMatches:
    def __init__(self,teams):
        self.teams = teams
    
    def find_total_match(self):
        return len(self.teams) - 1
    
    def total_teams(self):
        return len(self.teams)

    @staticmethod
    def power_of_two(target):
        if target > 1:
            for i in range(1, int(target)):
                if (2 ** i >= target):
                    return 2 ** i
        else:
            return 1

    @staticmethod
    def power_of_two_list(target):
        closest_list = []
        if target > 1:
            for i in range(1, int(target)):
                closest_list.append(2 ** i)
                if (2 ** i >= target):
                    return closest_list[:-1]
        else:
            closest_list.append(1)
            return closest_list

teams = range(1,15)

single_elem = FindMatches(teams)


print("Total Teams :",single_elem.total_teams())
total_teams = single_elem.total_teams()
closest_power = single_elem.power_of_two(total_teams)
print("Closest 2 power : ", closest_power)

byes = closest_power - total_teams

print("Byes : ", byes)

power_of_two_list = sorted(single_elem.power_of_two_list(total_teams),reverse=True)

print("List of power of two :", power_of_two_list)

formated_match_list = []
for i,j in enumerate(power_of_two_list):
    if i == 0:
        formated_match_list.append(j-byes)
    else:
        formated_match_list.append(j)
print("Formatted list :", formated_match_list)
