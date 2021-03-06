# 안드로이드 메모리 모니터링
python script를 이용하여 현재 실행중인 안드로이드 특정 프로세스의 메모리를 모니터링 할 수 있습니다.
메모리 측정 인자는 PSS를 사용하였습니다.

# 사용법
1. memory_monitoring.py에 모니터링 할 프로세스의 패키지 이름을 입력해주세요.
1. memory_monitoring.py를 실행해주세요.<br> memory_monitoring.py를 실행하면 해당 프로세스의 메모리 사용량이 실시간으로 모니터링 됩니다.<br>또한 메모리 측정값이 meminfo.txt에 기록됩니다.
1. 메모리 모니터링을 끝내려면 'ctrl+c'를 이용하여 memory_monitoring.py를 종료해주세요.
1. 메모리 모니터링 후에 visualize.py를 실행하면 meminfo.txt에 기록된 값을 이용하여 메모리 사용량 그래프를 그려줍니다.

### 참고사항
- PC에 한 대의 안드로이드 스마트폰만 연결되어있어야합니다.
- PC에 연결된 안드로이드 스마트폰의 개발자모드를 활성화하고 USB 디버깅모드를 활성화해주세요.
- adb 환경변수 설정이 되어있어야합니다.
- 그래프의 가로축 단위는 테스트 시간(초)입니다.
- 그래프의 세로축 단위는 MB입니다.


# LICENSE
MIT License

Copyright (c) 2020 Kim Sung Yeon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
