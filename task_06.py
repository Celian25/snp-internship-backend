class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(game: list) -> list:
    check_win = [["R", "S"], ["S", "P"], ["P", "R"]]
    if len(game) > 2:
        raise WrongNumberOfPlayersError
    if game[0][1] not in ["R", "P", "S"] or game[1][1] not in ["R", "P", "S"]:
        raise NoSuchStrategyError
    if game[0][1] == game[1][1]:
        return game[0]
    if [game[0][1], game[1][1]] in check_win:
        return game[0]
    return game[1]


print(rps_game_winner([["player1", "P"], ["player2", "S"]]))
