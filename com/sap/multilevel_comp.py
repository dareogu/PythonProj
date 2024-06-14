#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''
  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_1')"
    },
    "externalName": "compL2_1",
    "cust_gofield": "GO1",
    "cust_fofield": "location1",
    "cust_picklistfield": "PK1",
    "cust_translatablefield_en_US": "trans1",
    "cust_compL3": [
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_1',externalCode='compL3_1')"
        },
        "externalName": "compL3_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_1',externalCode='compL3_2')"
        },
        "externalName": "compL3_2",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },
  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_2')"
    },
    "externalName": "compL2_2",
    "cust_gofield": "GO2",
    "cust_fofield": "location1",
    "cust_picklistfield": "PK1",
    "cust_translatablefield_en_US": "trans1",
    "cust_compL3": [
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_2',externalCode='compL3_1')"
        },
        "externalName": "compL3_1",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_2',externalCode='compL3_2')"
        },
        "externalName": "compL3_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },
  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_3')"
    },
    "externalName": "compL2_3",
    "cust_gofield": "GO3",
    "cust_fofield": "location1",
    "cust_picklistfield": "PK1",
    "cust_translatablefield_en_US": "trans1",
    "cust_compL3": [
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_3',externalCode='compL3_1')"
        },
        "externalName": "compL3_1",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_3',externalCode='compL3_2')"
        },
        "externalName": "compL3_2",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },
  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_4')"
    },
    "externalName": "compL2_4",
    "cust_gofield": "GO4",
    "cust_fofield": "location1",
    "cust_picklistfield": "PK1",
    "cust_translatablefield_en_US": "trans1",
    "cust_compL3": [
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_4',externalCode='compL3_1')"
        },
        "externalName": "compL3_1",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_4',externalCode='compL3_2')"
        },
        "externalName": "compL3_2",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },
  {
    "__metadata": {
      "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_5')"
    },
    "externalName": "compL2_5",
    "cust_gofield": "GO5",
    "cust_fofield": "location1",
    "cust_picklistfield": "PK1",
    "cust_translatablefield_en_US": "trans1",
    "cust_compL3": [
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_5',externalCode='compL3_1')"
        },
        "externalName": "compL3_1",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF21099CompL3(cust_XAF19281CompL2_externalCode='compL2_5',externalCode='compL3_2')"
        },
        "externalName": "compL3_2",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },'''

file = open("multilevel_comp.txt", "w")
for i in range(1, 1001, 1):
    pass
    result = s % (i, i, i, i, i)
    file.write(result)
file.close()
