# from flask import Flask, render_template, request,jsonify
# import pickle
# # from text_summary import summarize
# import numpy as np

# model=pickle.load(open('./model.pkl','rb'))

# app=Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')


# @app.route("/predict", methods=["POST"])
# def predict():
#     rawtext = request.form["rawtext"]
#     # Call the summarize method from the loaded TextSummarizer instance
#     summary = model.summarize(rawtext)
#     return jsonify({"summary": summary})



# if __name__=="__main__":
#     app.run(debug=True)





# # @app.route("/analyze",methods=["GET","POST"])
# # def analyze():
# #     if request.method =="POST":
# #         rawtext=request.form["rawtext"]
# #         summary,original_txt,len_orig_txt,len_summary=summarize(rawtext)
    
# #     return render_template("summary.html",summary=summary,original_txt=original_txt,len_orig_txt=len_orig_txt,len_summary=len_summary)









from flask import Flask, render_template, request,jsonify
import pickle
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
my_file = THIS_FOLDER / "model.pkl"

model=pickle.load(open(my_file,'rb'))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    rawtext = request.form["rawtext"]
    # Call the summarize method from the loaded TextSummarizer instance
    summary = model.summarize(rawtext)
    return jsonify({"summary": summary})



if __name__=="__main__":
    app.run(debug=True)

