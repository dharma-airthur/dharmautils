import functools
import inspect
from typing import Any, Callable, Type
from .log_config import LogConfig
from .log_wrapper import DharmaLogger

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
        base_logger = self.log_config.get_logger(cls.__name__)
        logger = DharmaLogger(base_logger)
        
        # Add logger as a class attribute
        cls.logger = logger

        # Wrap each method with logging
        for name, method in original_methods.items():
            wrapped = self._create_logged_method(method, logger)
            setattr(cls, name, wrapped)

        return cls

    def _create_logged_method(self, method: Callable, logger: DharmaLogger) -> Callable:
        @functools.wraps(method)
        def wrapper(instance, *args, **kwargs):
            trace_id = self.log_config.generate_trace_id()
            logger.set_trace_id(trace_id)

            try:
                logger.info(f"Calling method '{method.__name__}'")
                result = method(instance, *args, **kwargs)
                logger.info(f"Method '{method.__name__}' completed successfully")
                return result
            except Exception as e:
                logger.error(f"Error in method '{method.__name__}': {str(e)}", exc_info=True)
                raise

        return wrapper 