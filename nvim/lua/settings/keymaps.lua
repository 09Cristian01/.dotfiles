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


-- Vimspector
k("n", "<F9>", "<cmd>call vimspector#Launch()<cr>")
k("n", "<F5>", "<cmd>call vimspector#StepOver()<cr>")
k("n", "<F8>", "<cmd>call vimspector#Reset()<cr>")
k("n", "<F11>", "<cmd>call vimspector#StepOver()<cr>")
k("n", "<F12>", "<cmd>call vimspector#StepOut()<cr>")
k("n", "<F10>", "<cmd>call vimspector#StepInto()<cr>")
k('n', "Db", ":call vimspector#ToggleBreakpoint()<cr>")
k('n', "Dw", ":call vimspector#AddWatch()<cr>")
k('n', "De", ":call vimspector#Evaluate()<cr>")
