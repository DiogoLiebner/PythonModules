import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._buffer: list[tuple[int, str]] = []
        self._next_rank: int = 1

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._buffer:
            raise IndexError("No data available for output.")

        rank, value = self._buffer.pop(0)
        return rank, value

    def _enqueue(self, value: str) -> None:
        self._buffer.append((self._next_rank, value))
        self._next_rank += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)

        return False

    def ingest(
                self,
                data: int | float | list[typing.Union[int, float]]
            ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._enqueue(str(item))
        else:
            self._enqueue(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("TextProcessor only accepts str or lists of str.")

        if isinstance(data, list):
            for item in data:
                self._enqueue(item)
        else:
            self._enqueue(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("LogProcessor only accepts dict[str, str] \
or lists of dict[str, str].")

        if isinstance(data, list):
            for item in data:
                self._enqueue(self._format_log(item))
        else:
            self._enqueue(self._format_log(data))

    def _format_log(self, data: dict[str, str]) -> str:
        log_level = data.get("log_level", "")
        log_message = data.get("log_message", "")

        if isinstance(log_level, str) \
                and isinstance(log_message, str) and log_level and log_message:
            return f"{log_level}: {log_message}"

        return ", ".join(f"{key}={value}" for key, value in data.items())


def main():
    print("=== Code Nexus - Data Processor ===\n")

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    print("Testing Numeric Processor...")
    print("Trying to validate input '42':", numeric_processor.validate(42))
    print("Trying to validate input 'Hello':",
          numeric_processor.validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")

    try:
        numeric_processor.ingest("foo")
    except ValueError as exc:
        print("Got exception:", exc)

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric_processor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")

    for index in range(3):
        _, value = numeric_processor.output()
        print(f"Numeric value {index}: {value}")

    print("\nTesting Text Processor...")
    print("Trying to validate input '42':", text_processor.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_processor.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    _, text_value = text_processor.output()
    print("Text value 0:", text_value)

    print("\nTesting Log Processor...")
    print("Trying to validate input 'Hello':", log_processor.validate("Hello"))
    print(
        "Processing data: [{'log_level': 'NOTICE', 'log_message': \
'Connection to server'}, "
        "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]"
    )

    log_processor.ingest([
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ])

    print("Extracting 2 values...")
    for index in range(2):
        _, log_value = log_processor.output()
        print(f"Log entry {index}: {log_value}")


if __name__ == "__main__":
    main()
