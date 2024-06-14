#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''{
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='CompL2_1')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO1",
    "cust_translatablefield_en_US": "trans1"
  },'''

file = open("comp_writer.txt", "w")
for i in range(1, 101, 1):
    pass
    result = s % (i)
    file.write(result)
file.close()
