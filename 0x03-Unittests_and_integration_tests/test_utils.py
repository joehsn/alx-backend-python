#!/usr/bin/env python3
"""
0. Parameterize a unit test task's module.
"""
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for test cases.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),

    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        access_nested_map function tests.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),

    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """
        access_nested_map exception raising tests.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    get_json function tests class.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),

    ])
    def test_get_json(self, test_url, test_payload):
        """
        Tests get_json's output.
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    memoize function tests class.
    """

    def test_memoize(self):
        """

        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

            with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,

            ) as memo_fxn:
                test_class = TestClass()
                self.assertEqual(test_class.a_property(), 42)
                self.assertEqual(test_class.a_property(), 42)
                memo_fxn.assert_called_once()
