import datetime

import models


def mock_trains() -> models.Trains:
    return models.Trains(
        [
            models.Train(
                number="1",
                station="Кузьминки",
                time=datetime.datetime(year=2020, month=10, day=12, hour=9, minute=30),
            ),
            models.Train(
                number="6",
                station="Кузьминки",
                time=datetime.datetime(year=2020, month=10, day=12, hour=10, minute=45),
            ),
            models.Train(
                number="2",
                station="Одинцово",
                time=datetime.datetime(year=2020, month=10, day=12, hour=12, minute=20),
            ),
            models.Train(
                number="3",
                station="Сколково",
                time=datetime.datetime(year=2020, month=10, day=12, hour=9, minute=0),
            ),
            models.Train(
                number="4",
                station="Рабочий посёлок",
                time=datetime.datetime(year=2020, month=10, day=12, hour=9, minute=20),
            ),
            models.Train(
                number="5",
                station="Одинцово",
                time=datetime.datetime(year=2020, month=10, day=12, hour=13, minute=0),
            ),
        ]
    )
