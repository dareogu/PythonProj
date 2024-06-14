#!/usr/bin/env python
# -*- encoding: utf-8 -*-

str = '''{
    "__metadata": {
        "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P%d')"
    },
    "externalCode": "P%d",
    "cust_stringf": "str",
    "cust_picklistf": "PK1",
    "cust_booleanf": "false",
    "cust_fof": "LocationXAF19281_FOF",
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
                "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P%d')"
        }
    }],
    "cust_vw2": [{
        "__metadata": {
            "uri": "cust_XAF19281GOF(effectiveStartDate=datetime'1990-01-01T00:00:00',externalCode='GO1')"
        }
    }],
    "cust_compL2": [{
        "__metadata": {
            "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalCode": "compL2_1",
        "cust_gofield": "GO1",
        "cust_translatablefield_en_US": "trans1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_defaultValue": "trans1",
        "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
            },
            "externalCode": "compL2_3",
            "cust_gofield": "GO3",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
            },
            "externalCode": "compL2_2",
            "cust_gofield": "GO2",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
            },
            "externalCode": "compL2_4",
            "cust_gofield": "GO4",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
            },
            "externalCode": "compL2_5",
            "cust_gofield": "GO5",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
            },
            "externalCode": "compL2_6",
            "cust_gofield": "GO1",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
            },
            "externalCode": "compL2_7",
            "cust_gofield": "GO2",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
            },
            "externalCode": "compL2_8",
            "cust_gofield": "GO3",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
            },
            "externalCode": "compL2_9",
            "cust_gofield": "GO4",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    },
        {
            "__metadata": {
                "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
            },
            "externalCode": "compL2_10",
            "cust_gofield": "GO5",
            "cust_translatablefield_en_US": "trans1",
            "cust_picklistfield": "PK1",
            "cust_translatablefield_defaultValue": "trans1",
            "cust_fofield": "LocationXAF19281_FOF"
    }]
},
'''
for i in range(1, 10, 1):
    pass
    n = (i % 5) + 1
    print(str % (i, i, n, i, i, i, i, i, i, i, i, i, i, i))

# for i in range(1, 11):
#     #te = {"uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_%d')"}
#     test = {
#         "__metadata": str(i),
#         "externalCode": "compL2_" + str(i),
#         "cust_gofield": "GO" + str(i),
#         "cust_translatablefield_en_US": "trans1",
#         "cust_picklistfield": "PK1",
#         "cust_translatablefield_defaultValue": "trans1",
#         "cust_fofield": "LocationXAF19281_FOF"
#     }
#     if(i % 5 == 1):
#         d = 1
#
#     if(i % 5 == 2):
#         d = 2
#
#     if(i % 5 == 3):
#         d = 3
#
#     if(i % 5 == 4):
#         d = 4
#
#     if(i % 5 == 0):
#         d = 5
#
#     print(json.dumps(test))


#     for i in range(1, 11):
#         Ecode = 'P' + str(i)
#         dic1 = {'type': 'dic1', 'username': 'loleina', 'age': Ecode}
#         json_dic1 = json.dumps(dic1)
#         # print json_dic1
#         json_dic2 = json.dumps(dic1, sort_keys=True, indent=4, separators=(
#             ',', ': '), encoding="gbk", ensure_ascii=True)
#         print json_dic2

# for i in range(1, 11):
# Ecode = "P" + str(i)
# print Ecode
#     var = {"__metadata": {
#         "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P1')"
#     },
#         "externalCode": Ecode}
#     print(json.dumps(var))
# print(test % (i, i))
