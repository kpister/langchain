from typing import Any, List

from langchain.callbacks.tracers.base import BaseTracer
from langchain.callbacks.tracers.schemas import Run


class RunStackCallbackHandler(BaseTracer):
    name = "run_stack_callback_handler"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.traced_runs: List[Run] = []

    def _persist_run(self, run: Run) -> None:
        self.traced_runs.append(run)

    def peek(self) -> Run:
        return self.traced_runs[-1]

    def pop(self) -> Run:
        return self.traced_runs.pop()