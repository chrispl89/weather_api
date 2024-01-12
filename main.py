from requests import get
from json import loads
from terminaltables import AsciiTable

# if you want to check another cities you need to change them below
CITIES = ['Gdańsk', 'Warszawa', 'Kraków', 'Poznań']


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    # you can choose other data. You need to look to the json output and change the rows
    rows = [
        ['City', 'Measurement time', 'Temperature']
    ]
    for row in loads(response.text):
        if row['stacja'] in CITIES:
            # again you need to modify the rows if you want to check other data
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
            ])

    table = AsciiTable(rows)
    print(table.table)


if __name__ == '__main__':
    main()
