#!/bin/bash

until python gym_search.py; do
    echo "Gym search crashed with exit code $?. Respawning..." >&2
    sleep 1
done
