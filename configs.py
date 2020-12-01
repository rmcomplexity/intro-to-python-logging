import logging
from io import StringIO
from filters import require_debug_false_filter, require_debug_true_filter

def logging_config_fun():

    # create logger
    app_logger = logging.getLogger("app")
    app_logger.setLevel(logging.DEBUG)

    external_library_logger = logging.getLogger("external_library")
    external_library_logger.setLevel(logging.INFO)

    # long formatter
    long_fmt = logging.Formatter(
        "[APP] {levelname} {asctime} {module} {name}.{funcName}:{lineno:d}: {message}",
        style="{"
    )

    # short formatter
    short_fmt = logging.Formatter(
        "[APP] {levelname} [{asctime}] {message}",
        style="{"
    )

    # console handler config
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(short_fmt)
    console_handler.addFilter(require_debug_false_filter())

    # console debug handler config
    console_debug_handler = logging.StreamHandler()
    console_debug_handler.setLevel(logging.DEBUG)
    console_debug_handler.setFormatter(long_fmt)
    console_debug_handler.addFilter(require_debug_true_filter())

    app_logger.addHandler(console_handler)
    app_logger.addHandler(console_debug_handler)
    external_library_logger.addHandler(console_handler)

LOGGING_CONFIG_DICT = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "long": {
            "format": "[APP] {levelname} {asctime} {module} "
                      "{name}.{funcName}:{lineno:d}: {message}",
            "style": "{"
        },
        "short": {
            "format": "[APP] {levelname} [{asctime}] {message}",
            "style": "{"
        }
    },
    "filters": {
        "debug_true": {
            "()": "filters.require_debug_true_filter"
        },
        "debug_false": {
            "()": "filters.require_debug_false_filter"
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "short",
            "filters": ["debug_false"]
        },
        "console_debug": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "long",
            "filters": ["debug_true"]
        }
    },
    "loggers": {
        "external_library": {
            "handlers": ["console"],
            "level": "INFO"
        },
        "app": {
            "handlers": ["console", "console_debug"],
            "level": "DEBUG"
        }
    }
}

LOGGING_FILE_CONFIG = StringIO("""
[loggers]
keys=root,external_library,app

[handlers]
keys=console,console_debug

[formatters]
keys=long,short

[formatter_long]
format=[APP] {levelname} {asctime} {module} {name}.{funcName}:{lineno:d}: {message}
style={
datefmt=
class=logging.Formatter

[formatter_short]
format=[APP] {levelname} [{asctime}] {message}
style={
datefmt=
class=logging.Formatter

[handler_console]
class=StreamHandler
level=INFO
formatter=short
args=(sys.stdout,)

[handler_console_debug]
class=StreamHandler
level=DEBUG
formatter=long
args=(sys.stdout,)

[logger_root]
level=NOTSET
handlers=console

[logger_external_library]
level=INFO
handlers=console
propagate=1
qualname=external_library

[logger_app]
level=DEBUG
handlers=console,console_debug
qualname=app

""")
