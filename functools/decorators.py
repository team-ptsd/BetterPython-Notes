import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter


def is_prime(number: int) -> bool:
    """Return True if *number* is prime."""
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


class AbstractComponent(ABC):
    @abstractmethod
    def execute(self, upper_bond: int) -> int:
        pass


class ConcreteComponent(AbstractComponent):
    def execute(self, upper_bond: int) -> int:
        count = 0
        for number in range(1, upper_bond):
            if is_prime(number):
                count += 1
        return count


class AbstractDecorator(AbstractComponent, ABC):
    def __init__(self, decorated: AbstractComponent) -> None:
        self._decorated = decorated


class BenchmarkDecorator(AbstractDecorator):
    def execute(self, upper_bond: int) -> int:
        start_time = perf_counter()
        value = self._decorated.execute(upper_bond)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f"Execution of {self._decorated.__class__.__name__} took {run_time:.2f} seconds."
        )
        return value


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    component = ConcreteComponent()
    benchmark_decorator = BenchmarkDecorator(component)
    value = benchmark_decorator.execute(100000)
    logging.info(f"Found {value} primes.")


if __name__ == "__main__":
    main()
