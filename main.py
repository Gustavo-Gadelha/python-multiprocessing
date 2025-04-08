import random
import time
from multiprocessing import Queue, Semaphore, Process, Manager


def deliver(semaphore: Semaphore, deliveries: Queue, log: dict[any], id: int):
    total_deliveries = 0
    delivery_time = 0

    while True:
        if deliveries.empty():
            break

        semaphore.acquire()
        print(f'[Motoboy {id}] < Acquired semaphore >')
        order = deliveries.get()
        semaphore.release()
        print(f'[Motoboy {id}] < Released semaphore >')

        start = time.perf_counter_ns()
        time_to_deliver = random.uniform(1,3)
        print(f'[Motoboy {id}] - Delivering {order} in {time_to_deliver}')
        time.sleep(time_to_deliver)

        end = time.perf_counter_ns()

        total_deliveries += 1
        delivery_time += (end - start) / 10**9
        print(f'[Motoboy {id}] + {order} Delivered')

    log[id] = {
        'total_deliveries': total_deliveries,
        'delivery_time': delivery_time,
        'average_time': delivery_time / total_deliveries
    }


def make_deliveries(total):
    queue = Queue()
    for number in range(total):
        queue.put(f'Order {number}')

    return queue


if __name__ == '__main__':
    semaphore = Semaphore(1)
    deliveries = make_deliveries(15)

    manager = Manager()
    log = manager.dict()

    motoboys = []
    for n in range(5):
        motoboy = Process(target=deliver, args=(semaphore, deliveries, log, n))
        motoboys.append(motoboy)
        motoboy.start()

    for m in motoboys:
        m.join()

    import json

    print('\n >>>> All deliveries have been done <<<<')
    print(json.dumps(dict(log), indent=2))
