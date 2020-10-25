import folium
from folium.features import DivIcon
from region_info import loc_dict, movement


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


        df_day = movement[movement['date'] == day]

        for col in df_day.columns:
            if col == 'date':
                continue

            # Get two regions from the column name
            regions = col.split(">")

            if regions[0] == regions[1]:
                continue

            if regions[0] == 'Jeju-do' or regions[1] == 'Jeju-do':
                continue

            # get a row from this col
            moving_amount = df_day[col].tolist()[0]

            if moving_amount <= 0:
                continue

            # Make two points for a route
            points = []
            points.append(tuple([loc_dict[regions[0]][0], loc_dict[regions[0]][1]]))
            points.append(tuple([loc_dict[regions[1]][0], loc_dict[regions[1]][1]]))

            # Draw route between regions
            folium.PolyLine(points, color="green", weight=moving_amount*0.0002, opacity=0.5).add_to(m)

        day = day.replace('/', '_')
        m.save(f'output/movement_{day}.html')


days = ['1/20/2020', '2/20/2020', '3/20/2020']
# days = ['2/20/2020']

for day in days:
    MakeFoliumMap().run(day)