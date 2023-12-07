from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
T = "Tab"
R = "Return"
A = "mod1"
M = "mod4"
C = "control"
S = "shift"
P = "space"

TMUX = "tmux new"
EDITOR = f"kitty {TMUX} nvim"
BROWSER = "thorium-browser"
TERMINAL = f"kitty {TMUX}"
CONSOLE = "zsh"
MENU = "rofi"
TASK_MANAGER = "kitty btop"
FILE_MANAGER = "kitty ranger"

keys = [
    # vvv ARROWS vvv
    #   Change focus
    Key([M], T, lazy.layout.next(), desc="Move focus to other window"),
    ###
    Key([M], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([M], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([M], "j", lazy.layout.down(), desc="Move focus down"),
    Key([M], "k", lazy.layout.up(), desc="Move focus up"),
    #   Rezise
    Key([M], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    ###
    Key([M, C], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([M, C], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([M, C], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([M, C], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #   Move window
    Key([M, S], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([M, S], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([M, S], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([M, S], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # ^^^ ARROWS ^^^
    # vvv SYSTEM vvv
    Key([M, C], "r", lazy.reload_config(), desc="Reload the config"),
    Key([M, C], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([M], "w", lazy.window.kill(), desc="Kill focused window"),
    # ^^^ SYSTEM ^^^
    # vvv Programs vvv
    Key([M], R, lazy.spawn(f"{TERMINAL} {CONSOLE}"), desc="Launch terminal"),
    Key([M], P, lazy.spawn(f"{MENU} -show run"), desc="Run a program with rofi"),
    Key([M, A], "b", lazy.spawn(f"{BROWSER}"), desc="Open browser"),
    Key([M, A], "t", lazy.spawn(f"{TASK_MANAGER}"), desc="Open task manager"),
    Key([M, A], "f", lazy.spawn(f"{FILE_MANAGER}"), desc="Open file manager"),
    Key([M, A], "e", lazy.spawn(f"{EDITOR}"), desc="Open editor"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch flameshot"),
    # ^^^ Programs ^^^
    Key([M], "y", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [M, S],
        R,
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 5- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 5+ unmute")),
]

