#!/usr/bin/python

import sys
import pytz
import datetime as dt

utc = pytz.utc
eastern = pytz.timezone('US/Eastern')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

target = open('final_weather_data.csv', 'w')
target.truncate()

with open('weather-data.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    if len(line) != 148:
        continue
    data = line.strip();
    USAF = data[0:6];
    WBAN = data[7:12];
    datestring = data[13:25];
    DIR = data[26:29];
    SPD = data[30:33];
    GUS = data[34:37];
    CLG = data[38:41];
    SKC = data[42:45];
    L = data[46:47];
    M = data[48:49];
    H = data[50:51];
    VSB = data[52:56];
    MW1 = data[57:59];
    MW2 = data[60:62];
    MW3 = data[63:65];
    MW4 = data[66:68];
    AW1 = data[69:71];
    AW2 = data[72:74];
    AW3 = data[75:77];
    AW4 = data[78:80];
    W = data[81:82];
    TEMP = data[83:87];
    DEWP = data[88:92];
    SLP = data[93:99];
    ALT = data[100:105];
    STP = data[106:112];
    MAX = data[113:116];
    MIN = data[117:120];
    PCPO1 = data[121:126];
    PCP06 = data[127:132];
    PCP24 = data[133:138];
    PCPXX = data[139:144];
    SD = data[145:147];

    datestring = datestring[0:4] + '/' + datestring[4:6] + '/' + datestring[6:8] + ' ' + datestring[
                                                                                         8:10] + ':' + datestring[
                                                                                                       10:12] + ':00';
    try:
        date = dt.datetime.strptime(datestring, "%Y/%m/%d %H:%M:%S")
        date_gmt = utc.localize(date, is_dst=None)
        date_est = date_gmt.astimezone(eastern)
        final_line = USAF.strip() + ',' + WBAN.strip() + ',' + str(date_est)[
                                                               0:19] + ',' + DIR + ',' + SPD.strip() + ',' + GUS.strip() + ',' + CLG.strip() + ',' + SKC.strip() + ',' + L.strip() + ',' + M.strip() + ',' + H.strip() + ',' + VSB.strip() + ',' + MW1.strip() + ',' + MW2.strip() + ',' + MW3.strip() + ',' + MW4.strip() + ',' + AW1.strip() + ',' + AW2.strip() + ',' + AW3.strip() + ',' + AW4.strip() + ',' + W.strip() + ',' + TEMP.strip() + ',' + DEWP.strip() + ',' + SLP.strip() + ',' + ALT.strip() + ',' + STP.strip() + ',' + MAX.strip() + ',' + MIN.strip() + ',' + PCPO1.strip() + ',' + PCP06.strip() + ',' + PCP24.strip() + ',' + PCPXX.strip() + ',' + SD.strip()
        target.write(final_line)
        target.write("\n")
    except ValueError:
        print 'error';

target.close()
