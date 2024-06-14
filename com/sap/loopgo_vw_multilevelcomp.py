#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''
{
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
    "cust_clobf": "this is clob",
    "cust_datetimef": "/Date(1518487810000+0000)/",
    "cust_decimalf": "1.1",
    "cust_userf": "admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [{
        "__metadata": {
            "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1990-01-01T00:00:00',externalCode='I%d')"
        }
    }],
    "cust_vw2": [{
        "__metadata": {
            "uri": "cust_XAF19281GOF(effectiveStartDate=datetime'1990-01-01T00:00:00',externalCode='GO1')"
        }
    }],
    "cust_compL2": [{
        "__metadata": {
            "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1990-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='I%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1",
        "cust_compL3": [{
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
    }]
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
        "cust_compL3": [{
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
    }]
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
        "cust_compL3": [{
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
    }]
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
        "cust_compL3": [{
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
    }]
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
        "cust_compL3": [{
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
    }]
    }]
},'''

file = open("loopgo_vw_multilevelcomp.txt", "w")
for i in range(1, 1001, 1):
    pass
    n = ((i - 1) % 5) + 1
    result = s % (i, i, n, i, i, i, i, i, i)
    file.write(result)
file.close()
