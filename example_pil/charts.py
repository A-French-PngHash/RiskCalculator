import datetime
import os
from PIL import ImageFont, Image, ImageDraw


def combine_hex_values(d : dict):
    """
    Combine the hex values given in the dictionary.

    :param d: Dictionary of colors as keys with the percentage (between 0 and 1) as values.
    """
    d_items = sorted(d.items())
    tot_weight = sum(d.values())
    red = int(sum([int(k[:2], 16)*v for k, v in d_items])/tot_weight)
    green = int(sum([int(k[2:4], 16)*v for k, v in d_items])/tot_weight)
    blue = int(sum([int(k[4:6], 16)*v for k, v in d_items])/tot_weight)
    zpad = lambda x: x if len(x)==2 else '0' + x
    return zpad(hex(red)[2:]) + zpad(hex(green)[2:]) + zpad(hex(blue)[2:])

def draw_activity_charts(connection_data: [[int]], is_global_guild_activity : bool, id : int, last_day : datetime.datetime):
    """
    Draw activity charts and output it to output.png.

    :param connection_data: When the user was connected. List of x days with each day having 24 element (one for each
    hour). Each element is the number of minutes connected during the hour.
    :param is_global_guild_activity: If the activity data passed is for the whole guild. If set to False, it means it is
     the activity of one user.
    :param id: The guild/user id.
    :param last_day: The last day of the connection data. (the latest day)
    """

    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    number_of_days = len(connection_data)

    with Image.open(f"{os.path.dirname(os.path.abspath(__file__))}/activity chart.jpg") as im:
        title_font = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}/Fonts/Uni Sans Heavy.otf",
                                        size=30)
        body_font = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}/Fonts/Uni Sans Thin.otf", size=20)
        width_taken_by_times = 70  # The total width taken by the times at the left.
        xbegin = 70  # The left beginning of the rectangles.
        length = 80  # The length of a rectangle.
        y_begin_offset = 63  # The beginning of the rectangles on the y axis.

        draw = ImageDraw.Draw(im)

        if is_global_guild_activity:
            draw.text((165, 10), f"Activite du serveur {id}", fill=(0, 0, 0), font=title_font)
        else:
            draw.text((200, 10), f"Activite de {id}", fill=(0, 0, 0), font=title_font)

        # Adding the color rectangles
        for (index, connected_at) in enumerate(connection_data):
            current_day = last_day - datetime.timedelta(days=number_of_days - index - 1)
            week_day = week_days[current_day.isoweekday() - 1]
            draw.text((xbegin + 13, 40), f"{week_day} {current_day.day}", fill=(0, 0, 0), font=body_font)
            for i in range(24):
                values = combine_hex_values(
                        {"7600FB": connected_at[i] / 60, "E2D3F4": 1 - connected_at[i] / 60})
                print(values, connected_at[i], 1 - connected_at[i] / 60)
                if values == "3a0x73fe":
                    pass
                draw.rectangle(
                    [(xbegin, i * 17.55 + y_begin_offset), (xbegin + length, i * 17.55 + 10 + y_begin_offset)],
                    fill="#" + values)
            xbegin += length + 20

    im.save(f"{os.path.dirname(os.path.abspath(__file__))}/output.png", "PNG")