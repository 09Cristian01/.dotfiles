# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# from libqtile.utils import guess_terminal

# everforest theme (from sainnhe's github)
colors = {
    "bg-dim": "#1E2326",
    "bg0": "#272E33",
    "bg1": "#2E383C",
    "bg2": "#374145",
    "bg3": "#414B50",
    "bg4": "#495156",
    "bg5": "#4F5B58",
    "bg-visual": "#4C3743",
    "bg-red": "#493B40",
    "bg-green": "#3C4841",
    "bg-blue": "#384B55",
    "bg-yellow": "#45443c",
    "default": "#D3C6AA",
    "fg-red": "#E67E80",
    "fg-orange": "#E69875",
    "fg-yellow": "#DBBC7F",
    "fg-green": "#A7C080",
    "fg-aqua": "#83C092",
    "fg-blue": "#7FBBB3",
    "fg-purple": "#D699B6",
    "fg-grey0": "#7A8478",
    "fg-grey1": "#859289",
    "fg-grey2": "#9DA9A0",
    "statusline0": "#A7C080",
    "statusline1": "#D3C6AA",
    "statusline2": "#E67E80",
}

font_settings = {
    "default": "sans",
    "size": 16,
}

bar_settings = {
    "bg-color": colors["bg-dim"],
    "active-color": colors["default"],
    "size": 20,
}


# User's functions space
def print_rounded_corner(
    left: bool,
    bg_color: str = colors["bg-dim"],
    fg_color: str = colors["bg2"],
):
    if left:
        return widget.TextBox(
            "",  # nf-ple-left_half_circle_thick
            background=bg_color,
            foreground=fg_color,
            font=font_settings["default"],
            fontsize=bar_settings["size"] + 5,
            padding=-1,
        )

    else:
        return widget.TextBox(
            "",  # nf-ple-right_half_circle_thick
            background=bg_color,
            foreground=fg_color,
            font=font_settings["default"],
            fontsize=bar_settings["size"] + 5,
            padding=0,
        )


mod = "mod4"
alt = "mod1"

terminal = "kitty"
editor = "kitty nvim"  # "kitty helix"
file_manager = "kitty ranger"
task_manager = "kitty btop"
menu = "rofi -show run"
browser = "librewolf"
screenshot = "flameshot gui"
ide = "codium --user-data-dir $HOME/Projects/.vscodiumConfigs/python/profile/ --extensions-dir $HOME/Projects/.vscodiumConfigs/python/plugins/"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn(menu), desc="Open menu"),
    Key([mod, alt], "e", lazy.spawn(editor), desc="Open helix"),
    Key([mod, alt], "b", lazy.spawn(browser), desc="Open libreoffice"),
    Key([mod, alt], "f", lazy.spawn(file_manager), desc="Open ranger"),
    Key([mod, alt], "t", lazy.spawn(task_manager), desc="Open btop"),
    Key(
        [mod], "Print", lazy.spawn(screenshot), desc="Take a screenshot with flameshot"
    ),
    # Key([mod, alt], "", lazy.spawn(), desc=""),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"),
        desc="Raise Volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"),
        desc="Lower Volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Raise Volume",
    ),
]

# Icon names list
# 1. nf-linux-archlinux
# 2. nf-oct-browser
# 3. nf-oct-terminal
# 4. nf-fa-folder_open
# 5. nf-md-file_code
# 6. nf-dev-git_branch
# 7. nf-seti-config /  nf-fa-flask / nf-cod-settings
# 8.
# 9.
# ALERT: Limit of groups 9

groups = [
    Group(i)
    for i in [
        "   ",
        "   ",
        "   ",
        "   ",
        " 󰈮 ",
        "  ",
        "   ",  # 
    ]
]

