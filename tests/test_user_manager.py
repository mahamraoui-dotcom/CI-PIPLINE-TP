import pytest
from app.user_manager import UserManager


def test_add_user():
    manager = UserManager()
    manager.add_user("Manar")
    assert manager.count_users() == 1


def test_add_existing_user():
    manager = UserManager()
    manager.add_user("Manar")
    with pytest.raises(ValueError):
        manager.add_user("Manar")


def test_remove_user():
    manager = UserManager()
    manager.add_user("Hiba")
    manager.remove_user("Hiba")
    assert manager.count_users() == 0


def test_remove_unknown_users():
    manager = UserManager()
    with pytest.raises(ValueError):
        manager.remove_user("Test")
