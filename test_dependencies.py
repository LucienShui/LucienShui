"""Simple test to verify that updated dependencies work correctly together."""

import numpy as np
import requests
import pytest


def test_numpy_works():
    """Test that numpy 2.x works correctly."""
    array = np.array([1, 2, 3, 4, 5])
    assert array.sum() == 15
    assert np.__version__.startswith('2.3')


def test_requests_works():
    """Test that requests works correctly."""
    # Test that requests module loads and has expected attributes
    assert hasattr(requests, 'get')
    assert hasattr(requests, 'post')
    assert requests.__version__.startswith('2.32')


def test_pytest_works():
    """Test that pytest 8.x works correctly."""
    assert pytest.__version__.startswith('8.4')


if __name__ == "__main__":
    test_numpy_works()
    test_requests_works()
    test_pytest_works()
    print("All dependency tests passed!")