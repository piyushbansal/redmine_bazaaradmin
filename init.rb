require 'redmine'

Redmine::Plugin.register :redmine_bazaaradmin do
  name 'Redmine Bazaaradmin plugin'
  author 'Swetha V'
  description 'This is a plugin for Redmine'
  version '0.0.1'
  permission :bazaaradmin, { :bazaaradmin => [:index] }, :public => true
  menu :project_menu, :bazaaradmin, { :controller => 'bazaaradmin', :action => 'index' }, :caption => 'Bazaar Admin', :after => :activity, :param => :project_id

end
