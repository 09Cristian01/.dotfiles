local lsp = require('lsp-zero')

lsp.on_attach(function(client, bufnr)
	-- see :help lsp-zero-keybindings
	-- to learn the available actions
	lsp.default_keymaps({buffer = bufnr})
end)

require('mason').setup({})
require('mason-lspconfig').setup({
	ensure_installed = {},
	handlers = {
		lsp.default_setup,
	},
})

local cmp = require('cmp')

--cmp.mapping.confirm({ select = true })

cmp.setup({
	sources = {
		{name = 'nvim_lsp'}
	},
	mapping = cmp.mapping.preset.insert({
		['<C-Space>'] = cmp.mapping.complete(),
		['<CR>'] = cmp.mapping.confirm({ select = true }),
		['<TAB>'] = cmp.mapping.select_next_item(),
		['<S-TAB>'] = cmp.mapping.select_prev_item(),
	}),
	confirmation = {
		completeopt = 'menu,menuone,noinsert'
	}
})
