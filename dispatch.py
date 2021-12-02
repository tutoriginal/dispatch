#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv(".env")

from dispatch.api import get_subscribed
from dispatch.clusters import get_hosts, get_hosts
from dispatch.Placement import Placement

pisciners, err = get_subscribed("c-piscine-final-exam")
if err is not None:
    os._exit(1)
hosts = get_hosts("fu")

placement = Placement(hosts)
placement.place(pisciners)

placement.to_json_file("placement.json")
placement.to_file("placement.txt")