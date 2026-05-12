from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    feedback = None

    if request.method == 'POST':
        message = request.form.get('message')

        if not message or message.strip() == "":
            feedback = "Wiadomość nie może być pusta."
        else:
            print(f"Otrzymano wiadomość: {message}")
            feedback = "Dziękuję! Twoja wiadomość została wysłana."

    return render_template('contact.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
