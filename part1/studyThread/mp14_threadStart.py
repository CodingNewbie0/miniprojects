# 스레드 학습
# 기본프로세스 하나, 서브 스레드 다섯개 동시에 진행
import threading
import time

# Thread를 상속받은 백그라운드작업 클래스
class BackfroundWorker(threading.Thread):
    # 생성자
    def __init__(self, names: str) -> None:
        super().__init__()
        self._name = f'{threading.current_thread().name} : {names}'

    def run(self) -> None:
        print(f'BackfroundWorker start : {self._name}')
        time.sleep(2)
        print(f'BackfroundWorker end : {self._name}')

if __name__ == '__main__':
    print('기본 프로세스 시작.')

    for i in range(5):
        name = f'서브 스레드{i}'
        th = BackfroundWorker(name)
        th.start() # run이 실행됨

    print('기본 프로세스 종료.')