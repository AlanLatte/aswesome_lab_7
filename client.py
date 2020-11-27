import datetime
from typing import List

import binarytree

import models
from exceptions import ExitFromAddMethod


class TrainClient:
    trains: models.Trains
    node: binarytree.Node

    def __init__(self, trains: models.Trains = None):
        self.trains = models.Trains() if trains is None else trains
        self._build()

    def add(self):
        """Добавляет к Trains экземпляр Train и билдит новое бинарное дерево.
        В случае возникновнеии если пользователь вышел из меню заполнения данных.
        Возвращаем кастомную ошибку."""
        try:
            train = self._add()
        except ExitFromAddMethod:
            raise ExitFromAddMethod
        self.trains.items.append(train)
        self._build()

    @staticmethod
    def _add() -> models.Train:
        """Приватная реализация метода add.
        В случае если во время заполнения данных пользователь нажмет на ctrl+Z,
        программа вернет кастомную ошибку ExitFromAddMethod."""
        try:
            number = input("Введите номер поезда: → ")
            station = input("Введите станцию: → ")
        except KeyboardInterrupt:
            raise ExitFromAddMethod
        try:
            time = datetime.datetime.strptime(
                input("Введите время YYYY-MM-DDThh:mm): → ").strip(),
                "%Y-%m-%dT%H:%M", )
        except ValueError or KeyboardInterrupt:
            raise ExitFromAddMethod
        else:
            return models.Train(number=number, station=station, time=time)

    def _build(self):
        """Пересобирает поезда и бинарное дерево."""
        self.trains.__post_init__()
        self.node = binarytree.build(self.trains.sorted_indexes_by_time)

    def node_stdout(self, show_index: bool = True) -> None:
        """Выводит в консоль бинарное дерево.
        :param show_index отвечает за дополнительный префикс индекса."""
        try:
            self.node.pprint(index=show_index)
        except AttributeError:
            print("Список поездов пуст.")

    def node_find_by_number(self) -> None:
        """Публичный поиск в бинарном дереве поезда, который удовлетворяет
        номеру."""
        number = input("Введите номер поезда: \t→ ").strip()
        try:
            train = self._node_find_by_number(number)
        except ValueError as e:
            print(e)
        except AttributeError:
            print("Список поездов пуст.")
        else:
            print(
                f"Номер: {train.number}\t"
                f"Станция: {train.station}\t"
                f"Время: {datetime.datetime.fromtimestamp(train.time)}"
            )

    def _node_find_by_number(self, number: str) -> models.Train:
        """Приватная реализация функции поиска по номеру.
        :param number: номер поезда.
        """
        try:
            nodes = self._node_preorder()
        except AttributeError as e:
            raise AttributeError(e)
        else:
            for node in nodes:
                try:
                    train = self.trains.train_by_index(node.value)
                except ValueError:
                    break
                if train.number == number:
                    return train
            raise ValueError(f"Поезд с номером {number} не найден.")

    def node_find_by_station(self) -> None:
        """Публичный поиск в бинарном дереве поезда, который удовлетворяет
        станции."""
        station = input("Введите название станции: \t→ ").strip().strip()
        try:
            train = self._node_find_by_station(station)
        except ValueError as e:
            print(e)
        except AttributeError:
            print("Список поездов пуст.")
        else:
            for find_train in train:
                print(
                    f"Номер: {find_train.number}\t"
                    f"Станция: {find_train.station}\t"
                    f"Время: {datetime.datetime.fromtimestamp(find_train.time)}"
                )

    def _node_find_by_station(self, station: str) -> List[models.Train]:
        """Приватная реализация функции поиска по имени станции.
        :param station: название станции.
        """
        trains = []
        try:
            nodes = self._node_preorder()
        except AttributeError as e:
            raise AttributeError(e)
        else:
            for node in nodes:
                try:
                    train = self.trains.train_by_index(node.value)
                except ValueError:
                    break
                if train.station == station:
                    trains.append(train)
            return trains

    def _node_preorder(self) -> List[binarytree.Node]:
        """Приватная реализция прямого обхода значений из бинанрного дерева."""
        try:
            return self.node.preorder
        except AttributeError:
            raise AttributeError(
                "Невозможно получить значения прямого обхода. Причина: нода пуста."
            )
