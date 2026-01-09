from script.deploy import deploy_favorites


def test_starting_values():
    favorites_contract = deploy_favorites()
    starting_number = favorites_contract.retrieve()
    assert 42 == starting_number
