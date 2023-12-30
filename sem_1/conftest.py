import pytest


@pytest.fixture
def badword():
    return 'Масква'


@pytest.fixture
def goodword():
    return 'Москва'