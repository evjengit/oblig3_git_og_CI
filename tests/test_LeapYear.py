import pytest
from app.leapYear import isLeapYear

def test_leap_year_divisible_by_4_not_100():
    # Arrange
    year = 2008

    # Act
    result = isLeapYear(year)

    # Assert
    assert result == True

def test_leap_year_divisible_by_400():
    # Arrange
    year = 1600

    # Act
    result = isLeapYear(year)

    # Assert
    assert result == True

def test_non_leap_year_not_divisible_by_4():
    # Arrange
    year = 2001

    # Act
    result = isLeapYear(year)

    # Assert
    assert result == False

def test_non_leap_year_divisible_by_100_not_400():
    # Arrange
    year = 1900

    # Act
    result = isLeapYear(year)

    # Assert
    assert result == False