from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form.get('message')
        print(f"Otrzymano wiadomość: {message}")
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
