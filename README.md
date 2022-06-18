# CHANGE DETECTOR

```
:'######::'##::::'##::::'###::::'##::: ##::'######:::'########:
'##... ##: ##:::: ##:::'## ##::: ###:: ##:'##... ##:: ##.....::
 ##:::..:: ##:::: ##::'##:. ##:: ####: ##: ##:::..::: ##:::::::
 ##::::::: #########:'##:::. ##: ## ## ##: ##::'####: ######:::
 ##::::::: ##.... ##: #########: ##. ####: ##::: ##:: ##...::::
 ##::: ##: ##:::: ##: ##.... ##: ##:. ###: ##::: ##:: ##:::::::
. ######:: ##:::: ##: ##:::: ##: ##::. ##:. ######::: ########:
:......:::..:::::..::..:::::..::..::::..:::......::::........::
'########::'########:'########:'########::'######::'########:
 ##.... ##: ##.....::... ##..:: ##.....::'##... ##:... ##..::
 ##:::: ##: ##:::::::::: ##:::: ##::::::: ##:::..::::: ##::::
 ##:::: ##: ######:::::: ##:::: ######::: ##:::::::::: ##::::
 ##:::: ##: ##...::::::: ##:::: ##...:::: ##:::::::::: ##::::
 ##:::: ##: ##:::::::::: ##:::: ##::::::: ##::: ##:::: ##::::
 ########:: ########:::: ##:::: ########:. ######::::: ##::::
........:::........:::::..:::::........:::......::::::..:::::
```

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Pypi](https://img.shields.io/badge/VERSION-0.0.1-blue?style=for-the-badge&logo=pypi)](https://pypi.org/project/wts/)

## CHANGE DETECTOR

Installation

```bash
pip install changedetector
```

Change detector is a tool that can be used to detect changes in your code.
It works with a simple syntax.

```python
from changedetector import detectchange
detectchange.activate()
```
It detects changes in your root directory. And executes the scripts chosen
when the script is executed.

It can be used to detect changes in python, ruby, c++ files.

You can execute the script on a second `Thread`.
