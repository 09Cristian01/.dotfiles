local opt = vim.opt
local g = vim.g

g.mapleader = " "

opt.number = true
opt.relativenumber = true

opt.clipboard = "unnamedplus"
opt.mouse = "a"

opt.cursorline = true

opt.smartcase = true

opt.hlsearch = true
opt.incsearch = true

opt.wrap = true

opt.breakindent = true

opt.tabstop = 4
opt.shiftwidth = 4

opt.termguicolors = true
-- opt.guicursor = ""

opt.wildmenu = true

opt.undofile = true
opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
opt.backup = false
opt.swapfile = false

opt.splitbelow = true
opt.splitright = true

opt.scrolloff = 10
opt.signcolumn = "yes"

opt.updatetime = 50

opt.colorcolumn = "80"

opt.ff = "unix"
