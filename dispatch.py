#!/usr/bin/env python3

from dispatch.Placement import Placement
from dispatch.clusters import get_hosts, get_hosts
from dispatch.api import get_subscribed
import os
from dotenv import load_dotenv

load_dotenv(".env")


pisciners, err = get_subscribed("c-piscine-final-exam")
if err is not None:
    os._exit(1)
hosts = get_hosts("fu")

placement = Placement(hosts)
placement.place(pisciners)

placement.to_json_file("placement.json")
placement.to_file("placement.txt")
