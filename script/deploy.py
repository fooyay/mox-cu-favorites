from src import favorites  # type: ignore
from moccasin.boa_tools import VyperContract  # type: ignore


def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Favorites deployed to {favorites_contract.address} with starting number {starting_number}")

    favorites_contract.store(42)
    updated_number: int = favorites_contract.retrieve()
    print(f"Favorites updated number to {updated_number}")

    return favorites_contract


def moccasin_main() -> VyperContract:
    return deploy_favorites()
