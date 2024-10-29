from cmath import sqrt
import requests

def calc_task():
    a = []
    for i in range(33000000):
        a.append(sqrt(i*i+127))

def api_task():
    endpoint = "http://127.0.0.1:8000/sleep"
    response = requests.get(endpoint)

def test_single_thread():
    start = time.time()
    calc_task()
    api_task()
    end = time.time()
    print(f"Time taken: {end-start}")

def test_multi_thread():
    import threading
    start = time.time()
    t1 = threading.Thread(target=calc_task)
    t2 = threading.Thread(target=api_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print(f"Time taken: {end-start}")

if __name__ == "__main__":
    import time
    test_single_thread()
    test_multi_thread()