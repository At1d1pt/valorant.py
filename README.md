# valorant.py
A python wrapper for [valorant-api](https://valorant-api.com/)

## Installation
This project is not complete yet and is not available on pip for now. You can download this package through git and pip.

```
pip install git+https://github.com/At1d1pt/valorant.py.git
```

## Example
- Fetching an agent by it's display name
```py
import valorant
client = valorant.Client()
agent = client.agent('jett')
print(agent.name)
```