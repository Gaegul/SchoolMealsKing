from smk.ES import es


def get_meal(date):
    result = es.search(
        index="schoolmeal",
        body={
            'from': 0,
            'size': 100,
            'query': {
                'match': {
                    'Date': date
                }
            }
        }
    )

    response = {
        'breakfast': result['hits']['hits'][0]['_source']['Meal'],
        'lunch': result['hits']['hits'][1]['_source']['Meal'],
        'dinner': result['hits']['hits'][2]['_source']['Meal']
    }

    return response
