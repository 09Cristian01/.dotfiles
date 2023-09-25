--[[local lsp = require("lsp-zero")

lsp.preset("recommended")

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

local cmp = require("cmp")
local cmp_select = {behavior = cmp.SelectBehavior.Select}
local cmp_mappings = lsp.defaults.cmp_mappings({
	["<C-Space>"] = cmp.mapping.complete(),
	["<C-y>"] = cmp.mapping.confirm({ select = true }),
})

lsp.setup_nvim_cmp({
	mapping = cmp_mappings
})

lsp.on_attach(function(client, bufnr)
	--print("help")
	local opts = {buffer = bufnr, remap = false}
	local map = vim.keymap.set

	map("n", "<leader>gd", function() vim.lsp.buf.definition() end, opts)
	map("n", "<leader>vrr", function() vim.lsp.buf.references() end, opts)
	map("n", "<leader>vrn", function() vim.lsp.buf.rename() end, opts)
end)

lsp.setup()--]]

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
