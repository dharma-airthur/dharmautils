# DharmaUtils

A library developed to standardize utility classes and their usage across different repositories, providing common functionality and consistent implementation patterns.

## Features

### Logging Module

- Decorator-based class logging with `@DharmaLog()`
- Automatic method entry/exit tracking
- Trace ID generation for request tracking
- Hierarchical logging with class-based contexts
- Formatted output with timestamps and log levels
- Exception tracking and error logging
- Thread-safe logging implementation

## Installation

Using Poetry:

    ```bash
    # Add dharmautils directly from the repository
    poetry add git+https://github.com/DharmaAI/dharmautils.git
    ```

## Usage

    ```python
    from dharmautils.logging import DharmaLog

    @DharmaLog()
    class MyMLModel:
        def train(self, data):
            self.logger.info("Starting model training")
            # Your training code here
            self.logger.info("Training completed")

        def predict(self, input_data):
            self.logger.info("Making predictions")
            # Your prediction code here
    ```

## Logging Features

- Automatic trace ID generation for request tracking
- Hierarchical logging with class-based contexts
- Formatted output with timestamps and log levels
- Exception tracking and error logging
- Thread-safe logging operations

## License

Copyright (c) 2024 Dharma AI - All rights reserved.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

## Requirements

- Python ^3.12
- Poetry for dependency management
