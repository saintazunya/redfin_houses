import pandas as pd
import io

from redfin_houses.house_filter import HouseFilter, PropertyTypeEnum, PriceEnum, SqftEnum, BathEnum, LotEnum
from redfin_houses.redfin import query_house_list
from datetime import datetime

def convert_csv_to_dataframe(csv):
    f = io.StringIO(csv)
    df = pd.read_csv(f)
    return df


def get_property_by_zip_code(zipcode, filter=None):
    print("Searching within zipcode: {}".format(zipcode))
    print("Applying filter: {}".format(filter.to_query_str()))
    response = query_house_list("zipcode/{}".format(zipcode), filter)
    return response
def get_property_by_city(city, filter=None):
    print("Searching within city: {}".format(city))
    print("Applying filter: {}".format(filter.to_query_str()))
    response = query_house_list(f"{city}", filter)
    return response

if __name__ == "__main__":
    import logging

    logging.basicConfig(encoding='utf-8', level=logging.INFO)

    house_filter = HouseFilter(
        property_type_list=[PropertyTypeEnum.HOUSE],
        max_price=PriceEnum.PRICE_1M,
        sold=True
    )
    zipcode = [98004, 98005,98007,98006,98029,98052,98033,98034,98073]
    redmond = 'city/14913/WA/Redmond/'
    bellevue = 'city/1387/WA/Bellevue'
    issaquah = 'city/8645/WA/Issaquah'
    kirkland = "city/9148/WA/Kirkland"
    # houses_csv = get_property_by_zip_code(zipcode, filter=house_filter)
    houses_csv = get_property_by_city(kirkland, filter=house_filter)
    df_houses = convert_csv_to_dataframe(houses_csv)
    city = kirkland
    with pd.option_context('display.max_columns', None, 'display.expand_frame_repr', False, 'max_colwidth', -1):
        df_houses.to_csv(f'./data/{city.split("/")[-1]}-{datetime.now()}')
        print(df_houses)
