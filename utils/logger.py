import logging
import os

def setup_logger(name="scraper"):
    log_folder = "output"
    os.makedirs(log_folder, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # prevent duplicate handlers
        file_handler = logging.FileHandler(
            os.path.join(log_folder, "process.log")
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
