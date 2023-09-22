local map = vim.keymap.set
local g = vim.g

g.mapleader = " "
map("n", "<leader>pv", vim.cmd.Ex)
map("n", "<C-s>v", vim.cmd.vsplit)
map("n", "<C-s>h", vim.cmd.split)
