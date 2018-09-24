#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyfits
import time
import datetime
from multiprocessing import Pool
import numpy as np
import gc

print '\ntest date : ', datetime.datetime.now()
filetitle = 'PM0011_036'
fname = []
for i in range(0x01, 0x0E):
    fname.append('../data/' + filetitle + '/' + filetitle + str(hex(i))[2].upper() + '1.sf')
print fname

f = map(lambda name: pyfits.open(name), fname)

header = map(lambda fp: fp['SUBINT'].header, f)
data = map(lambda fp: fp['SUBINT'].data, f)

freq = 96
sub_int = 4096
sub_int_num = 2051


def compress_m(mat1, time_com):
    # mat1 : ndarray, the target matrix, shape(sub_int_num*sub_int, freq)
    # time_com : integer, the range of time integration
    a = mat1[0:time_com, :].sum(0)
    for s in range(1, sub_int_num * sub_int / time_com):
        a = np.append(a, mat1[s * time_com:(s + 1) * time_com, :].sum(0))
    a = a.reshape(sub_int_num * sub_int / time_com, freq)
    return a


outfile = open('../output/corTest1', 'a')
outfile2 = []

for i in range(91):
    outfile2.append(open('../output/channel/resultofchannel_%s' % i, 'w'))
compress_index = 256

outfile.write("test date = " + str(datetime.datetime.now()) + '\n')
outfile.write("compress index = %d\n" % (compress_index))

start_time = time.time()
# new
m = []
com = []
for i in range(3):
    m.append(data[i]['DATA'].reshape(sub_int_num * sub_int, freq))
    com.append(compress_m(m[i], compress_index))
del m
gc.collect()

end_time = time.time()
outfile.write('compress time = %d\n' % (end_time - start_time))


def correlation_cal(m0, m1, offset):
    # offset : integer, the time offset for correlation test.
    cor = (m0[offset:, :] * m1[:-offset, :]).sum()
    print 'offset = %s : cor = %s' % (offset, cor)


rangeM = sub_int * sub_int_num / compress_index

start_time = time.time()
count = -1

#这里是最耗时的地方，因为找不到numpy里面能简化这几个循环的方法
for beam1 in range(3):
    for beam2 in range(beam1, 3):
        count += 1
        for channel in range(freq):
            outfile2[count].write('#%s\n' % channel)
            cons = np.dot(com[beam1][:, channel:channel+1], com[beam2][:, channel:channel+1].T)
            for k in range(rangeM):
                a = cons[k:, :rangeM - k].diagonal().sum()
                b = cons[:rangeM - k, k:].diagonal().sum()
                outfile2[count].write('%s\n%s\n' % (a, b))
            del cons
            gc.collect()
        outfile2[count].close()


end_time = time.time()
outfile.write('calculate time = %d\n' % (end_time - start_time))
outfile.write('complete!')
outfile.close()


