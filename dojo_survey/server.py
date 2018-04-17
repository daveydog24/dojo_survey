from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretgfdfgKeepItSafe'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    dojo_location = request.form['dojo_location']
    favorite_language = request.form['favorite_language']
    comment = request.form['comment']

    if len(name) < 1:
        flash('Error: Name can not be empty!')
        return redirect('/')
    elif len(comment) > 120: #Could of made this less than one elif but it says the comment is optional? so i didnt
        flash('Error: Comment was too long!')
        return redirect('/')        
    else: 
      session['name'] = name
      session['dojo_location'] = dojo_location 
      session['favorite_language'] = favorite_language 
      session['comment'] = comment
      return render_template("results.html", name=session['name'], dojo_location=session['dojo_location'], favorite_language=session['favorite_language'], comment=session['comment'])

app.run(debug=True)