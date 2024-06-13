#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''
{
    "__metadata": {
        "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1999-01-01T00:00:00',externalCode='N%d')"
    },
    "externalName": "N%d",
    "cust_stringf": "str",
    "cust_picklistf": "PK1",
    "cust_booleanf": false,
    "cust_fof": "location1",
    "cust_gof": "GO%d",
    "cust_numberf": "1",
    "cust_datasourcef": "ManageOrganizationPayAndJobStructures",
    "cust_clobf": "this is clob",
    "cust_datetimef": "\/Date(1518487810000+0000)\/",
    "cust_decimalf": "1.1",
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "\/Date(1518480000000)\/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [{
        "__metadata": {
                "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
        }
    }],
    "cust_vw2": [{
        "__metadata": {
            "uri": "cust_XAF19281GOF(effectiveStartDate=datetime'1990-01-01T00:00:00',externalCode='GO1')"
        }
    }]
},'''

file = open("LoopGoJsonWithVW.txt", "w")
for i in range(1, 1001, 1):
    pass
    n = ((i - 1) % 5) + 1
    result = s % (i, i, n)
    file.write(result)
file.close()
