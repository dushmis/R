#!/bin/bash

pid=$(pgrep caffeinate)
if [ -z "${pid}" ]; then
    caffeinate -dimsu -w `pgrep Finder` >> /tmp/log.log 2>&1 &
else
    echo "running" >/dev/null
fi