
from flask import Flask ,request  ,render_template ,Markup
# from flask_cors import CORS

from main import recommend ,movie_list


# In[ ]:

app=Flask(__name__)

@app.route('/')
def home():
        return render_template("recommend.html")

@app.route('/predict',methods=['POST'])
def predict():
    mov=request.form['movie_name']
    recommend(mov)
    result=movie_list()
    return render_template('recommend.html',processed=Markup("The Movie you chosed is '{0}'<br>  The recommendations are <br>{1}".format(mov,result)))


if __name__ == '__main__':
    app.run()


