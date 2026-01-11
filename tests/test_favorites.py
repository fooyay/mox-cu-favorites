def test_starting_values(favorites_contract):
    starting_number = favorites_contract.retrieve()
    assert 42 == starting_number


def test_updating_values(favorites_contract):
    favorites_contract.store(100)
    updated_number = favorites_contract.retrieve()
    assert 100 == updated_number


def test_can_add_people(favorites_contract):
    # arrange
    new_person = "Alice"
    new_favorite_number = 15

    # act
    favorites_contract.add_person(new_person, new_favorite_number)

    # assert
    (number, name) = favorites_contract.list_of_people(0)
    assert new_person == name
    assert new_favorite_number == number
