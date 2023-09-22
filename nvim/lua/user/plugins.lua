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
  		priority = 1000,
 	 	opts = {},
		enable = false,
	},
	{
		"mbbill/undotree",
		lazy = false,
		priority = 1000,
		keys = {},
	},
	{
		"tpope/vim-fugitive",
		lazy = false,
		priority = 1000,
	},
	{
		"ThePrimeagen/harpoon",
		event = "VeryLazy",
		priority = 1000,
		dependencies = { "nvim-lua/plenary.nvim" },
	},
	{
    	'goolord/alpha-nvim',
		event = "VimEnter",
    	config = function ()
        	require'alpha'.setup(require'alpha.themes.dashboard'.config)
		end,
	},
	{
		"lewis6991/impatient.nvim",
		--event = "VimEnter",
		lazy = false,
		priority = 2000,
	},	
}

local opts = {}

require("lazy").setup(plugins, opts)
