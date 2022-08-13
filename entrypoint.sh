#!/bin/sh
set -e
file=$(find /code -name '*.hex')
num_files=$(echo "$file" | wc -l)
if [ "$num_files" -gt 1 ]; then
  echo "Too many hex files found" > /dev/stderr
  exit 1
elif [ "$num_files" -eq 0 ]; then
  echo "Didn't find any hex files" > /dev/stderr
  exit 1
fi
port=$(find /dev -name 'tty*' -not -name 'tty')
num_ports=$(echo "$file" | wc -l)
if [ "$num_ports" -gt 1 ]; then
  echo "Too many serial ports found" > /dev/stderr
  exit 1
elif [ "$num_ports" -eq 0 ]; then
  echo "Didn't found any serial ports" > /dev/stderr
  exit 1
fi

avrdude -c avr109 -p m32u4 -P "$port" -U "flash:w:$file:i"
