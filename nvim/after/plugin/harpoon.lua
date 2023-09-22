local mark = require("harpoon.mark")
local ui = require("harpoon.ui")

vim.keymap.set("n", "<leader>ta", mark.add_file)
vim.keymap.set("n", "<leader>tt",  function() vim.cmd(":Telescope harpoon marks") end) --ui.toggle_quick_menu)

vim.keymap.set("n", "<S-TAB>", ui.nav_next)
vim.keymap.set("n", "<TAB>", ui.nav_prev)

vim.keymap.set("n", "<leader>t1", function() ui.nav_file(1) end)
vim.keymap.set("n", "<leader>t2", function() ui.nav_file(2) end)
vim.keymap.set("n", "<leader>t3", function() ui.nav_file(3) end)
vim.keymap.set("n", "<leader>t4", function() ui.nav_file(4) end)
vim.keymap.set("n", "<leader>t5", function() ui.nav_file(5) end)
vim.keymap.set("n", "<leader>t6", function() ui.nav_file(6) end)
vim.keymap.set("n", "<leader>t7", function() ui.nav_file(7) end)
vim.keymap.set("n", "<leader>t8", function() ui.nav_file(8) end)
vim.keymap.set("n", "<leader>t9", function() ui.nav_file(9) end)
