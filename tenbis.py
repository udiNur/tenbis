#!/usr/bin/env python
import os
from dataclasses import dataclass
from os.path import expanduser
from typing import Optional

import requests
from bs4 import BeautifulSoup

TENBIS_COOKIE_FN = ".tenbis_cli.txt"
COOKIE_FILE_PASSABLE_LOCATIONS = [
    TENBIS_COOKIE_FN,
    os.path.join(expanduser("~"), TENBIS_COOKIE_FN)
]


def parse_cookie_file(path: str) -> Optional[str]:
    if os.path.isfile(path):
        with open(path) as f:
            return f.read().strip()


def get_cookie():
    cookie = None

    for fp in COOKIE_FILE_PASSABLE_LOCATIONS:
        cookie = parse_cookie_file(fp)
        if cookie:
            print("Uses the credential file on:", fp)
            break

    if cookie is None:
        raise Exception(
            f"The cookie file is not found in the following paths: {', '.join(COOKIE_FILE_PASSABLE_LOCATIONS)},"
            f" please add the file and try again")

    return cookie


HEADERS = {
    'authority': 'www.10bis.co.il',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': None

}


@dataclass
class BalanceTable:
    monthly_frame: float
    monthly_balance: float
    monthly_used: float


def get_user_report(headers_: dict):
    response = requests.get('https://www.10bis.co.il/Account/UserReport', headers=headers_)
    return BeautifulSoup(response.text, "html.parser")


def parse_balances_table(b: BeautifulSoup) -> BalanceTable:
    balances_table = b.find('table', {"class": "userReportDataTbl"})
    if balances_table is None:
        raise Exception("Something wrong with the cookie (expired, or not valid),"
                        " use the debugger to inspect the 'get response' HTML data")
    data = balances_table.find_all("th")

    return BalanceTable(monthly_frame=data[6].text.strip(),
                        monthly_balance=data[2].text.strip(),
                        monthly_used=data[4].text.strip())


if __name__ == '__main__':
    headers = dict(HEADERS)
    headers["cookie"] = get_cookie()

    b = get_user_report(headers)
    balance_table = parse_balances_table(b)
    print(f"""
Welcome to TenBis panel!
your monthly frame is {balance_table.monthly_used} / {balance_table.monthly_frame} 
the balance is {balance_table.monthly_balance}""")

# TODO the daily calc for the poor ones
