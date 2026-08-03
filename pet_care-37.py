# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: PetCare
import unittest


def test_pet_care():
    """Unit tests for PetCare."""
    from petcare import Pet, log_feeding, log_health, log_walk, add_note

    # Test feeding
    assert log_feeding('cat', 'fish') is None
    assert log_feeding('dog', 'meat') is None

    # Test health
    assert log_health('cat', 'healthy') is None
    assert log_health('dog', 'sick') is None

    # Test walk
    assert log_walk('cat') is None
    assert log_walk('dog') is None

    # Test note
    assert add_note('pet1', 'good pet') is None


if __name__ == '__main__':
    test_pet_care()
