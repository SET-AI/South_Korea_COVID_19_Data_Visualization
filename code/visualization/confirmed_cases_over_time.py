import folium
from folium.features import DivIcon
import datetime
from region_info import loc_dict, time_province
from math import log


class MakeFoliumMap():
    def __init__(self):
        pass

    def run(self, day):
        m = folium.Map([36.4, 128], zoom_start=8)

        # Draw region titles
        for name, loc in loc_dict.items():
            folium.map.Marker(
                [loc[0], loc[1]],
                icon=DivIcon(
                    icon_size=(10,36),
                    icon_anchor=(150, 15),
                    html=f'<div style="font-size: 10pt; border-radius: 5px;  background: #7f7fff; color: white; padding: 0px;'
                         f'border: 1px; opacity: 0.8; text-align: center; vertical-align: middle; width: 150px;  height: 20px;">{name}</div>',
                    )
                ).add_to(m)

        # Draw region points
        for name, loc in loc_dict.items():
            folium.map.Marker(
                [loc[0], loc[1]],
                icon=DivIcon(
                    icon_size=(10,36),
                    icon_anchor=(15,15),
                    html=f'<span style="height: 30px;  width: 30px;  opacity: 0.8;  background-color: #4c4cff;  border-radius: 50%;  display: inline-block;"></span>',
                    )
                ).add_to(m)

        converted_day = datetime.datetime.strptime(day, "%m/%d/%Y").strftime('%Y-%m-%d')
        df_day = time_province[time_province['date'] == converted_day]

        for index, row in df_day.iterrows():
            province = row['province']
            confirmed = row['confirmed']
            print(province, confirmed)

            # Draw route between regions
            folium.Circle([loc_dict[province][0], loc_dict[province][1]], radius=log(confirmed+1)*5000,
                          color='red', fillOpacity=0.5, fill=True).add_to(m)

        day = day.replace('/', '_')
        m.save(f'output/confirmed_{day}.html')


days = ['1/20/2020', '2/20/2020', '3/20/2020']

for day in days:
    MakeFoliumMap().run(day)