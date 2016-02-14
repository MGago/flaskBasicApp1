from app import app

@app.route('/')
def index():
	return 'this is the homepage'

