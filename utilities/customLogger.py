import logging
import os
from pathlib import Path


class LogGen:

    @staticmethod
    def loggen(name):
        log_dir = Path.cwd() / "Logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "loggerfile.log"

        logger = logging.getLogger(name if name else "nopCommerce")  # use a named logger
        if not logger.handlers:  # prevent duplicate handlers
            logger.setLevel(logging.INFO)  # ensure INFO+ messages are processed

            fh = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter(
                "%(asctime)s: %(levelname)s: %(name)s: %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p"
            )
            fh.setFormatter(formatter)
            logger.addHandler(fh)

            # optional: also print to console (helpful during development/tests)
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            logger.addHandler(ch)

            logger.propagate = False
        return logger
