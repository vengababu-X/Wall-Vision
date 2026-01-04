import subprocess
import time
import statistics

TARGET_IP = "192.168.1.105"  # phone / device IP
WINDOW_SIZE = 10
THRESHOLD = 15.0

window = []
distance_history = []
HISTORY_SIZE = 5

def ping_latency():
    start = time.time()
    subprocess.run(
        ["ping", "-c", "1", TARGET_IP],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return (time.time() - start) * 1000

def estimate_distance(stddev):
    if stddev > 45:
        return "~1–2 m (very close)"
    elif stddev > 30:
        return "~2–4 m (near)"
    else:
        return "~4–8 m (far)"

def get_detection():
    latency = ping_latency()
    window.append(latency)

    if len(window) > WINDOW_SIZE:
        window.pop(0)
        stddev = statistics.pstdev(window)

        if stddev > THRESHOLD:
            dist = estimate_distance(stddev)
            distance_history.append(dist)
            if len(distance_history) > HISTORY_SIZE:
                distance_history.pop(0)

            stable = max(set(distance_history), key=distance_history.count)
            return True, stable
    return False, None
