#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''
  {
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1999-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1999-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1991-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1991-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1992-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1992-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1993-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1993-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1994-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1994-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1995-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1995-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1996-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1996-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1997-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1997-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },{
    "__metadata": {
      "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P%d')"
    },
    "externalName": "P%d",
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
    "cust_userf": "Admin",
    "cust_timef": "PT10H10M10S",
    "cust_translatablef_defaultValue": "trans1",
    "cust_datef": "/Date(1518480000000)/",
    "cust_translatablef_en_US": "trans1",
    "cust_vw1": [
      {
        "__metadata": {
          "uri": "cust_XAF19281BasicFullPurgePerf(effectiveStartDate=datetime'1998-01-01T00:00:00',externalCode='P10001')"
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
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_1')"
        },
        "externalName": "compL2_1",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_2')"
        },
        "externalName": "compL2_2",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_3')"
        },
        "externalName": "compL2_3",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_4')"
        },
        "externalName": "compL2_4",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_5')"
        },
        "externalName": "compL2_5",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_6')"
        },
        "externalName": "compL2_6",
        "cust_gofield": "GO1",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_7')"
        },
        "externalName": "compL2_7",
        "cust_gofield": "GO2",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_8')"
        },
        "externalName": "compL2_8",
        "cust_gofield": "GO3",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_9')"
        },
        "externalName": "compL2_9",
        "cust_gofield": "GO4",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      },
      {
        "__metadata": {
          "uri": "cust_XAF19281CompL2(cust_XAF19281BasicFullPurgePerf_effectiveStartDate=datetime'1998-01-01T00:00:00',cust_XAF19281BasicFullPurgePerf_externalCode='P%d',externalCode='compL2_10')"
        },
        "externalName": "compL2_10",
        "cust_gofield": "GO5",
        "cust_fofield": "location1",
        "cust_picklistfield": "PK1",
        "cust_translatablefield_en_US": "trans1"
      }
    ]
  },'''

file = open("MultiDateCompJson.txt", "w")
for i in range(2001, 2101, 1):
    pass
    n = ((i - 1) % 5) + 1
    result = s % (
        i, i, n, i, i, i, i, i, i, i, i, i, i, i, i, n, i, i, i, i, i, i, i, i, i, i, i, i, n, i, i, i, i, i, i, i, i,
        i, i, i, i, n, i, i, i, i, i, i, i, i, i, i, i, i, n, i, i, i, i, i, i, i, i, i, i, i, i, n, i, i, i, i, i, i,
        i, i, i, i, i, i, n, i, i, i, i, i, i, i, i, i, i, i, i, n, i, i, i, i, i, i, i, i, i, i, i, i, n, i, i, i, i,
        i, i, i, i, i, i)
    file.write(result)
file.close()
