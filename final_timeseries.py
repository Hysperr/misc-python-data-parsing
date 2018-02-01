"""
Format, tally and print relevant user activity
that occurs between the first two months
(non-inclusive) as specified in the test-case
string. Output is listed from most recent month,
each record sorted alphabetically.
"""

import re
from collections import defaultdict


test_case_1 = '2015-08, 2016-04\n\n2015-08-15, clicks, 635\n2016-03-24, app_installs, 683\n2015-04-05, favorites, ' \
              '763\n2016-01-22, favorites, 788\n2016-01-22, favorites, 8999\n2015-12-26, clicks, 525\n2016-06-03, reshares, ' \
              '101\n2015-12-02, app_installs, 982\n2016-09-17, app_installs, 770\n2015-11-07, impressions, 245\n2016-10-16, ' \
              'impressions, 567 '

test_case_2 = "2015-02, 2016-03\n\n2015-04-22, impressions, 238\n2016-12-23, impressions, 492\n2015-10-31, follows, " \
              "898\n2016-03-19, impressions, 388\n2015-10-14, app_installs, 335\n2016-08-05, impressions, 120\n2015-02-05, " \
              "favorites, 616\n2016-12-06, follows, 459\n2015-12-31, follows, 388\n2016-02-24, impressions, " \
              "155\n2015-06-08, favorites, 876\n2016-04-24, app_installs, 639\n2015-05-16, app_installs, 875\n2016-03-06, " \
              "reshares, 938\n2015-03-25, follows, 590\n2016-10-09, favorites, 729\n2015-01-21, impressions, " \
              "568\n2016-06-24, clicks, 95\n2015-11-07, app_installs, 513\n2016-11-08, clicks, 379\n2015-12-30, reshares, " \
              "346\n2016-10-27, clicks, 245\n2015-04-04, follows, 948\n2016-03-15, clicks, 919\n2015-07-21, clicks, " \
              "612\n2016-04-08, clicks, 628\n2015-05-07, clicks, 781\n2016-10-01, app_installs, 445\n2015-04-17, " \
              "app_installs, 3\n2016-01-11, reshares, 395\n2015-10-19, impressions, 767\n2016-01-03, clicks, " \
              "192\n2015-07-07, impressions, 625\n2016-04-02, favorites, 775\n2015-11-29, impressions, 992\n2016-04-03, " \
              "impressions, 775\n2015-12-15, follows, 607\n2016-06-21, clicks, 864\n2015-02-27, impressions, " \
              "918\n2016-03-12, favorites, 526\n2015-05-20, favorites, 812\n2016-05-14, app_installs, 299\n2015-01-09, " \
              "reshares, 94\n2016-03-22, clicks, 702\n2015-08-22, impressions, 146\n2016-11-04, app_installs, " \
              "554\n2015-08-27, app_installs, 102\n2016-11-21, follows, 763\n2015-10-01, clicks, 908\n2016-01-27, reshares, " \
              "440\n2015-10-30, impressions, 597\n2016-06-03, follows, 471\n2015-05-22, follows, 545\n2016-03-13, clicks, " \
              "371\n2015-12-27, reshares, 11\n2016-01-13, favorites, 557\n2015-11-06, clicks, 661\n2016-09-26, follows, " \
              "920\n2015-11-01, reshares, 433\n2016-05-14, reshares, 627\n2015-06-18, app_installs, 185\n2016-08-09, " \
              "reshares, 271\n2015-01-27, impressions, 476\n2016-04-25, reshares, 275\n2015-07-23, impressions, " \
              "141\n2016-06-28, clicks, 962\n2015-06-24, reshares, 451\n2016-02-28, clicks, 181\n2015-09-18, follows, " \
              "581\n2016-11-13, app_installs, 694\n2015-03-10, clicks, 929\n2016-10-19, favorites, 128\n2015-09-25, " \
              "favorites, 947\n2016-02-29, reshares, 353\n2015-04-24, impressions, 115\n2016-03-25, follows, " \
              "905\n2015-09-26, impressions, 665\n2016-01-29, reshares, 974\n2015-12-25, favorites, 729\n2016-04-25, " \
              "follows, 109\n2015-07-25, impressions, 37\n2016-04-28, reshares, 959\n2015-09-13, app_installs, " \
              "415\n2016-09-27, reshares, 686\n2015-01-05, clicks, 881\n2016-05-06, follows, 424\n2015-01-19, clicks, " \
              "569\n2016-11-02, clicks, 145\n2015-01-22, impressions, 894\n2016-07-10, reshares, 627\n2015-04-18, clicks, " \
              "858\n2016-06-28, clicks, 724\n2015-06-03, clicks, 535\n2016-02-07, reshares, 770\n2015-09-18, impressions, " \
              "146\n2016-06-18, favorites, 628\n2015-10-09, reshares, 319\n2016-07-23, follows, 885\n2015-05-07, reshares, " \
              "43\n2016-10-29, app_installs, 916 "


# TEST CASE
data = test_case_2


daoko = defaultdict(list)                                           # def dict can call functions on mutable value list while empty
data = data.strip().replace(' ', '').split('\n')                    # trim white-space, remove spaces, split on delimiter='\n'
data = list(filter(None, data))                                     # remove any ''
data_range = list(map(int, re.sub('-', '', data[0]).split(',')))    # remove dashes '-' from date, convert to int
data_range[1] = data_range[1]-1                                     # because the end date is non-inclusive
data = data[1:]

for idx, x in enumerate(data):
    xi = x.split(',')                               # Split each entry ['2015-08-15,clicks,635'] => ['2015-08-15', 'clicks', '635']
    date = int(re.sub('-', '', xi[0])[:6])          # Remove dashes, take year & month yyyymm from yyyymmdd then convert to int
    if date < data_range[0] or date > data_range[1]:
        continue                                    # If month isn't within  range, skip processing to next entry
    category = xi[1]
    tally = int(xi[2])
    if category not in daoko[date]:
        daoko[date].extend([category, tally])       # Will mutate the list by 'morphing' contents inside without appending a list
    else:                                           # Else increase the tally for this month's category
        for tdx, t in enumerate(daoko[date]):
            if t == category:
                daoko[date][tdx + 1] += tally

for k, v in daoko.items():
    if len(v) > 2:
        daoko[k] = list(zip(daoko[k][::2], daoko[k][1::2]))  # [1:['run', 5, 'ball', 4],...] => [1:[('run', 5), ('ball', 4)],...]
        daoko[k].sort(key=lambda z: z[0])                    # Sort value lists on category  => [1:[('ball', 4), ('run', 5)],...]
daoko = sorted(daoko.items(), reverse=True)                  # Sort dictionary on keys (integer months), reverse for desc order

# output formatted engagement data, regex is great
for c in daoko:
    c = re.sub('[]()[\']+', '', str(c))
    c = c[:4] + '-' + c[4:]
    print(c)
