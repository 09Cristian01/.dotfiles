local k = vim.keymap.set
local c = vim.cmd

--k("n", "<leader>pv", c.Ex)
k("n", "<C-s>v", c.vsplit)
k("n", "<C-s>h", c.split)

k("v", "J", ":m '>+1<CR>gv=gv")
k("v", "K", ":m '<-2<CR>gv=gv")
k("v", "H", "'< <gv")
k("v", "L", "'> >gv")

k("n", "<leader>ra", ":%s/\\<<C-r><C-w>\\>/<C-r><C-w>/gI<Left><Left>")

k("n", "J", "mzJ`z")

k("n", "<leader>uc", "viwU")
k("i", "<leader>uc", "viwUi")

k("n", "<leader>yl", "Vip+y")
k("i", "<leader>yl", "Vip+yi")

k("i", "jk", "<ESC> gg=G :w<CR>")

k("n", "n", "nzzzv")
k("n", "N", "nzzzv")

k("n", "<leader>x",  "<c>!chmod +x %<CR>", {silent = true})

--k("n", "<leader>=", "gg=G")

k("n", "<leader>ot", function() require("utils.float_terminal")(nil, {ctrl_hjkl = false}) end)
