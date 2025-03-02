from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)

Movies =["obi-wan","anakin","yoda","luke","mace-windu"]


@app.route('/')

def index():
    return  render_template("index.html",Films=Movies)
    # article=dict()
    # article['title']='First Article'
    # article['content']='This is the first article'
    # article['author']='yasin'
     
     
    # numbers = [1,2,3,4,5]
 
    # return redirect(url_for("home",name="yasin"))
    # return render_template("home_page.html" ,title="Yasin",id =24,Films=Movies,mace="mace-windu")
    
@app.route('/About')
def About():
    return  render_template("abaout.html")
 

@app.route('/Articles')
def Articles():
    return render_template("articles.html")
# @app.route('/home/<name>')
# def home(name):
#     # return "<p>Hello {}{}</p>".format(name,123)
#     return f"<p>Hello {name} {123}</p>"

# @app.route('/caracter')
# def caracter():
#     return render_template("layaout.html")


@app.route('/nav')
def nav():
    return render_template("layout.html")



if __name__ == '__main__':
    app.run(debug=True)
