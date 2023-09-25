local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
	vim.fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable", -- latest stable release
		lazypath,
	})
end
vim.opt.rtp:prepend(lazypath)

local plugins = {
	{
		"olimorris/onedarkpro.nvim",
		lazy = true,
		priority = 1000,
		opts = {}, 
	},
	{
		'nvim-telescope/telescope.nvim',
		lazy = true,
		priority = 1000,
		tag = '0.1.3',
		dependencies = { 'nvim-lua/plenary.nvim' },
	},
	{
		"nvim-treesitter/nvim-treesitter", 
		build = ":TSUpdate",
		priority = 1000,
		lazy = true,
		--event = "verylazy",
		--	config = function() require('plugins.treesitter') end
	},
	{
		"folke/tokyonight.nvim",
		event = "VeryLazy",
		--verylazy = true,
		--priority = 1000,
		opts = {},
		enabled = false,
	},
	{
		"mbbill/undotree",
		lazy = false,
		priority = 1000,
		--keys = {},
	},
	{
		"tpope/vim-fugitive",
		lazy = false,
		priority = 1000,
	},
	{
		"ThePrimeagen/harpoon",
		event = "VeryLazy",
		--priority = 1000,
		dependencies = { "nvim-lua/plenary.nvim" },
	},
	{
		'goolord/alpha-nvim',
		lazy = true,
		event = "VimEnter",
		config = function ()
			require'alpha'.setup(require'alpha.themes.dashboard'.config)
		end,
	},
	{
		"lewis6991/impatient.nvim",
		--event = "VimEnter",
		--lazy = false,
		enabled = false,
		priority = 2000,
	},
	{
		'VonHeikemen/lsp-zero.nvim',
		lazy = true,
		branch = 'v3.x',
	},

	--- Uncomment these if you want to manage LSP servers from neovim
	{
		'williamboman/mason.nvim',
		lazy = false,
		dependencies = {'williamboman/mason-lspconfig.nvim'},
	},

	-- LSP Support
	{
		'neovim/nvim-lspconfig',
		lazy = false,
		dependencies = {'hrsh7th/cmp-nvim-lsp'},
	},

	-- Autocompletion
	{
		'hrsh7th/nvim-cmp',
		lazy = true,
		dependencies = {
			{'L3MON4D3/LuaSnip'},
		},
	},
	{
		'windwp/nvim-autopairs',
		lazy = true,
		event = "InsertEnter",
		opts = {} -- this is equalent to setup({}) function
	}
}

local opts = {
	ui = {
		border = "none", -- rounded
		icons = {
			cmd = "⌘",
			config = "🛠",
			event = "📅",
			ft = "📂",
			init = "⚙",
			keys = "🗝",
			plugin = "🔌",
			runtime = "💻",
			source = "📄",
			start = " ",
			task = "📌",
			lazy = "󰒲 ",
		},
	},
	change_detection = {notify = true,}
}

require("lazy").setup(plugins, opts)
