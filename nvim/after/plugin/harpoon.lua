--[==[
local mark = require("harpoon.mark")
local ui = require("harpoon.ui")

local k = vim.keymap.set

k("n", "<leader>ta", mark.add_file)
k("n", "<leader>tt",  function() vim.cmd(":Telescope harpoon marks") end) --ui.toggle_quick_menu)

k("n", "<S-TAB>", ui.nav_next)
k("n", "<TAB>", ui.nav_prev)

k("n", "<leader>t1", function() ui.nav_file(1) end)
k("n", "<leader>t2", function() ui.nav_file(2) end)
k("n", "<leader>t3", function() ui.nav_file(3) end)
k("n", "<leader>t4", function() ui.nav_file(4) end)
k("n", "<leader>t5", function() ui.nav_file(5) end)
k("n", "<leader>t6", function() ui.nav_file(6) end)
k("n", "<leader>t7", function() ui.nav_file(7) end)
k("n", "<leader>t8", function() ui.nav_file(8) end)
k("n", "<leader>t9", function() ui.nav_file(9) end)
--]==]
