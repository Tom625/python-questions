def top_k_teams(batsmen: list, k: int) -> list:
    '''
    Given a list of dictionaries with batsman names, runs, and team names,
    Create a list with the top k teams in terms of total runs 
    starting from the highest to the lowest runs.

    Assume no two teams have the same number of runs.

    Arguments:
    batsmen: list of dict - list containing dictionaries with keys 'name', 'runs', and 'team'
    k: int - number of top teams to return

    Return:
    list - top k teams in terms of total runs
    '''

    team_runs = {}

    for batsman in batsmen:
        if batsman['team'] not in team_runs:
            team_runs[batsman['team']] = 0
        team_runs[batsman['team']] += batsman['runs']

    return sorted(team_runs, key=team_runs.get, reverse=True)[:k]
