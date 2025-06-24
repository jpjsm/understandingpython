from random import randrange
from typing import Iterable
from sympy import nextprime
from time import sleep

from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import (
    OTLPMetricExporter,
)
from opentelemetry.metrics import (
    CallbackOptions,
    Observation,
    get_meter_provider,
    set_meter_provider,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from sqlalchemy import true

exporter = OTLPMetricExporter(insecure=True)
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader])
set_meter_provider(provider)


def observable_counter_func(options: CallbackOptions) -> Iterable[Observation]:
    yield Observation(randrange(1,25), {})


def observable_up_down_counter_func(
    options: CallbackOptions,
) -> Iterable[Observation]:
    yield Observation(randrange(-25,25), {})


def observable_gauge_func(options: CallbackOptions) -> Iterable[Observation]:
    yield Observation(randrange(0,10), {})


meter = get_meter_provider().get_meter("getting-started", "0.1.2")

# Counter
counter = meter.create_counter("counter")

# Async Counter
observable_counter = meter.create_observable_counter(
    "observable_counter",
    [observable_counter_func],
)

# UpDownCounter
updown_counter = meter.create_up_down_counter("updown_counter")

# Async UpDownCounter
observable_updown_counter = meter.create_observable_up_down_counter(
    "observable_updown_counter", [observable_up_down_counter_func]
)

# Histogram
histogram = meter.create_histogram("histogram")


# Async Gauge
gauge = meter.create_observable_gauge("gauge", [observable_gauge_func])

print("Press CTRL+C to terminate")
messagewait = 0.0
symbols = ['-', '\\', '|', '/']
i = 0
while true:
  counter.add(randrange(1000,10000))
  observable_counter
  updown_counter.add(randrange(-100,100))
  histogram.record(nextprime(randrange(10007,104729))/nextprime(randrange(1009,9973)))
  waiting = nextprime(randrange(1009,9973))/nextprime(randrange(10007,104729))
  sleep(waiting)
  messagewait = messagewait + waiting
  if messagewait > 1:
      print("   \r{0}\r".format(symbols[i%len(symbols)]), end='')
      i = i + 1
