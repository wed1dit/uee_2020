from flask import Flask
from flask import render_template, redirect, url_for
from .forms import DownloadForm
from .cfg import yaml

app = Flask(__name__)
app.config['SECRET_KEY'] = 'swqdwq21412rqwasssasomwegwmoepgweo'


super_passwd = yaml['common']['kor_passwd']


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/download_test', methods=['GET', 'POST'])
def download():
    
    form = DownloadForm()
    if form.validate_on_submit():
        access_code = form.password.data
        if access_code == super_passwd:
            return redirect(url_for("success"))
        else:
            ctx = "დაშვების კოდი არასწორად არის შეყვანილი"
            return render_template("test_download.html", form=form, metadata=ctx)
        
    return render_template('test_download.html', form=form)

@app.route('/success', methods=['GET', 'POST'])
def success():
    subjects = yaml['session']['subjects']
    date = yaml['common']['date']
    return render_template("success.html", date=date, subjects=subjects)