import logging
from typing import Any, Optional

class DharmaLogger:
    """
    A wrapper for the standard logger that automatically includes trace_id
    """
    def __init__(self, logger: logging.Logger):
        self._logger = logger
        self._trace_id = None

    def set_trace_id(self, trace_id: str) -> None:
        self._trace_id = trace_id

    def _log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        if 'extra' not in kwargs:
            kwargs['extra'] = {}
        kwargs['extra']['trace_id'] = self._trace_id
        self._logger.log(level, msg, *args, **kwargs)

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.DEBUG, msg, *args, **kwargs)

    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.INFO, msg, *args, **kwargs)

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.ERROR, msg, *args, **kwargs)

    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.CRITICAL, msg, *args, **kwargs) 