import socket
from antminer.constants import DEFAULT_PORT
from antminer.base import BaseClient


class LocalMiners(object):
    TIMEOUT = 0.05

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        self.ip_address = sock.getsockname()[0]
        sock.close()
        self.network = '{}.'.format('.'.join(self.ip_address.split('.')[:3]))
        self._miner_index = 0
        self._miners = None

    def _is_up(self, addr):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.TIMEOUT)
        if not sock.connect_ex((addr, DEFAULT_PORT)):
            is_up = True
        else:
            is_up = False

        sock.close()
        return is_up

    def discover(self):
        found = []
        for ip in xrange(1, 256):
            addr = '{network}{ip}'.format(network=self.network, ip=str(ip))
            if self._is_up(addr):
                found.append(BaseClient(addr))

        return found

    def __iter__(self):
        return self

    def next(self):
        if self._miners is None:
            self._miners = self.discover()

        if self._miner_index >= len(self._miners):
            raise StopIteration
        else:
            self._miner_index += 1
            return self._miners[(self._miner_index - 1)]

    def seek(self, offset):
        self._miner_index = offset

    def flush(self):
        self._miner_index = 0
        self._miners = None
