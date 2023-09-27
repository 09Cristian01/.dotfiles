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

local opts = {								-- set up configurations
defaults = {
	lazy = true,
},
ui = {
	border = "none", -- rounded
	icons = {
		cmd = "⌘",
		config = "🛠",
		event = "📅",
		ft = "📂",
		--config = "⚙",
		keys = "🗝",
		plugin = "🔌",
		runtime = "💻",
		source = "📄",
		start = " ",
		task = "📌",
		lazy = "󰒲 ",
	},
},
change_detection = {
	notify = true,
},
performance = {
	rtp = {
		disabled_plugins = {
			"gzip",
			"netrwPlugin",
			"tarPlugin",
			"tohtml",
			"zipPlugin",
			"tutor",
		},
	},
},
}

local plugins = {
	--THEMES
	{
		"olimorris/onedarkpro.nvim",
		priority = 1000,
	},
	--UI
	--EDITOR
	{
		'windwp/nvim-autopairs',
		event = "InsertEnter",
	},
	{
		'hrsh7th/nvim-cmp',
		dependencies = {
			{'L3MON4D3/LuaSnip'},
		},
	},
	--LSP
	{
		'VonHeikemen/lsp-zero.nvim',
		lazy = false,
		branch = 'v3.x',
	},
	{
		'williamboman/mason.nvim',
		lazy = false,
		dependencies = {'williamboman/mason-lspconfig.nvim'},
	},
	{
		'neovim/nvim-lspconfig',
		lazy = false,
		dependencies = {'hrsh7th/cmp-nvim-lsp'},
	},
	{
		'nvim-telescope/telescope.nvim',
		tag = '0.1.3',
		dependencies = { 'nvim-lua/plenary.nvim' },
	},
	{
		"nvim-telescope/telescope-file-browser.nvim",
		dependencies = { "nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim" }
	},
	{
		"mbbill/undotree",
		lazy = false,
	},
	{
		"tpope/vim-fugitive",
		lazy = false,
	},
	{
		"theprimeagen/harpoon",
		event = "VeryLazy",
		dependencies = { "nvim-lua/plenary.nvim" },
	},
	{
		enabled = false,
		"lewis6991/impatient.nvim",
		event = "vimenter",
	},
	{
		"nvim-treesitter/nvim-treesitter",
		build = ":tsupdate",
		priority = 1000,
		--event = "verylazy",
		--	config = function() require('plugins.treesitter') end
	},
	--SQL
	{
		"kristijanhusak/vim-dadbod-ui",
		cmd = {
			'DBUI',
			'DBUIToggle',
			'DBUIAddConnection',
			'DBUIFindBuffer',
		},
		config = function()
			-- Your DBUI configuration
			vim.g.db_ui_use_nerd_fonts = 1
		end,
		dependencies = {
			{
				"tpope/vim-dadbod",
				cmd = { "DB" },
			},
			{
				"kristijanhusak/vim-dadbod-completion",
			},
		},
	},
	--GIT
	{
		"mhinz/vim-signify",
		lazy = false,
		enabled = false,
	},
	{
		"lewis6991/gitsigns.nvim",
		lazy = false,
	}
}
-- UI(ALPHA)
if vim.api.nvim_buf_get_option(0, "filetype") == "" then
	table.insert(plugins,
	{
		'goolord/alpha-nvim',
		event = "BufReadPost",--"VimEnter",
		config = function ()
			require('alpha').setup(require('alpha.themes.dashboard').config)
		end,
	})
end


require("lazy").setup(plugins, opts)
