# python-antminer

A Pythonic interface to the Antminer API.

# Example

```python
from antminer.base import BaseClient

client = BaseClient('192.168.0.25') # Change to IP address of your miner.
client.connect()
print client.version()
```
