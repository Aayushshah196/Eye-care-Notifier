from multiprocessing import Process, Manager
from notifier import notifier
from app import Window

def start_app(close_status):
    window = Window()
    window.mainloop()
    close_status["close"] = window.close_status



if __name__ == "__main__":
    manager = Manager()
    close_status = manager.dict()
    close_status["close"] = -1
    p1 = Process(target=notifier, name="Background Notifier", daemon=True)
    p2 = Process(target=start_app, name="Eye care Settings", args=(close_status,), daemon=True)

    p1.start()
    p2.start()
    
    while(True):
        if close_status["close"]==0:
            p1.terminate()
            p1 = Process(target=notifier, name="Background Notifier", args=(close_status, ), daemon=True)
            p1.start()
        elif close_status["close"] == 1:
            p1.terminate()
            p2.terminate()
            break
    p1.join
    p2.join()