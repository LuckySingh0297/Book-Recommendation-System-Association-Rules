# Import libraries
from flask import Flask, render_template, request
from urllib.parse import quote
from sqlalchemy import create_engine
import pandas as pd
import pickle
import joblib
from mlxtend.frequent_patterns import apriori, association_rules

def to_list(i):
    return (sorted(list(i)))


def association(data_new):
    frequent_itemsets = apriori(data_new, min_support = 0.0075, max_len = 4, use_colnames = True)
    # Most frequent itemsets based on support 
    frequent_itemsets.sort_values('support', ascending = False, inplace = True)
    rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
    ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)
    ma_X = ma_X.apply(sorted)
    rules_sets = list(ma_X)
    unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]
    index_rules = []
    for i in unique_rules_sets:
        index_rules.append(rules_sets.index(i))
    # Rules without any redudancy 
    rules_no_redundancy = rules.iloc[index_rules, :]
    # Sorted list and top 10 rules 
    rules_10= rules_no_redundancy.sort_values('lift', ascending = False).head(10)
    return(rules_10)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST' :
        f = request.files['file']
        user = request.form['user']
        pw = request.form['password']
        db = request.form['databasename']
        engine = create_engine(f'mysql+pymysql://{user}:%s@localhost:3306/{db}' % quote(f'{pw}'))
        
        try:

            data = pd.read_csv(f)
        except:
                try:
                    data = pd.read_excel(f)
                except:      
                    data = pd.DataFrame(f)
                    
                  
       
       
        ar=association(data)
        df=ar.iloc[:,1:]
         
        df.to_sql('arbooks', con = engine, if_exists = 'replace', chunksize = 5000, index = False)
        
        html_table = ar.to_html(classes = 'table table-striped')
        
        return render_template("data.html", Y = f"<style>\
                    .table {{\
                        width: 50%;\
                        margin: 0 auto;\
                        border-collapse: collapse;\
                    }}\
                    .table thead {{\
                        background-color: #39648f;\
                    }}\
                    .table th, .table td {{\
                        border: 1px solid #ddd;\
                        padding: 8px;\
                        text-align: center;\
                    }}\
                        .table td {{\
                        background-color: #888a9e;\
                    }}\
                            .table tbody th {{\
                            background-color: #ab2c3f;\
                        }}\
                </style>\
                {html_table}")

if __name__=='__main__':
    app.run(debug = True)
