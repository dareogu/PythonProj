#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''
{
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_1')"
    },
    "externalName": "compL2_1u",
    "cust_gofield": "GO%d",
    "cust_fofield": "location1",
    "cust_picklistfield": "PK1",
    "cust_translatablefield_en_US": "CompL2trans",
    "cust_compL3": [
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',cust_XAF19281CompL2_externalCode='compL2_1',externalCode='compL3_3')"
        },
        "externalName": "compL3_3",
        "cust_gofield": "GO%d",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "CompL3trans"
      }
    ]
  },
  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_6')"
    },
    "externalName": "compL2_6",
    "cust_gofield": "GO1",
    "cust_fofield": "location1",
    "cust_picklistfield": "PK1",
    "cust_translatablefield_en_US": "trans2",
    "cust_compL3": [
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',cust_XAF19281CompL2_externalCode='compL2_6',externalCode='compL3_1')"
        },
        "externalName": "compL3_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans3"
      }
    ]
  },'''

file = open("multilevel_comp_loopgo.txt", "w")
for i in range(1, 501, 1):
    pass
    n = (i % 5) + 1
    m = ((i - 1) % 5) + 1
    result = s % (i, n, i, n, i, m, i, m)
    file.write(result)
file.close()
