# Telnet Executioner with API Manager
Executes Telnet commands based on API responses

## Installation

Download and run main.py, Change the Host-IP Variables

```bash
API >
11-  host = "0.0.0.0"
12-  port = 80

Telnet Server >
38   self.host = "CHANGEME"
39   self.port = 23
```


## Usage

```python
GET Request > http://0.0.0.0?host="70.70.70.75"&port=80&username="NoelP"&password="Password"&time=60
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Disclaimer
```python
This repository is for academic purposes, the use of this software is your responsibility.
```
## License
[GNU v3](https://www.gnu.org/licenses/gpl-3.0.nl.html)
