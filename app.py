from flask import Flask, render_template, request

from modelo import clasificar_estado

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            cantidad = int(request.form.get("cantidad_sintomas", ""))
            dias = int(request.form.get("dias_sintomas", ""))
            intensidad = int(request.form.get("intensidad", ""))
        except ValueError:
            error = "Completa los tres campos con números enteros."
        else:
            try:
                resultado = clasificar_estado(cantidad, dias, intensidad)
            except ValueError as exc:
                error = str(exc)

    return render_template("index.html", resultado=resultado, error=error)


if __name__ == "__main__":
    app.run()