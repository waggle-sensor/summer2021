## Meeting Notes

- Where do we want to put the metrics? (Assuming Sage database)
- Do we adopt Prometheus as the live metrics exporter?
  - Pros: it supports HTTP and works well with tagged data (n dimensional data)
  - Cons: we would possibly need to expose an HTTP socket on the nodes, which could be a security hazard? *Would we need to implement authentication for pulling metrics?*



## Post-Meeting Notes

- My main goal is to implement live profiling to supplement Aji's edge controller. I will need to setup a Prometheus configuration on the NX that pulls metrics from each app using sockets. When the `live_metrics` module inits, the app will block until the socket connection to `live_metrics.sock` is established.
  - Prometheus Client and custom collector
    - Runs on node in container, collects metrics from unix sockets using a custom collector
    - Runs in its own container
    - Hosts a message server that gathers messages from apps and dispatches them to the controller
  - `live_metrics.py` (for use in the app written in a way that is convenient for developers)
    - Runs inside the app container as a Python library that the developers can call for convenience profiling methods
    - Connects to the message server via socket *(TODO: Will the socket communication with the message server be entirely written by me from scratch or is there a better solution available? I need to ask someone about RabbitMQ and how that could work with this setup.)*

