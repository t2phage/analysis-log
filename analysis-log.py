#!/usr/bin/env python
#-*-coding:UTF-8-*-

import re

for line in file('./test.log'):
    OriginalLogLine = line.strip()
    AccessTime = OriginalLogLine.split(' ')[1:3]
    AccessTimeDate = AccessTime[0]
    AccessTimeHour = AccessTime[1].split(':')[0]
    AccessTimeMinute = AccessTime[1].split(':')[1]
    AccessTimeSecond = AccessTime[1].split(':')[2]
    QueryWord = OriginalLogLine.split(' ty=')[0]
    print QueryWord
    #QueryWord = re.findall('^NOTICE: (/d+)-(/d+).*w\[(.*)\].*$',OriginalLogLine,output)
    #QueryWord = QueryWord.split(' ')[8:].strip('w[]')
    #QueryWord.group() 
