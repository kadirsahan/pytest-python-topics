import pytest
import json
from tinydb import TinyDB

print("ok")

@pytest.fixture
def db():
    db = TinyDB("db.json")
    print("\n setup db")
    yield db
    db.truncate()
    print("\n teardown db")

def test_insert_one(db):
    db.insert({"name":"gnmn"})
    assert len(db.all()) ==1

def test_insert_multiple(db):
    db.insert_multiple([{"name":"gnmn"},{"name":"kfmr"}])
    assert len(db.all()) ==2