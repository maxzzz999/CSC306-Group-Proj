import threading
import time
import random

NUM_PHILOSOPHERS = 5
NUM_FORKS = NUM_PHILOSOPHERS

forks = [threading.Semaphore(1) for _ in range(NUM_FORKS)]
mutex = threading.Semaphore(1)

def philosopher(index):
    while True:
        print(f"Philosopher {index} is thinking...")
        time.sleep(random.randint(1, 5))
        
        mutex.acquire()
        
        left_fork_index = index
        right_fork_index = (index + 1) % NUM_FORKS
        
        forks[left_fork_index].acquire()
        forks[right_fork_index].acquire()
        
        mutex.release()
        
        print(f"Philosopher {index} is eating...")
        time.sleep(random.randint(1, 5))
        
        forks[left_fork_index].release()
        forks[right_fork_index].release()

philosopher_threads = []
for i in range(NUM_PHILOSOPHERS):
    philosopher_threads.append(threading.Thread(target=philosopher, args=(i,)))
    
for thread in philosopher_threads:
    thread.start()
    
for thread in philosopher_threads:
    thread.join()
