import sys
import logging
import logging.config
from configs import LOGGING_CONFIG_DICT, logging_config_fun, LOGGING_FILE_CONFIG

def dict_config():
    """Config logging using a dictionary."""

    logging.config.dictConfig(LOGGING_CONFIG_DICT)

def file_config():
    """Config logging using a file."""

    logging.config.fileConfig(LOGGING_FILE_CONFIG)

def code_config():
    """Config logging using code."""
    logging_config_fun()

CONFIG_OPTIONS = {
    "1": dict_config,
    "2": code_config,
    "3": file_config
}

def run():
    """Run example."""

    chosen_config_type = input("""
    What type of configuration would you like to try?

    1) Dict config *default
    2) Code config
    3) File config
    """)

    chosen_config_type = chosen_config_type or "1"

    CONFIG_OPTIONS[chosen_config_type]()

    app_logger = logging.getLogger("app")
    views_logger = logging.getLogger("app.views")
    models_logger = logging.getLogger("app.models")

    app_logger.info("Info message in app logger, data: %s", { "test": "data" })
    views_logger.debug("Debug message in views logger, data: %s", { "test": "data" })
    models_logger.info("Info message in models logger, data: %s", { "test": "data" })

"""
Run sample
"""
run()
