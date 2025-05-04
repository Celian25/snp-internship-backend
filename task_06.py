class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(game: list) -> str:
    check_win = [["R", "S"], ["S", "P"], ["P", "R"]]
    if len(game) > 2:
        raise WrongNumberOfPlayersError
    if game[0][1] not in ["R", "P", "S"] or game[1][1] not in ["R", "P", "S"]:
        raise NoSuchStrategyError
    if game[0][1] == game[1][1]:
        return f"{game[0][0]}, {game[0][1]}"
    if [game[0][1], game[1][1]] in check_win:
        return f"{game[0][0]}, {game[0][1]}"
    return f"{game[1][0]}, {game[1][1]}"
