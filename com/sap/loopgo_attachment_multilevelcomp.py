#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = ''' {
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1990-01-01T00:00:00',externalCode='I%d')"
    },
    "externalName": "I%d",
    "cust_stringf": "str",
    "cust_picklistf": "PK1",
    "cust_booleanf": false,
    "cust_fof": "location1",
    "cust_gof": "GO%d",
    "cust_numberf": "1",
    "cust_datasourcef": "ManageOrganizationPayAndJobStructures",
    "cust_datetimef": "/Date(1518487810000+0000)/",
    "cust_decimalf": "1.1",
    "cust_userf": "admin",
    "cust_timef": "PT9H9M9S",
    "cust_translatablef_defaultValue": "trans5",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans5",
    "cust_attachmentfNav": {
      "__metadata": {
        "uri": "Attachment(50L)"
      }
    },
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1990-01-01T00:00:00',externalCode='P10001')"
        }
      }
    ],
    "cust_vw2": [
      {
        "__metadata": {
          "uri": "cust_XAF19281GOF(effectiveStartDate=datetime'1990-01-01T00:00:00',externalCode='GO1')"
        }
      }
    ],
    "cust_compL2": [
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans4",
        "cust_compL3": [
          {
            "__metadata": {
              "uri": "cust_XAF21099CompL3(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',cust_XAF19281CompL2_externalCode='compL2_7',externalCode='compL3_3')"
            },
            "externalName": "compL3_3",
            "cust_gofield": "GO2",
            "cust_fofield": "location1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_en_US": "trans6"
          }
        ]
      }
    ]
  },
  {
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1991-01-01T00:00:00',externalCode='I%d')"
    },
    "externalCode": "I%d"
  },'''

file = open("loopgo_attachment_multilevelcomp.txt", "w")
for i in range(1, 501, 1):
    pass
    n = ((i - 1) % 5) + 1
    result = s % (i, i, n, i, i, i, i)
    file.write(result)
file.close()
