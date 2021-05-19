# src/saipyspark_testing101/wikipedia.py
import requests
import click

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

def random_page(language="en"):
    url = API_URL.format(language=language)
    try:
        with requests.get(url) as response:
          response.raise_for_status()
          return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
