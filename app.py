from flask import Flask, render_template, request, redirect, url_for, session;

app = Flask(__name__)
app.secret_key = "senha_secreta"

@app.route("/")
def tarefas():
    if "tarefas" not in session:
        session["tarefas"] = []
    tarefas = session["tarefas"]
    return render_template ("tarefas.html", tarefas=tarefas)

@app.route("/add", methods = ["POST"])
def adicionar():
    tarefa = request.form.get("tarefa")
    session["tarefas"].append(tarefa)
    session.modified = True
    return redirect(url_for("tarefas"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tarefas = session.get("tarefas",[])
    if 0 <= task_id < len(tarefas):
        tarefas.pop(task_id)
        session["tarefas"] = tarefas 
        session.modified = True
    return redirect(url_for("tarefas"))
    

if __name__ == "__main__":
    app.run(debug=True)