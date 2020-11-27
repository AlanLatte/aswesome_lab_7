import datetime
from dataclasses import dataclass, field
from typing import Union, List


@dataclass
class Train:
    """Train структура которая служит для хранения данных поездов.
    time - Время отправления. Параметр по умолчанию -- сейчас."""

    number: str
    station: str
    _index: int = field(default=None)
    time: Union[datetime.datetime, int] = field(default=datetime.datetime.now())

    def __post_init__(self):
        """Мы используем timestamp в качестве отчеста времени. В случае если мы передали
        объект datetime, мы преобразуем его."""
        if isinstance(self.time, int):
            self.time = self.time
        elif isinstance(self.time, datetime.datetime):
            self.time = int(self.time.timestamp())

        if self._index:
            raise ValueError("Запрещенно передавать _index.")

    @property
    def index(self):
        return self._index


@dataclass
class Trains:
    """Trains служит для агрегрирования экземпляров Train.
    items -- кортеж состоящий из уникальных значений. По умочанию - пустой
    indexes -- список проиндексированный список Train"""

    items: List[Train] = field(default_factory=list)

    def __post_init__(self):
        numbers: List[str] = []
        for index, value in enumerate(self.items):
            numbers.append(value.number)
            value._index = index
        if len(numbers) > len(set(numbers)):
            raise ValueError("Номера поездов не должны повторяться.")

    @property
    def times(self) -> List[int]:
        """Возвращает кортеж из timestamp."""
        return [item.time for item in self.items]

    @property
    def indexes(self) -> List[int]:
        """Возвращает все индексы кортежа."""
        return [item.index for item in self.items]

    @property
    def sorted_indexes_by_time(self) -> List[int]:
        """Возвращает кортеж из индексов отсортированный по времени."""
        import operator

        return [
            item.index for item in sorted(self.items, key=operator.attrgetter("time"))
        ]

    def train_by_index(self, index: int) -> Train:
        """Возвращает Train из кортежа согласно индексу."""
        try:
            return self.items[index]
        except IndexError:
            raise ValueError(f"Поезд с индексом {index} не найден.")
