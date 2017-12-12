from models.blog import Blog
from routes import *


main = Blueprint('blog', __name__)

Model = Blog

@main.route('/')
def index():
    return render_template('blog_add.html')

@main.route('/add', methods=['POST'])
def add():
    form = request.form

    # form.content.replace('\n','br')
    Model.new(form)
    return redirect(url_for('.index'))
