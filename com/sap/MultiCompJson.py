#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json

s = '''  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO1",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO2",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO3",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO4",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO5",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO1",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO2",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO3",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO4",
    "cust_translatablefield_en_US": "trans1"
  },  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
    },
    "cust_picklistfield": "PK1",
    "cust_fofield": "location1",
    "cust_gofield": "GO5",
    "cust_translatablefield_en_US": "trans1"
  },'''

file = open("MultiCompJson.txt", "w")
for i in range(1901, 2001, 1):
    pass
    result = s % (i, i, i, i, i, i, i, i, i, i)
    file.write(result)
file.close()
