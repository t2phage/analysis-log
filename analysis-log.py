#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import re

dict = {}
pattern = (r'^NOTICE: (\d+)-(\d+) (\d+):(\d+):(\d+).*w\[(.*)\] (.*)')
regex = re.compile(pattern)
pv_sum = 0
hc_sum = 0
nhc_sum = 0
for line in open('./test.log'):
    if line.startswith('NOTICE:'):
        text = line
        match = regex.search(text)
        if match != None :
            dict['month'] = match.group(1)
            dict['day'] = match.group(2)
            dict['hour'] = match.group(3)
            dict['minute'] = match.group(4)
            dict['second'] = match.group(5)
            dict['word'] = match.group(6)
            for seg in match.group(7).split(' '):
                k, j = seg.split('=')
                dict[k] = j
            print 'Query word is: ' + dict['word']
    
        # 计数器
        pv_sum = pv_sum + 1
        if dict['hc'] == "1":
            hc_sum = hc_sum + 1
        else:
            nhc_sum = nhc_sum + 1


# 输出计数器
print "Total PV: %d, Cache hit: %d, Cache miss: %d." % (pv_sum, hc_sum, nhc_sum)
