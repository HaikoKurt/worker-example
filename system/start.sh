#! /bin/bash

python3 server/process.py &
hypercorn --config file:./hypercorn.conf.py app:app