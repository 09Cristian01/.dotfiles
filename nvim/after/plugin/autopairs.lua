local cmp_autopairs = require('nvim-autopairs.completion.cmp')
local cmp = require('cmp')
local npairs = require('nvim-autopairs')

cmp.event:on(
  'confirm_done',
  cmp_autopairs.on_confirm_done()
)

npairs.setup({
  enable_check_bracket_line = true
})
