import flask
import database
import get_news
import get_data

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        if database.verify_user(username, password):
            return flask.redirect(flask.url_for('main_page', user_id=username))
        else:
            error = 'Invalid username or password. Please try again!'
            return flask.render_template("login.html", error=error)
    return flask.render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
    return flask.render_template("create-account.html")


@app.route('/mainpage/?<string:user_id>', methods=['GET'])
def main_page(user_id):
    return flask.render_template("mainpage.html", userid=user_id)


@app.route('/mainpage/list/medicine/<user_id>', methods=['GET', 'POST'])
def medicine(user_id):
    medicine_list = database.get_medicine('medicine', user_id)
    table_name = "Medicine records"
    return flask.render_template("medicine_table.html", table_name=table_name, medicine_list=medicine_list)


@app.route('/mainpage/list/takeout/<user_id>', methods=['GET'])
def takeout(user_id):
    table_name = "Takeout"
    return flask.render_template("takeout_table.html", table_name=table_name)


@app.route('/mainpage/list/news/<user_id>', methods=['GET'])
def news(user_id):
    table_name = "News"
    data = get_data.get_data()
    news_list = get_news.get_news()
    return flask.render_template("news_table.html", table_name=table_name, data=data, news_list=news_list)


@app.route('/mainpage/list/trips/<user_id>', methods=['GET'])
def trips(user_id):
    table_name = "Trips"
    return flask.render_template("trip_table.html", table_name=table_name)


@app.route('/post/medicine/<user_id>', methods=['POST'])
def post_medicine(user_id):
    database.post_medicine(flask.request.form, user_id)
    return flask.redirect(flask.url_for('medicine', user_id=user_id))


if __name__ == '__main__':
    app.run()
