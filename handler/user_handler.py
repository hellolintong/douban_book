#coding=utf8
from flask import render_template
from flask import Blueprint
from flask import session
from flask import request
from flask import redirect
from flask import abort
from db.user import user_model
from config import Config

user = Blueprint('user', __name__, template_folder=Config.PARENT_DIR+'/templates', static_folder=Config.PARENT_DIR+'/static')


###########user operation#########################
def login_check():
    return 'user_id' in session


def get_login_user_id():
    if login_check():
        return session['user_id']
    else:
        return None

@user.route('/user/login', methods=['GET', 'POST'])
def login():
    #import pdb; pdb.set_trace()
    if request.method == 'GET':
        return render_template('login.html', login=False)
    elif request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = user_model.get_user(name=name)
        if user:
            user = user[0]
            if  user_model.check_user(user, password):
                session['user_id'] = str(user.id)
                return redirect('/user/' + str(user.id))
        session.pop('user_id', None)
        return redirect('/user/login')


@user.route('/user/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')


@user.route('/user/register', methods=['GET', 'POST'])
def register():
    #import pdb; pdb.set_trace()
    if request.method == 'GET':
        return render_template('register.html', login=False, info="")
    elif request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        if password != repeat_password:
            return render_template('register.html', login=False, info=u"密码不相符，请重新输入")
        user = user_model.add_user(name=name, password=password)
        if not user:
            return render_template('register.html', login=False, info=u"用户名已经存在")
        session['user_id'] = str(user.id)
        return redirect('/user/' + str(user.id))


################user home###########################
@user.route('/user/<user_id>')
def user_home(user_id):
    #import pdb; pdb.set_trace()
    if not login_check():
        return redirect('/user/login')
    user = user_model.get_user(id=user_id)
    if not user:
        abort(404)
    user = user[0]
    tags = user.collect_tags
    return render_template('user_home.html', tags=tags, login=True, user_id=user.id, user=user)


@user.route('/user/tag_operation/<operation>/<user_id>/<tag_name>')
def user_add_tag(operation, user_id, tag_name):
    if not login_check():
        return redirect('/user/login')
    user = user_model.get_user(id=user_id)
    if not user:
        abort(404)
    user = user[0]
    if operation == 'add':
        user_model.add_tag(user, tag_name)
        return redirect('/')
    elif operation == 'del':
        user_model.del_tag(user, tag_name)
        return redirect('/user/'+user_id)
    else:
        abort(404)


