#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import csv

writer = csv.writer(open('CSVReader.csv', 'wb'))

data = [('zzz', 20, 123456), ('jojo', 10, 789012)]

writer.writerows(data)
