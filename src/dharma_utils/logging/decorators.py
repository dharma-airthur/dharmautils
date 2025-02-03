import functools
import inspect
from typing import Any, Callable, Type
from .log_config import LogConfig

class DharmaLog:
    """
    A decorator class for adding logging capabilities to classes
    """
    def __init__(self) -> None:
        self.log_config = LogConfig()

    def __call__(self, cls: Type) -> Type:
        # Store original methods
        original_methods = {
            name: method 
            for name, method in inspect.getmembers(cls, inspect.isfunction)
            if not name.startswith('__')
        }

        # Create logger instance for the class
        logger = self.log_config.get_logger(cls.__name__)

        # Wrap each method with logging
        for name, method in original_methods.items():
            wrapped = self._create_logged_method(method, logger)
            setattr(cls, name, wrapped)

        return cls

    def _create_logged_method(self, method: Callable, logger: Any) -> Callable:
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            trace_id = self.log_config.generate_trace_id()
            extra = {'trace_id': trace_id}

            try:
                logger.info(
                    f"Calling method '{method.__name__}'",
                    extra=extra
                )
                result = method(*args, **kwargs)
                logger.info(
                    f"Method '{method.__name__}' completed successfully",
                    extra=extra
                )
                return result
            except Exception as e:
                logger.error(
                    f"Error in method '{method.__name__}': {str(e)}",
                    extra=extra,
                    exc_info=True
                )
                raise

        return wrapper 