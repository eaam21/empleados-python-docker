from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOEmpleado import DAOEmpleado
 

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOEmpleado()
ruta='/empleado'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route(ruta+'/')
def index():
    data = db.read(None)

    return render_template('empleado/index.html', data = data)

@app.route(ruta+'/add/')
def add():
    return render_template('/empleado/add.html')

@app.route(ruta+'/addempleado', methods = ['POST', 'GET'])
def addempleado():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo empleado creado")
        else:
            flash("ERROR, al crear empleado")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('empleado/update.html', data = data)

@app.route(ruta+'/updateempleado', methods = ['POST'])
def updateempleado():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('empleado/delete.html', data = data)

@app.route(ruta+'/deleteempleado', methods = ['POST'])
def deleteempleado():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Empleado eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")