for index, group in enumerate(groups):
    index = str(index + 1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                index,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                index,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Floating(
    #    border_focus=colors["fg-green"],
    #    border_normal=colors["bg-green"],
    #    border_width=1,
    # ),
    layout.Columns(
        border_focus=colors["fg-green"],
        border_normal=colors["bg-green"],
        border_width=1,
        single_border_width=True,
        single_margin=True,
        grow_amount=3,
    ),
    layout.Tile(
        border_focus=colors["fg-green"],
        border_normal=colors["bg-green"],
        border_width=1,
        single_border_width=True,
        single_margin=True,
    ),
    layout.MonadWide(
        border_focus=colors["fg-green"],
        border_normal=colors["bg-green"],
        border_width=1,
        single_border_width=True,
        single_margin=True,
    ),
    layout.TreeTab(
        bg_color=colors["bg-dim"],
        active_bg=colors["bg-yellow"],
        inactive_bg=colors["bg1"],
        urgent_bg=colors["bg-red"],
        font=font_settings["default"],
        fontsize=font_settings["size"],
        active_fg=colors["fg-yellow"],
        inactive_fg=colors["fg-aqua"],
        urgent_fg=colors["fg-red"],
        border_width=0,
        margin_left=0,
        margin_y=0,
        padding_left=10,
        padding_x=-5,
        padding_y=2,
        previous_on_rm=True,
        section_fg=colors["fg-blue"],
        section_fontsize=14,
        section_top=6,
        section_left=60,
        section_bottom=6,
        section_padding=6,
        sections=["Main"],
        vspace=5,
    ),
    # layout.Stack(autosplit=True),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(
    #    border_focus=colors["fg-green"],
    #    border_normal=colors["bg-green"],
    #    border_width=1,
    #    single_border_width=True,
    #    single_margin=True,
    # ),
    # layout.RatioTile(),
    # layout.Slice(),
    # layout.VerticalTile(),
    layout.Zoomy(columnwidth=250),
    layout.Max(),
]

widget_defaults = dict(
    font=font_settings["default"],
    fontsize=font_settings["size"],
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=colors["bg2"],
                    foreground=colors["default"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    # scroll=True,
                    scale=0.6,
                ),
                widget.GroupBox(
                    active=colors["default"],
                    inactive=colors["fg-grey2"],
                    highlight_method="block",
                    # highlight_color=[colors["bg-blue"], colors["fg-blue"]],
                    background=colors["bg2"],
                    borderwidth=3,
                    disable_drag=True,
                    font_size=font_settings["size"],
                    # foreground=colors["fg-orange"],
                    font=font_settings["default"],
                    margin_y=3,
                    margin_x=0,
                    other_current_screen_border=colors["fg-grey0"],
                    other_screen_border=colors["bg-yellow"],
                    this_current_screen_border=colors["fg-grey0"],
                    this_screen_border=colors["bg-blue"],
                    padding_y=5,
                    padding_x=0,
                    rounded=False,
                    urgent_alert_method="block",
                    urgent_border=colors["bg-yellow"],
                    urgent_text=colors["fg-yellow"],
                ),
                widget.Prompt(
                    background=colors["bg5"],
                    foreground=colors["default"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    bell_style="visual",
                    cursor=False,
                    ignore_dups_history=True,
                    max_history=10,
                    record_history=False,
                    visual_bell_color=colors["fg-red"],
                    prompt=" 󰉺  ",  # nf-md-format_list_bulleted_type
                ),
                print_rounded_corner(False),
                widget.WindowName(
                    background=colors["bg-dim"],
                    foreground=colors["default"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    empty_group_string=" ",  # nf-oct-circle / nf-cod-circle
                    format="  {name}",  # nf-fa-circle / nf-cod-circle_filled
                ),
                # widget.Backlight(),
                # widget.KeyboardKbdd(configured_keyboards=["us", "es", "pt"],)
                print_rounded_corner(True),
                widget.Notify(
                    background=colors["bg-yellow"],
                    background_low=colors["bg-blue"],
                    background_urgent=colors["bg-red"],
                    foreground=colors["fg-yellow"],
                    foreground_low=colors["fg-blue"],
                    foreground_urgent=colors["fg-red"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    # audiofile=True,
                    default_timeout=60,
                    default_timeout_low=30,
                    default_timeout_urgent=120,
                    action=False,
                    fmt="󱅫 {}",  # nf-md-bell_badge
                ),
                widget.PulseVolume(
                    background=colors["bg2"],
                    foreground=colors["default"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    # cardid=None,
                    channel="Master",
                    device="default",
                    # check_mute_command=None,
                    # check_mute_string="muted",
                    # get_volume_command=None,
                    # volume_down_command=None,
                    # volume_up_command=None,
                    # volume_app="pamixer",
                    scroll=True,
                    step=10,
                    limit_max_volume=True,
                    fmt=" 󰕾  {}",  # nf.md-volume_high
                    emoji=False,
                    emoji_list=[
                        " 󰸈 ",  # nf-md-volume_variant_off
                        " 󰕿 ",  # nf-md-volume_low
                        " 󰖀 ",  # nf-md-volume_medium
                        " 󰕾 ",  # nf-md-volume_high
                    ],
                    mouse_callbacks={},
                    update_interval=1.0,
                ),
                widget.KeyboardLayout(
                    background=colors["bg2"],
                    foreground=colors["default"],
                    configured_keyboards=["es", "pt"],  # "fr", "us"],
                    display_map={
                        "es": " 󰬚 ",  # nf-md-alpha_s_box
                        "pt": " 󰬗 ",  # nf-md-alpha_p_box
                        # "fr":" 󰬍 ", #nf-md-alpha_f_box
                        # "us":" 󰬜 ", #nf-md-alpha_u_box
                    },
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    mouse_callbacks={
                        "Button1": lazy.widget["keyboardlayout"].next_keyboard(),
                    },
                    # colours=[colors["fg-yellow"], colors["fg-aqua"]],
                ),
                print_rounded_corner(False, bg_color=colors["bg0"]),
                widget.Battery(
                    background=colors["bg0"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    format="{char} {percent:2.0%}",
                    foreground=colors["statusline0"],
                    show_short_text=False,
                    update_interval=1,
                    notification_timeout=0,
                    # low_background,
                    low_foreground=colors["statusline2"],
                    low_percentage=0.25,
                    notify_below=26,
                    charge_char=" 󰂏 ",  # nf-md-battery_plus_variant
                    discharge_char=" 󰂌 ",  # nf-md-battery_minus_variant
                    empty_char=" 󰂃 ",  # nf-md-battery_alert
                    full_char=" 󰁹 ",  # nf-md-battery
                    unknown_char=" 󰂑 ",  # nf-md-battery_unknown
                ),
                # widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(),
                # "%Y-%m-%d %a %I:%M %p"),
                # icons
                # clock => nf-seti-time_cop
                # calendar => nf-md-calendar
                widget.Clock(
                    format="   %Hh%M  󰃭  %d/%m/%Y",
                    background=colors["bg0"],
                    foreground=colors["default"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                ),
                print_rounded_corner(True, bg_color=colors["bg0"]),
                widget.WidgetBox(
                    background=colors["bg2"],
                    foreground=colors["default"],
                    close_button_location="right",
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    text_closed=" 󱊖 ",  # nf-md-tray
                    text_open=" 󱊔 ",  # nf-md-tray_full
                    widgets=[
                        widget.Memory(
                            background=colors["bg5"],
                            foreground=colors["default"],
                            font=font_settings["default"],
                            fontsize=font_settings["size"],
                            measure_mem="M",
                            format="   {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",  #  󰾶  {SwapUsed: .0f}{ms}/{SwapTotal:.0f}{ms}",
                            # nf-fae-chip
                            # nf-md-folder_swap
                        ),
                        widget.CPU(  # CPU 1
                            background=colors["bg5"],
                            foreground=colors["default"],
                            font=font_settings["default"],
                            fontsize=font_settings["size"],
                            # padding=3,
                            format="    {load_percent}%",  # nf-oct-cpu
                        ),
                        widget.CPU(  # CPU 2
                            background=colors["bg5"],
                            foreground=colors["default"],
                            font=font_settings["default"],
                            fontsize=font_settings["size"],
                            # padding=3,
                            format="    {load_percent}%",  # nf-oct-cpu
                        ),
                        widget.ThermalZone(
                            zone="/sys/class/thermal/thermal_zone0/temp",
                            crit=65,
                            high=60,
                            background=colors["bg5"],
                            foreground=colors["statusline1"],
                            fgcolor_normal=colors["fg-aqua"],
                            fgcolor_high=colors["fg-yellow"],
                            fgcolor_crit=colors["fg-red"],
                            font=font_settings["default"],
                            fontsize=font_settings["size"],
                            # tag_sensor="acpitz-0",
                            format=" 󰡵  {temp}ºC",  # nf-md-gauge_low
                            format_high=" 󰊚  {temp}ºC",  # nf-md-gauge
                            format_crit=" 󰡴  {temp}ºC",  # nf-md-gauge_full
                        ),
                        widget.DF(
                            background=colors["bg5"],
                            foreground=colors["default"],
                            visible_on_warn=False,
                            font=font_settings["default"],
                            fontsize=font_settings["size"],
                            measure="G",
                            warn_color=colors["statusline2"],
                            warn_space=10,
                            partition="/home",
                            format=" 󰋊  {r:.0f}%",  # nf-md-harddisk
                        ),
                        widget.Net(
                            background=colors["bg5"],
                            foreground=colors["default"],
                            font=font_settings["default"],
                            fontsize=font_settings["size"],
                            interface=None,
                            prefix="M",
                            format="   {down}   {up}",  # nf-fa-wifi / nf-fa-arrow_circle_down / nf-fa-arrow_circle_up
                        ),
                    ],
                ),
                widget.QuickExit(
                    background=colors["bg2"],
                    foreground=colors["fg-red"],
                    font=font_settings["default"],
                    fontsize=font_settings["size"],
                    padding=5,
                    countdown_format=" {} ",  # nf-fa-power_off
                    default_text="  ",  # nf-fa-power_off
                ),
            ],
            30,
            background=bar_settings["bg-color"],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])
