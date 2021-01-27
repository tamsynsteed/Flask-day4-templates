from flask import Flask, render_template

app =Flask(__name__)

@app.route('/Index')
def index():
        return render_template('greet.html')

@app.route('/about')
def about():
        return render_template('about.html')



if __name__=='__main__':
    app.run(debug=True)
