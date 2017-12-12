from models.todo import Todo
from models.blog import Blog
from routes import *


main = Blueprint('todo', __name__)

Model = Todo


@main.route('/')
def index():
    # ms = Model.query.all()
    import datetime
    d1 = datetime.datetime(2016,1,5)
    d2 = datetime.datetime.now()
    a = (d2 - d1).days
    b = datetime.datetime.now().weekday() + 1
    blogs = Blog.query.all()
    return render_template('end.html', a=a, b=b,blogs = blogs)

@main.route('/guonian')
def guonian():
    import datetime
    d1 = datetime.datetime(2018,2,15)
    d2 = datetime.datetime.now()
    a = (d1 - d2).days
    b = datetime.datetime.now().weekday() + 1
    return render_template('guonian.html', a=a, b=b)

@main.route('/marry')
def marry():
    return render_template('marry.html')

@main.route('/money')
def money():
    return render_template('money.html')

@main.route('/edit/<id>')
def edit(id):
    m = Model.query.get(id)
    return render_template('todo_edit.html', todo=m)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    Model.new(form)
    return redirect(url_for('.index'))


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    Model.update(id, form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
def delete(id):
    Model.delete(id)
    return redirect(url_for('.index'))
