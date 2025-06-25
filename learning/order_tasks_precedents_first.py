#!/usr/bin/env python
# -*- coding: utf-8 -*-

def order_tasks_precedents_first(task_list):
    '''
    Returns a list of tasks that can be executed in the order given, with no risk of failure for predecesor not completed.

    :task_list: List of (task_id, list(required_tasks))
    '''
    ordered_tasks = []
    remaining = len(task_list)
    i = remaining - 1
    while task_list:
        if not (set(task_list[i][1]) - set(ordered_tasks)):
            t = task_list.pop(i)
            ordered_tasks.append(t[0])

        i -= 1
        if i < 0:
            r = len(task_list)
            if r == remaining:
                raise Exception("Not enough precedents to solve the problem.\nPrecendents: {0}.\nRemaining task ids: {1}".format(ordered_tasks, [t[1] for t in task_list]))
            
            remaining = r
            i = remaining - 1
    
    return ordered_tasks



if __name__ == "__main__":
    t1 = [
        (1, []),
        (2, []),
        (3, [2,1]),
        (4, [3]),
        (5, [2]),
        (6, [1]),
    ]

    print order_tasks_precedents_first(t1)