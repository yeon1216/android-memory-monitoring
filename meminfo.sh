#!/bin/bash



# 현재 시간 write
timestamp=`date +%Y%m%d%H%M%S`
#echo `date +%Y%m%d%H%M` >> meminfo.txt

# adb shell dumpsys meminfo : 안드로이드폰에서 실행중인 프로세스 메모리 정보 read
# grep [packageName] : [packageName]와 일치하는 부분 find
# xargs echo : 결과물을 한줄로 만들어줌
# tr -d ',' : , 문자열 제거
# tr -d ' ' : 공백 제거
# awk -F " " '{ split($0, array, "K");print array[1]; }' : K를 이용한 문자열 자르기
#  >> meminfo.txt : meminfo.txt에 결과 문자열 write
tempMemory=`adb shell dumpsys meminfo | grep [packageName] | xargs echo | tr -d ',' | tr -d ' ' | awk -F " " '{ split($0, array, "K");print array[1]; }'`

echo "$timestamp,$tempMemory" >> meminfo.txt
