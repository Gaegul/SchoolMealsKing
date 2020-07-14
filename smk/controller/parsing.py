import requests
import json
import re
from flask import abort

from smk import PARSING_URL, PARSING_KEY
from smk.ES import es


def parsing(start_date, end_date):
    try:
        params = {'KEY': PARSING_KEY,
                 'Type': 'json',
                 'pIndex': 1,
                 'pSize': 1000,
                 'ATPT_OFCDC_SC_CODE': 'G10',
                 'SD_SCHUL_CODE': '7430310',
                 'MLSV_FROM_YMD': start_date,
                 'MLSV_TO_YMD': end_date
            }

        response = requests.get(PARSING_URL, params)

        result = json.loads(response.text)

        meals = result['mealServiceDietInfo'][1]['row']

        for meal in meals:
            body = {
                'Date': meal['MLSV_YMD'],
                'Meal': re.split("[^ \u3131-\u3163\uac00-\ud7a3]+", meal['DDISH_NM']),
                'Type': meal['MMEAL_SC_NM']
            }
            es.index(index="schoolmeal", body=body)

        es.indices.refresh(index='schoolmeal')

        meal_count = len(meals)

        return {
            "message": f"{start_date}에서 {end_date}사이의 급식 {meal_count}만큼 ES에 저장되었습니다."
        }

    except KeyError:
        return abort(500, "server error")
