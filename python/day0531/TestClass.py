import threading
import time

class CountThread(threading.Thread):
    def __init__(self, title, start, end, term):
        super().__init__()
        self._title = title
        self._start = start
        self._end = end
        self._term = term

    def do_job(self):
        for _ in range(self._start, self._end):
            print(self._title, _)
            time.sleep(self._term)

    def run(self) -> None:
        self.do_job()
