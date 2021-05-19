# tests/test_wikipedia.py
from saipyspark_testing101 import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]
