local o = vim.opt
local g = vim.g
local c = vim.cmd

g.mapleader = " "
g.markdown_fenced_languages_enable_all = true

o.syntax = "enable"

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

o.showmatch = true
o.hlsearch = false
o.incsearch = true

o.wrap = false

o.breakindent = true
o.autoindent = true
o.copyindent = true
o.smartindent = true

o.expandtab = true
o.softtabstop = 4
o.tabstop = 4
o.shiftwidth = 4

o.termguicolors = true
-- o.guicursor = ""

o.wildmenu = true

o.undofile = true
o.undodir = os.getenv("HOME") .. "/.vim/undodir"
o.backup = false
o.swapfile = false

o.splitbelow = false
o.splitright = true

o.scrolloff = 10
o.signcolumn = "yes:1"

o.updatetime = 50

o.colorcolumn = "80"

o.ff = "unix"


o.completeopt = {'menuone', 'noselect', 'noinsert'}
o.shortmess = o.shortmess + { c = true}
c([[
autocmd CursorHold * lua vim.diagnostic.open_float(nil, { focusable = false })
]])

g.vimspector_sidebar_width = 85
g.vimspector_bottombar_height = 15
g.vimspector_terminal_maxwidth = 70
