from dharma_utils import DharmaLog

@DharmaLog()
class MyService:
    def do_something(self, value: str) -> str:
        return f"Processing {value}"

    def another_method(self) -> None:
        print("Another method") 