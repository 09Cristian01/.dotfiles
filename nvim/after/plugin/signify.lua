--require("signify")
local g = vim.g

g.signify_sign_add = "A"--"+"
g.signify_sign_delete = "D"--"-"
g.signify_sign_delete_first_line = "T"--"-"
g.signify_sign_change = "C"--"!"
g.signify_sign_change_delete = g.signify_sign_change .. g.signify_sign_delete_first_line
g.signify_sign_show_count = 1
g.signify_line_highlight = 1
g.signify_number_highlight = 1
