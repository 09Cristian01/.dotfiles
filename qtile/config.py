import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Match, Screen, Key
from libqtile.lazy import lazy

# from qtile_extras import widget
# from qtile_extras.widget.decorations import RectDecoration

import keymaps as k
import color_scheme as s
import functions as f

keys = k.keys
groups = k.groups

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [k.mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [k.mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([k.mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        **s.layout_theme,
    ),
    layout.Tile(
        **s.layout_theme,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # right=bar.Gap(50),
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.Spacer(
                    length=12,
                    **s.widget_theme,
                ),
                widget.GroupBox(
                    highlight_method="block",
                    active=s.palette["black"],
                    disable_drag=True,
                    hide_unused=True,
                    rounded=False,
                    margin_x=0,
                    inactive=s.palette["gray"],
                    this_current_screen_border=s.palette["active"],
                    this_screen_border=s.palette["inactive"],
                    other_current_screen_border=s.palette["active"],
                    other_screen_border=s.palette["inactive"],
                    urgent_alert_method="block",
                    urgent_border=s.palette["alert"],
                    urgent_text=s.palette["alert"],
                    **s.widget_theme,
                ),
                widget.Prompt(**s.widget_theme),
                widget.WindowName(
                    # font=font["name"],
                    max_chars=100,
                    parse_text=f.parse_names,
                    **s.widget_theme,
                ),
                # widget.Chord(
                #     chords_colors={
                #    "launch": ("#ff0000", "#ffffff"),
                # },
                # name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                widget.CurrentLayoutIcon(
                    **s.widget_theme,
                ),
                widget.CheckUpdates(
                    colour_have_updates=s.palette["purple"],
                    fmt="Updates: {}",
                    initial_text="...",
                    no_update_string="0",
                    distro="Arch_checkupdates",
                    update_interval=60 * 5,
                    **s.widget_theme,
                ),
                widget.Battery(
                    format="{char} {percent:2.0%} {hour:d}h{min:02d}",
                    low_background=s.palette["alert"],
                    low_percentage=0.25,
                    **s.widget_theme,
                ),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                widget.Clock(
                    format="%Y/%m/%d %H:%M",
                    **s.widget_theme,
                ),
                widget.QuickExit(
                    **s.widget_theme,
                ),
                widget.Spacer(
                    length=12,
                    **s.widget_theme,
                ),
            ],
            24,
            border_width=0,
            margin=5,
            **s.widget_theme,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [k.mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [k.mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([k.mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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

### EDITED BY THE USER ###
"""
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/cristian/.config/qtile/autostart.sh')
    subprocess.Popen([home])
"""


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])
