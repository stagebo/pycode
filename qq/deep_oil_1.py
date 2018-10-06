#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     deep_oil_1
    Author:        wyb
    Date:          2018/9/30 0030
    Description:   深度优先搜索
"""
#scr = from, dest = in, water = 水量
import copy
global num

class Oil(object):

    def __init__(self, capacity, water=0):

        self.capacity = capacity

        self.water = water



    def __eq__(self, other):#不论发生什么，只要有 == 做比较，就返回True

        return self.capacity == other.capacity and self.water == other.water

    def __ne__(self, other):

        return not self.__eq__(other)



    def is_empty(self):

        return self.water == 0



    def is_full(self):

        return self.capacity == self.water



    def dump_in(self, water):

        assert self.water + water <= self.capacity

        self.water += water



    def dump_out(self, water):

        assert self.water >= water

        self.water -= water



    def __str__(self):

        return str(self.water)

    def __repr__(self):
        return self.__str__()

       # __repr__ = __str__  ???




class Action(object):

    def __init__(self, from_, to_, water):

        self.from_ = from_

        self.to_ = to_

        self.water = water






class State(object):

    def __init__(self, oil_list, action):

        self.oil_list = copy.deepcopy(oil_list)

        self.action = copy.deepcopy(action)



    def do_dump(self):

        self.oil_list[self.action.from_].dump_out(self.action.water)

        self.oil_list[self.action.to_].dump_in(self.action.water)



    def __eq__(self, other):

        for bt_now, bt_end in zip(self.oil_list, other.oil_list):

            if bt_now != bt_end:

                return False

        return True



    def __ne__(self, other):

        return not self.__eq__(other)



class Algorithm(object):

    def __init__(self, start, end):

        self.start = start

        self.end = end

        assert len(start) == len(end)

        self.oil_count = len(start)



    def search(self, stack=None):

        if stack is None:

            stack = [State(self.start, None)]

        curr = stack[-1]

        if self.is_finished(curr):

            self.print_result(stack)

            return

        for i in range(self.oil_count):

            for j in range(self.oil_count):

                self.do_action(stack, curr, i, j)



    def do_action(self, stack, current, i, j):

        new_state = self.dump_water(current.oil_list, i, j)

        if new_state:

            if not self.is_processed_state(stack, new_state):

                stack.append(new_state)

            self.search(stack)



            stack.pop()



    def dump_water(self, oil_list, i, j):

        if i != j:

            from_, to_ = oil_list[i], oil_list[j]

            if from_.is_empty() or to_.is_full():

                return None

            water = to_.capacity - to_.water

            if water > from_.water:

                water = from_.water

                new_state = State(oil_list, Action(i, j, water))

                new_state.do_dump()

                return new_state

        return None



    def is_finished(self, current):

        for bt_1, bt_2 in zip(self.end, current.oil_list):

            if bt_1 != bt_2:

                return False

        return True



    def is_processed_state(self, stack, new_state):

        for one in stack:

            if one == new_state:

                return True

        return False



    def print_result(self, stack):

        num = 0

        print ('需要%d步' % (len(stack) - 1))

        for state in stack:

            num += 1

            if state.action:

                s = '%d号倒入%d号%d两' % (state.action.from_, state.action.to_, state.action.water)

            else:

                s = ''

            print ('%s <=== %s' % (state.oil_list, s))

            print ('\n')

        print('共%d种解法' % (num))



if __name__ == '__main__':

    start = [Oil(10, 10), Oil(7, 0), Oil(3, 0)]
    end = [Oil(10, 5), Oil(7, 5), Oil(3, 0)]
    alg = Algorithm(start, end)

    alg.search()
    print("main")