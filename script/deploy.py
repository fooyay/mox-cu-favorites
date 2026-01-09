from src import favorites


def deploy_favorites():
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Favorites deployed to {favorites_contract.address} with starting number {starting_number}")

    favorites_contract.store(42)
    updated_number = favorites_contract.retrieve()
    print(f"Favorites updated number to {updated_number}")

    return favorites_contract


def moccasin_main():
    deploy_favorites()
