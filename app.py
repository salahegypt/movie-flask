from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = int(request.form['age'])

    if age < 21:
        movie = {
            "title": "فيلم رقم 1",
            "image": "https://via.placeholder.com/400x250.png?text=فيلم+للشباب",
            "url": "https://www.youtube.com/watch?v=s2xQH3zMKKY"
        }
    elif age <= 40:
        movie = {
            "title": "فيلم رقم 2",
            "image": "https://via.placeholder.com/400x250.png?text=فيلم+للكبار",
            "url": "https://www.youtube.com/watch?v=0cnl33hDwgk"
        }
    else:
        movie = {
            "title": "فيلم رقم 3",
            "image": "https://via.placeholder.com/400x250.png?text=فيلم+للأكبر+سناً",
            "url": "https://www.youtube.com/watch?v=-INbpJksLro"
        }

    return render_template('result.html', name=name, movie=movie)

@app.route('/thank_you', methods=['POST'])
def thank_you():
    opinion = request.form['opinion']
    return render_template('thank_you.html', opinion=opinion)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)