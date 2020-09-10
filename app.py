from flask import Flask, render_template ,request
import time
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")
'''
@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submitted',methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return "data.message"
    else:
        return f"Something Not Right "
'''        

@app.errorhandler(404)  
def not_found(e): 
  return render_template("404.html") 

if __name__ == '__main__':
    app.run(debug=True)