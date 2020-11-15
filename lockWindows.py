import ctypes

def lock():
    ctypes.windll.user32.LockWorkStation()
        
if __name__ == "__main__":
    lock()
