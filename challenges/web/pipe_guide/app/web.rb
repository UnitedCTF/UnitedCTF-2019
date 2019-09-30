 require 'sinatra'

set :port, 9999

get '/' do

  if not page = params[:page]
    redirect '/?page=home.html'
  end

  open(page)
end
