from flask import abort

from smk.ES import es


def get_meal(date):
    try:
        result = es.search(
            index="schoolmeal",
            body= {
                'from': 0,
                'size': 100,
                'query': {
                    'match': {
                        'Date': date
                    }
                }
            }
        )

        return {
            '조식': result['hits']['hits'][0]['_source']['Meal'],
            '중식': result['hits']['hits'][1]['_source']['Meal'],
            '석식': result['hits']['hits'][2]['_source']['Meal']
        }

    except RuntimeError:
        return abort(500, "server error")
