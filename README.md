## JVM Thread Dump 분석 Tool

**소개**

이 도구는 JVM 프로세스의 Thread Dump를 분석하는 강력한 도구입니다. 정기적으로 JVM Thread Stack Dump를 수집하여 BLOCKED Thread의 존재 여부를 감시하며, 감시된 Thread는 로그로 기록됩니다. 또한, SMTP나 기타 메시지 시스템과 연동하여 서버 상태 알리미로 활용할 수 있습니다.

**실행 환경**
- OS: Linux
- Runtime: Python 3.4 이상, Java 1.5 이상

**설치 가이드**
1. repository의 모든 파일을 원하는 경로에 위치시킵니다.
2. `.py` 파일에 실행 권한을 부여합니다.
3. `JAVA_HOME` 환경 변수를 세팅해주세요.

**실행**
1. `ps -ef` 혹은 `jps -v` 등의 명령어로 JVM 프로세스 ID를 확인합니다.
2. 설치 경로에서 `./start_monitor.py {JVM 프로세스 ID}` 명령어를 실행합니다.
3. `ps -ef | grep start_monitor.py`로 정상적으로 실행되었는지 확인합니다.

**종료**
1. 설치 경로에서 `./stop_monitor.py`를 실행합니다.
2. `ps -ef | grep start_monitor.py`로 정상적으로 종료되었는지 확인합니다.

**Monitoring.properties 설정**
- [LOG] PATH: 이벤트가 발생했을 때 생성되는 로그 경로
- [LOG] INTERVAL: JVM Thread 감시 주기

**튜닝 가이드**
- 기본값으로 BLOCKED Thread를 감시합니다.
- 다른 상태의 Thread를 감시하고 싶다면 `server_monitor.py`의 `STATE.BLOCKED.value`를 다른 상태값으로 수정하세요.
- `getStateCount()`는 JVM Thread Dump를 시도합니다. 캐치된 Dump가 있다면 로그로 저장합니다.
- 로그 저장이 불필요한 경우, 2번째 파라미터로 `None` lambda를 넣어주세요.
  - 예시:
    - `getStateCount(STATE.BLOCKED.value)`: BLOCKED THREAD dump를 시도하며 로그를 저장
    - `getStateCount(STATE.RUNNABLE.value, lambda x, y: None)`: RUNNABLE THREAD dump를 시도하며 로그를 저장하지 않음
    - `getCpuStatus()`: 서버의 CPU점유율 출력

**메모리 모니터링**
- 대용량 트래픽환경에서 ThreadDump가 서브프로세스로 인터벌 실행되며 로그를 수집하는 동안 가비지콜렉터를 모니터링하면 더 좋습니다.
- `jstat -gcutil -t {JVM 프로세스 ID} 5000 20` gc timestamp를 5초 간격으로 20회 수집합니다.
- minor gc와 major gc의 빈도를 체크하고 STW점유를 줄일 수 있는 최적의 gc알고리즘과 코드 최적화를 진행해보세요.
- heap dump에 대해서는 추가 포스팅과 프로그램을 개발하여 곧 공개하도록 하겠습니다.
