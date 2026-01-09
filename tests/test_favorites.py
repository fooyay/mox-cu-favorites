from src import favorites


def test_starting_values():
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    assert starting_number == 7
