# python-antminer

A Pythonic interface to the Antminer API.

# Examples

## Get Version Information

Connect to a miner and get version information. Where appropriate, an instance of [`semantic_version.Version`](https://pypi.python.org/pypi/semantic_version/) is returned.

```python
from antminer.base import BaseClient

client = BaseClient('192.168.0.25') # Change to IP address of your miner.
client.connect()
print client.version()
```

## Discover Miners on the LAN

The `LocalMiners` class is an iterator that looks for miners on the LAN. A `BaseClient` is returned for each miner discovered.

```python
from antminer.discover import LocalMiners

network = LocalMiners()
for miner in network:
    print miner.version()
```
