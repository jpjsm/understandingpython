# Introduction

This example shows how to generate metrics in Python with OpenTelemetry (_otel_).
Metrics can be viewed using Prometheus, in this perticular case; but, metrics
can be generated for different backends, i.e. Dynatrace, New Relic, Splunk,
Grafana Labs (Prometheus), [etc.](https://opentelemetry.io/vendors/).

# Pre-requisites

## Docker

See [Get Docker](https://docs.docker.com/get-docker/) to install docker in your environment.

## Python 3.8

> **Note**  
Given the fact that as of 2022-06-01, Python 3.9 and Python 3.10 have not been widely introduced to some of the most popular Linux distros, this demo is done using Python 3.8.  
**Important**  
Python 3.8 is sunsetting as this note is been written (only bug fixes are allowed).

See [Installing Python 3.8.10 side-by-side with other Python instances in Windows 10](python38-SxS-in-windows.md) if you are running Windows and have a different version of Python.

## PIP 3

See []() to install PIP 3

## VirtualEnv



# Setup

## Prometheus

1. Copy the `prometheus` folder to your home folder (~), if in Linux, or to the root of the **C:** drive, if in Windows.

1. Check ports 8888, 9089, and 9090 are used elsewhere in the system.
    - **Windows**: Open a `CMD` window and type:  
  `netstat -a -n | find ":8888"`
      - replace `8888` with `9089`, and then with `9090` to check the other ports.
    - **Linux**:  
    Checking ports in Linux might be a bit trickier. Because the distro and version of the distro you're using, you might have different network tools installed (or you might not have any, if you are trying to run this demo inside a docker image :b ).  
    Open a `shell` window and run one of the following options:
      - `netstat -atu | egrep -i "(8888|9089|9090)"`
      - `ss -atu | egrep -i "(8888|9089|9090)"`

1. Check no *stopped* docker containers have those ports assigned.  
From a `shell` or `CMD` prompt type:
    - `docker container ls --all`

1. If the ports `8888` or `9089` are used elsewhere, you need to update the file: `prometheus.yml`

1. If the port `9090` is used elsewhere, you need to update the file: `start-prometheus-docker.cmd`


## Otel Collector Service

## Python Sample

# Demo

# Additional reading

- [What is  OpenTelemetry? An open-source standard for logs, metrics, and traces @ Dynatrace](https://www.dynatrace.com/news/blog/what-is-opentelemetry-2/)
- [Send data to Dynatrace with OpenTelemetry](https://www.dynatrace.com/support/help/extend-dynatrace/opentelemetry)
- [Dynatrace joins the OpenTelemetry project](https://www.dynatrace.com/news/blog/dynatrace-joins-the-opentelemetry-project/)