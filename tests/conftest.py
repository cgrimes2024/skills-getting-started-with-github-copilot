import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_db

original_activities = copy.deepcopy(activities_db)


@pytest.fixture(autouse=True)
def reset_activities():
    yield
    activities_db.clear()
    activities_db.update(copy.deepcopy(original_activities))


@pytest.fixture
def client():
    return TestClient(app)
