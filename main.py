

import requests

name_intelligence = {}


def get_request(name):

    files_url = "https://superheroapi.com/api/2619421814940190/search/"f'{name}'
    response = requests.get(files_url)
    return response.json()


def get_name_id(name):

    intelligence_of_char = get_request(name)['results']
    for val in intelligence_of_char:
        dict_int = dict(val["powerstats"])
        intelligence = dict_int['intelligence']
        return intelligence


if __name__ == '__main__':
    name_intelligence['Hulk'] = int(get_name_id('Hulk'))
    name_intelligence['Captain America'] = int(get_name_id('Captain America'))
    name_intelligence['Thanos'] = int(get_name_id('Thanos'))

    print(f'Самый умный - {max(name_intelligence, key=name_intelligence.get)},'
          f' его интеллект целых {max(name_intelligence.values())} единиц!!! Жесть!')


