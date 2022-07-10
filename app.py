from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        Type = int(request.form['Type'])
        Fixed_Acidity = float(request.form['Fixed Acidity'])/100
        Volatile_Acidity = float(request.form['Volatile Acidity'])/100
        Citric_Acid = float(request.form['Citric Acid'])/100
        Residual_Sugar = float(request.form['Residual Sugar'])/100
        Chlorides = float(request.form['Chlorides'])/100
        Free_Sulfur = float(request.form['Free Sulfur'])/100
        pH = float(request.form['pH'])/100
        Sulphates = float(request.form['sulphates'])/100
        Alcohol = float(request.form['alcohol'])/100
        input = [Type, Fixed_Acidity, Volatile_Acidity, Citric_Acid,
                 Residual_Sugar, Chlorides, Free_Sulfur, pH, Sulphates, Alcohol]
        model = joblib.load('model.pkl')
        if model.predict([input])[0] == 0:
            result = 'Wine Quality is Bad'
            color = 'red'
        else:
            result = 'Wine Quality is Good'
            color = 'green'
        return render_template('result.html', result=result, color=color)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
