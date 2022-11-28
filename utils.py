import json
import re
import requests

HEADERS = {"Content-type": "application/json; charset=utf-8"}


def load_file_config():
    """

    :return:
    """
    with open("config.json", 'r') as file_:
        data = json.load(file_)
    return data


def clear_url(url: str) -> str:
    """

    :param url:
    :return:
    """
    segments = url.split('/')
    for segment in segments:
        if re.search('\\d', segment):
            url = url.replace(segment, "?")
    return url


def validate_grant(endpoint: str, method: str, id_rol: int) -> bool:
    """

    :param endpoint:
    :param method:
    :param id_rol:
    :return:
    """
    data_config = load_file_config()
    url = data_config.get('url-backend-security') + f'/rol/validate/{id_rol}'
    print(url)


    body = {
        "url": endpoint,
        "method": method
    }
    response = requests.get(url, headers=HEADERS, json=body)
    print(response)
    print(response.status_code)
    has_grant = False
    try:
        if response.status_code == 200:
            has_grant = True
    except Exception as e:
        print(e)
    return has_grant




