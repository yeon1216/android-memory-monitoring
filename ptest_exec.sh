#!/bin/bash

rm meminfo.txt
touch meminfo.txt

# meminfo.sh 반복 실행
while true; do sh meminfo.sh; sleep 2 ; done ;