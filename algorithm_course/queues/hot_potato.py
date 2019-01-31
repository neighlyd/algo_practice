from algorithm_course.queues.queue import Queue


def hot_potato(kids, rounds):

    q = Queue()

    for kid in kids:
        q.enqueue(kid)

    while q.size() > 1:
        for i in range(rounds):
            kid_to_move = q.dequeue()
            q.enqueue(kid_to_move)
        q.dequeue()

    return q.dequeue()


assert hot_potato(('Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'), 9) == 'David'
