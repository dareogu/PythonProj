#!/usr/bin/env python
# -*- encoding: utf-8 -*-

s = '''{
        "__metadata": {
            "uri": "odata/v2/cust_SUPTForUserBasedWF(effectiveStartDate=datetime'19%d-01-01T00:00:00',externalCode='admin1')"
        },
        "externalCode": "admin1",
        "externalNameTranslationTextNav": [
            {
                "__metadata": {
                    "uri": "odata/v2/MDFLocalizedValue('defaultValue')"
                },
                "locale": "defaultValue",
                "value": "German%d"
            },
            {
                "__metadata": {
                    "uri": "odata/v2/MDFLocalizedValue('de_DE')"
                },
                "locale": "de_DE",
                "value": "German%d"
            },
            {
                "__metadata": {
                    "uri": "odata/v2/MDFLocalizedValue('en_GB')"
                },
                "locale": "en_GB",
                "value": "US%d"
            },
            {
                "__metadata": {
                    "uri": "odata/v2/MDFLocalizedValue('fr_FR')"
                },
                "locale": "fr_FR",
                "value": "FrFR%d"
            },
            {
                "__metadata": {
                    "uri": "odata/v2/MDFLocalizedValue('ja_JP')"
                },
                "locale": "ja_JP",
                "value": "你好日本%d"
            },
            {
                "__metadata": {
                    "uri": "odata/v2/MDFLocalizedValue('zh_CN')"
                },
                "locale": "zh_CN",
                "value": "你好中国%d"
            }
        ]
    },
'''

file = open("multi_locale_json.txt", "w")
for i in range(11, 61):
    pass
    result = s % (i, i, i, i, i, i, i)
    file.write(result)
file.close()
