
def configure(app):
	
	@app.route("/index")
	@app.route("/")
	def index():
	    return "Hello World!", 200


	@app.route("/langs")
	def langs():
		langs = ["Python", "PHP", "JS"]
		return render_template(
			'index.html',
			title="Melhores Linguagens"
			linguagens=langs
		)