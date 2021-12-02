import secrets
import json


class Placement:

    def __init__(self, hosts: list):
        self.hosts = dict([(host, None) for host in hosts])

    def place(self, users: list):
        for user in users:
            host = secrets.choice(list(self.hosts))
            while (self.hosts[host] != None):
                host = secrets.choice(list(self.hosts))
            self.hosts[host] = user

    def to_file(self, filename: str):
        f = open(filename, "w")
        for host, user in self.hosts.items():
            if user is not None:
                f.write(str(host) + ": " + str(user) + "\n")
        f.close()

    def to_json_file(self, filename: str):
        j = json.dumps(self.hosts, indent=4)
        f = open(filename, "w")
        f.write(j)
        f.close()
