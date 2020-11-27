from argparse import ArgumentParser
from typing import Callable

import mocks
import models
from client import TrainClient
import exceptions


class Worker:
    client: TrainClient

    def __init__(self, trains: models.Trains = None):
        self.client = TrainClient(trains)

    def actions(self, param: str) -> Callable[[], None]:
        """Возвращается объект функции."""
        try:
            return {
                "print": self.stdout,
                "find_by_number": self.find_by_number,
                "add": self.add_train,
                "find_by_station": self.find_by_station,
                "exit": self.exit,
            }[param]
        except KeyError:
            raise exceptions.UnknownCommand

    def handle_action(self) -> None:
        try:
            return self.actions(
                param=input(
                    "ACTIONS:\n"
                    "\tprint;"
                    "\tfind_by_number;"
                    "\tadd;"
                    "\tfind_by_station;"
                    "\texit;"
                    "\n\t→ "
                ),
            )()
        except exceptions.UnknownCommand:
            raise exceptions.UnknownCommand

    def exit(self) -> None:
        raise KeyboardInterrupt()

    def find_by_station(self) -> None:
        self.client.node_find_by_station()

    def add_train(self) -> None:
        try:
            self.client.add()
        except exceptions.ExitFromAddMethod:
            raise exceptions.ExitFromAddMethod

    def find_by_number(self) -> None:
        self.client.node_find_by_number()

    def stdout(self) -> None:
        self.client.node_stdout()

    def run(self):
        while True:
            try:
                self.handle_action()
                print("-" * 15)
            except exceptions.ExitFromAddMethod or exceptions.UnknownCommand:
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

    Worker(trains).run()


if __name__ == "__main__":
    cli()
