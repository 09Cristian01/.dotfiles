local o = vim.opt
local g = vim.g

g.mapleader = " "

o.cmdheight = 0

o.number = true
o.relativenumber = true

o.clipboard = "unnamedplus"
o.mouse = "a"

o.cursorline = true

o.smartcase = true
o.ignorecase = true

o.foldcolumn = "1"
o.foldlevel = 99
o.foldlevelstart = 99
o.foldenable = true

o.hlsearch = false
o.incsearch = true

o.wrap = true

o.breakindent = true

o.tabstop = 4
o.shiftwidth = 4

o.termguicolors = true
-- o.guicursor = ""

o.wildmenu = true

o.undofile = true
o.undodir = os.getenv("HOME") .. "/.vim/undodir"
o.backup = false
o.swapfile = false

o.splitbelow = true
o.splitright = true

o.scrolloff = 10
o.signcolumn = "yes:1"

o.updatetime = 50

o.colorcolumn = "80"

o.ff = "unix"
