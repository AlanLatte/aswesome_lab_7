import datetime

import models


def mock_trains() -> models.Trains:
    return models.Trains(
        [
            models.Train(
                number="1",
                station="Пушкина",
                time=datetime.datetime(year=2020, month=10, day=12, hour=12, minute=0),
            ),
            models.Train(
                number="6",
                station="Пушкина",
                time=datetime.datetime(year=2020, month=10, day=12, hour=12, minute=0),
            ),
            models.Train(
                number="2",
                station="Пушкина",
                time=datetime.datetime(year=2020, month=10, day=12, hour=13, minute=0),
            ),
            models.Train(
                number="3",
                station="Пушкина",
                time=datetime.datetime(year=2020, month=10, day=12, hour=14, minute=0),
            ),
            models.Train(
                number="4",
                station="Пушкина",
                time=datetime.datetime(year=2020, month=10, day=12, hour=16, minute=0),
            ),
            models.Train(
                number="5",
                station="Пушкина",
                time=datetime.datetime(year=2020, month=10, day=12, hour=15, minute=0),
            ),
        ]
    )
