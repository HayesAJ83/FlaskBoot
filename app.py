from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
#    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
#    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
#    df2 = df1.sort_values(by=['Eponym'],ascending=True)
#    data = df2['Eponym_easy'].tolist()   


#@app.route('/A2Z')
#def A2Z():
#    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
#    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
#    df2 = df1.sort_values(by=['Eponym'],ascending=True)
#    table = df2['Eponym_easy']
#    return render_template('A2Z_1.html')

#@app.route('/templates/A2Z_1.html')
#def A2Z():
#    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
#    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
#    df2 = df1.sort_values(by=['Eponym'],ascending=True)
#    data = df2['Eponym_easy'].tolist()
#    return render_template('A2Z_1.html', data=data)

if __name__ == "__main__":
    app.run(Debug=True)
