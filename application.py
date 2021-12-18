import re
from flask import Flask,request,render_template
import pickle
from sklearn.preprocessing import StandardScaler
application=Flask(__name__)
@application.route('/')
def homepage():
    return render_template('index.html')
@application.route('/result',methods=['POST'])
def result():
    mar_rate=request.form['MarRate']
    age=request.form['age']
    married_yrs=request.form['my']
    no_children=request.form['cldrn']
    religion=request.form['rlg']
    education=request.form['ed']
    occupation=request.form['occ']
    hus_occupation=request.form['occhus']
    model=pickle.load(open('Affair_LogisticRegression.pickle','rb'))
    scalar=StandardScaler()
    scaled_feature=scalar.fit_transform([[mar_rate,age,married_yrs,no_children,religion,education,occupation,hus_occupation]])
    is_Affair=model.predict(scaled_feature)
    if is_Affair==1:
        return 'As per provided data over the married woman chance to have an affair is:' + str(True)
    else:
        return 'As per provided data over the married woman chance to have an affair is:'+ str(False)

    
if __name__=='__main__':
    application.run(debug=True)
