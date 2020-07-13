import requests
import json
from flask import abort

from smk import PARSING_URL, PARSING_KEY
from smk.ES import es, make_index


def parsing(start_date, end_date):
    try:
        make_index(es, "smk")
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
                'Type': meal['MMEAL_SC_NM'],
                'Meal': meal['DDISH_NM'],
                'Date': meal['MLSV_YMD']
            }
            es.index(index="smk", doc_type='string', body=body)

        es.indices.refresh(index='smk')

        meal_count = len(meals)

        return {
            "message": f"{start_date}에서 {end_date}사이의 급식 {meal_count}만큼 ES에 저장되었습니다."
        }

    except RuntimeError:
        return abort(500, "server error")
