import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")


import pytest
from src.db import Databse

# note, what ever comes before the 'yield' is the test initiation and all that comes after the yield is the test cleanup (post test processes)


@pytest.fixture
def db():
	"""Provides a fresh instanch of the Database class and cleans up after the test."""
	database = Databse()
	yield database # Provides the fixture instance
	database.data.clear() # Cleanup step (not needed for in-memory, but useful for real DBs)

def test_add_user(db):
	db.add_user(1, "Alice")
	assert db.get_user(1) == "Alice"


def test_add_duplicate_user(db):
	db.add_user(1, "Alice") 
	with pytest.raises(ValueError, match=r"User already exists"):
		db.add_user(1, "Bob")


def test_delete_user(db):
	db.add_user(2, "Bob")
	db.delete_user(2)
	assert db.get_user(2) is None


