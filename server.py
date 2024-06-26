from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.config['TEMPLATES_AUTO_RELOAD'] = True  

@app.route('/')
def index():
    return render_template('index.html')


# Custom Error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

