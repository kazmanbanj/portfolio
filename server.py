from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

# this will be used as a general route function instead of repeating the code
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# hee, you can choose to write to file or csv for the contact form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'



























# @app.route('/works')
# def works():
#     return render_template('./works.html')

# @app.route('/work1')
# def work1():
#     return render_template('./work1.html')

# @app.route('/about')
# def about():
#     return render_template('./about.html')

# @app.route('/contact')
# def contact():
#     return render_template('./contact.html')

# @app.route('/components')
# def components():
#     return render_template('./components.html')

# @app.route('/favicon.ico')
# def icon():
#     return 'This is the contact page'

# @app.route('/<username>/<int:post_id>')
# def users_post(username=None, post_id=None):
#     return render_template('./index.html', name=username, post_id=post_id)