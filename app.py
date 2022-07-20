import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#sklearn libraries

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder
from sklearn.ensemble import IsolationForest
from sklearn import model_selection
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import f1_score,accuracy_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_percentage_error,accuracy_score

scaler = StandardScaler()
le = LabelEncoder()
# app instatiate

app = Flask(__name__) 

# server path 
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
         f = request.form['csvfile']
         data = []
         with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
         return render_template('data.html', data =data)
        
if __name__ == "__main__" :
    app.run()