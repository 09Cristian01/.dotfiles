local map = vim.keymap.set
local cmd = vim.cmd

map("n", "<leader>pv", cmd.Ex)
map("n", "<C-s>v", cmd.vsplit)
map("n", "<C-s>h", cmd.split)

map("v", "J", ":m '>+1<CR>gv=gv")
map("v", "K", ":m '<-2<CR>gv=gv")
map("v", "H", "'< <gv")
map("v", "L", "'> >gv")

map("n", "<leader>ra", ":%s/\\<<C-r><C-w>\\>/<C-r><C-w>/gI<Left><Left>")

map("n", "J", "mzJ`z")

map("n", "<leader>uc", "viwU")
map("i", "<leader>uc", "viwUi")

map("n", "<leader>yl", "Vip+y")
map("i", "<leader>yl", "Vip+yi")

map("i", "jk", "<ESC> :w<CR>")
map("i", "kj", "<ESC> :w<CR>")

map("n", "n", "nzzzv")
map("n", "N", "nzzzv")

map("n", "<leader>x",  "<cmd>!chmod +x %<CR>", {silent = true})
