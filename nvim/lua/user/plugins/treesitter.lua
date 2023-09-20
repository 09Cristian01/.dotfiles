return {
	"nvim-treesitter/nvim-treesitter", 
	build = ":TSUpdate",
--	config = function() require('plugins.treesitter') end
}
--[[
    build = function()
      require('nvim-treesitter.install').update({ with_sync = true })
    end,
--]]
