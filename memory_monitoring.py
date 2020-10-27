import matplotlib.pyplot as plt
import subprocess
import time

# 모니터링이 필요한 패키지 이름
# 여기에 모니터링이 필요한 패키지 이름을 입력해주세요
# ex) com.example.test
packageName = "com.example.test"

# 테스트 시작 시간
startTime = time.time()

# 테스트 결과 저장 파일
testResultWriteFile = open("meminfo.txt",'w')

while True:
    # 현재 시간
    # tempTime = datetime.datetime.now()
    tempTime = time.time()
    testTime = ((int)(tempTime - startTime))
    # shell script 명령어 작성
    # adb shell dumpsys meminfo : 안드로이드폰에서 실행중인 프로세스 메모리 정보 read
    # grep com.vaultmicro.camerafi.live : com.vaultmicro.camerafi.live와 일치하는 부분 find
    # xargs echo : 결과물을 한줄로 만들어줌
    # tr -d ',' : , 문자열 제거
    # tr -d ' ' : 공백 제거
    # awk -F " " '{ split($0, array, "K");print array[1]; }' : K를 이용한 문자열 자르기
    #  >> meminfo.txt : meminfo.txt에 결과 문자열 write
    cmd = ['adb','shell','dumpsys','meminfo','|','grep',packageName,'|','xargs echo','|','tr','-d','\',\'','|','tr','-d','\' \'','|','awk','-F','" "','\'{ split($0, array, "K");print array[1]; }\'']
    # 명령어 실행 후 반환되는 결과를 파일에 저장
    fd_popen = subprocess.Popen(cmd,stdout=subprocess.PIPE).stdout
    # 파일에 저장된 결과를 읽고 utf-8로 인코딩
    tempTotalPSSMemory = (int)(fd_popen.read().strip().decode('utf-8'))//1024
    # 파일 닫기
    fd_popen.close()

    # 프로세스가 실행중이지 않음
    if tempTotalPSSMemory!=0 :
        # 그래프 그리기
        plt.scatter(testTime,tempTotalPSSMemory)
        plt.pause(0.001)
        # 파일에 작성
        testResultWriteFile.write(str(testTime)+','+str(tempTotalPSSMemory)+'\n')
    else :
        startTime = time.time()

plt.show()