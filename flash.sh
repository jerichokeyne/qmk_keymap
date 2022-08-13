#!/bin/bash
podman run --group-add keep-groups --device "$1" --security-opt label=disable -v "$(pwd):/code" jkeyne/avrdude:latest
