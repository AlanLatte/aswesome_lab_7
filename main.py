from argparse import ArgumentParser

import mocks
from client import TrainClient
from exceptions import ExitFromAddMethod


def actions(client: TrainClient, param: str):
    if "print" == param:
        client.node_stdout()
    elif "find_by_number" == param:
        client.node_find_by_number()
    elif "add" == param:
        try:
            client.add()
        except ExitFromAddMethod:
            raise ExitFromAddMethod
    elif "find_by_station" == param:
        client.node_find_by_station()
    elif "exit" == param:
        raise KeyboardInterrupt()


def run(client: TrainClient):
    while True:
        try:
            actions(
                client,
                param=input(
                    "ACTIONS:\n"
                    "\tprint;"
                    "\tfind_by_number;"
                    "\tadd;"
                    "\tfind_by_station;"
                    "\texit;"
                    "\n\t→ "
                ),
            )
            print("-" * 15)
        except ExitFromAddMethod:
            continue
        except KeyboardInterrupt:
            break


def cli():
    """Чтение параметров из консоли."""
    parser = ArgumentParser(description="Apply mock values")
    parser.add_argument(
        "--mock-values",
        action="store_true",
        help="In program will implements mocked values",
    )
    args = parser.parse_args()

    trains = None
    if args.mock_values is True:
        trains = mocks.mock_trains()

    client = TrainClient(trains)
    run(client)


if __name__ == "__main__":
    cli()
