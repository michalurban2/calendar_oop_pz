from datetime import datetime, timedelta

import pytest

from event import Event


@pytest.fixture
def event():
    return Event(1, datetime.now().replace(microsecond=0) + timedelta(hours=3), 20, '', '', '')
