from flask import Blueprint, render_template, request, abort, current_app


bp = Blueprint("contact", __name__, url_prefix="/contact")


@bp.route("/", methods=['GET', 'POST'])
def contact():
	if request.method == "GET"
		return render_template('contact.html')
	
	name = request.form.get("name")
	message = request.form.get("message")

	if not name or not message:
		abort(400, "Mensagem inválida")

	return "OK"


def configure(app):
	app.register_blueprint(bp)