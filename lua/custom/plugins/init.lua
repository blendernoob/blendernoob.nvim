-- You can add your own plugins here or in other files in this directory!
--  I promise not to create any merge conflicts in this directory :)

-- See the kickstart.nvim README for more information
return {
  --MEL syntax hilighting
  { dir = '~/.config/nvim/vim-mel' },

  'catppuccin/nvim',
  name = 'catppuccin',
  priority = 1000,

  'rcarriga/nvim-dap-ui',
  dependencies = { 'mfussenegger/nvim-dap', 'nvim-neotest/nvim-nio' },

  'goolord/alpha-nvim',

  'vimwiki/vimwiki',
}
