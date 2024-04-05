# Python Logger Utility
Colorcode your logs to easily identify them during runtime

### Setup
Change the colors in the logger.py file if needed  
Add new properties to LOG_COLORS to get more log levels  
Otherwise no setup is needed, just import it and you are good to go!

### Usage
```python
from logger import Logger

logger = Logger("YOUR_MODULE_OR_CLASS_NAME_HERE").logger

# default/ predefined functions
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

### Example
![image](https://github.com/SchloesserJonas/python-logger-utility/assets/87974711/9a944b10-6f93-43ee-b136-f0753ee1f2d1)  
<sup>*Example with the default color configuration*</sup>
