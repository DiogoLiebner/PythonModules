from typing import Any, Protocol, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._buffer: list[tuple[int, str]] = []
        self._next_rank: int = 1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._buffer:
            raise IndexError("No data available for output.")

        rank, value = self._buffer.pop(0)
        return rank, value

    def _enqueue(self, value: str) -> None:
        self._buffer.append((self._next_rank, value))
        self._next_rank += 1


class ExportPlugin(Protocol):
    def process_output(
            self,
            data: list[tuple[int, str]]
    ) -> None:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)

        return False

    def ingest(
                self,
                data: int | float | list[Union[int, float]]
            ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._enqueue(str(item))
        else:
            self._enqueue(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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
    def validate(self, data: Any) -> bool:
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


class DataStream(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._processors: list[DataProcessor] = []
        self._processed_counts: dict[DataProcessor, int] = {}

    def validate(self, data: Any) -> bool:
        return False

    def ingest(self, data: Any) -> None:
        raise NotImplementedError(
            "DataStream does not ingest single elements directly; use \
process_stream()."
        )

    def register_processor(self, proc: DataProcessor) -> None:
        if proc not in self._processors:
            self._processors.append(proc)
            self._processed_counts[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False
            for processor in self._processors:
                if processor.validate(item):
                    before = len(processor._buffer)
                    processor.ingest(item)
                    after = len(processor._buffer)
                    self._processed_counts[processor] += after - before
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process element in stream: \
{item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            pret_n = processor.__class__.__name__.replace("Processor", " Processor").strip()
            total = self._processed_counts.get(processor, 0)
            remaining = len(processor._buffer)
            print(
                f"{pret_n}: total {total} items processed, remaining \
{remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
