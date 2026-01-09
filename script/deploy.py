from src import favorites


def deploy():
    favvorites_contract = favorites.deploy()
    starting_number = favvorites_contract.retrieve()
    print(f"Favorites deployed to {favvorites_contract.address} with starting number {starting_number}")


def moccasin_main():
    deploy()
