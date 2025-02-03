import logging
import uuid
from functools import lru_cache
from typing import Optional

class LogConfig:
    @lru_cache
    def get_logger(self, name: Optional[str] = None) -> logging.Logger:
        """
        Get or create a logger with the given name
        """
        logger = logging.getLogger(name or __name__)
        
        if not logger.handlers:
            # Configure logger if it hasn't been configured yet
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - [%(trace_id)s] - %(levelname)s - %(message)s'
            )
            
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        
        return logger

    def generate_trace_id(self) -> str:
        """
        Generate a unique trace ID for log tracking
        """
        return str(uuid.uuid4())[:8] 