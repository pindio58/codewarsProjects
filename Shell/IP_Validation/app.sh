#!/bin/bash
adr="$1"
echo "$adr" | grep -q "^[1-9]*\.[1-9]*\.[1-9]*\.[1-9]$"
if [ ! $? = 0 ]; then
    # echo aajo
  echo False
else
  echo True
fi