palette = {  # OneDark theme
    "black": "282C34",
    "red": "E06C75",
    "green": "98C379",
    "yellow": "E5C07B",
    "blue": "61AFEF",
    "purple": "C678DD",
    "cyan": "56B6C2",
    "gray": "ABB2BF",
}
palette["active"] = palette["green"]
palette["inactive"] = palette["yellow"]
palette["alert"] = palette["red"]

widget_theme = {
    "background": palette["black"],
    "foreground": palette["gray"],
    "font": "Ubuntu Bold",
    "fontsize": 12,
    # "max_chars": 50,
}

layout_theme = {
    "margin": 5,
    "margin_on_single": 5,
    "single_border_width": 0,
    "border_on_single": False,
    "border_width": 3,
    "grow_amount": 5,
    "border_focus": palette["active"],
    "border_normal": palette["gray"],  # palette["inactive"],
}
