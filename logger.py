import logging


class Logger:
    def __init__(self, module='Log):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)

        # Define your colors here
        self.LOG_COLORS = {
            logging.DEBUG: "\033[37m",  # gray
            logging.INFO: "\033[97m",  # White
            logging.WARNING: "\033[33m",  # Yellow
            logging.ERROR: "\033[31m",  # Red
            logging.CRITICAL: "\x1b[31;1m"  # Bold red
        }

        for level, color in self.LOG_COLORS.items():
            setattr(self.logger, logging.getLevelName(level).lower(),
                    self._colorize(getattr(self.logger, logging.getLevelName(level).lower()), color))

        for level, color in self.LOG_COLORS.items():
            self.formatter._fmt = color + "%(asctime)s[" + module + "]: %(message)s" + "\x1b[0m"
            self.stream_handler.setFormatter(self.formatter)

    def _colorize(self, func, color):
        def wrapper(message, *args, **kwargs):
            message = color + message + "\x1b[0m"
            return func(message, *args, **kwargs)
        return wrapper
