from flask import render_template, jsonify


def configure(app):
	
	@app.route("/index")
	@app.route("/")
	def index():
	    return "Hello World!", 200

	@app.route("/api")
	def api	():
	    return jsonify(data={"name":"felipe", "idade":23})

	@app.route("/langs")
	def langs():
		langs = ["Python", "PHP", "JS"]
		return render_template(
			'index.html',
			title="Melhores Linguagens",
			langs=langs
		)