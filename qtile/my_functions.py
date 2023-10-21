def parse_names(text: str) -> str:
    programs = {
        " - Thorium": "Thorium",
        " - Firefox": "Firefox",
        "nvim ": "Neovim",
        " - kitty": "Kitty",
        #"~": "Home Directory",
    }
    for program in programs.keys():
        if program not in text:
            continue
        return programs[program]
    return text
