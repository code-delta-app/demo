import queue
import threading
import time

_work = queue.Queue()
_results = {}


def submit(job_id, spec):
    _work.put((job_id, spec))


def result(job_id):
    return _results.get(job_id)


def _worker():
    while True:
        job_id, spec = _work.get()
        started = time.monotonic()
        try:
            steps = spec.get("steps", [])
            for step in steps:
                time.sleep(0.01)
            _results[job_id] = {
                "state": "done",
                "steps": len(steps),
                "elapsed": round(time.monotonic() - started, 3),
            }
        except Exception as exc:
            _results[job_id] = {"state": "failed", "error": str(exc)}
        finally:
            _work.task_done()


threading.Thread(target=_worker, daemon=True).start()
