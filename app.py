from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123@localhost/dashboard'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(50))
    address = db.Column(db.String(100))

@app.route('/')
def index():
    users = Users.query.all()
    return render_template('index.html', users=users)

@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    phone_number = request.form['phoneNumber']
    address = request.form['address']
    new_user = Users(name=name, gender=gender, email=email, phone_number=phone_number, address=address)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = Users.query.get_or_404(user_id)
    user.name = request.form['name']
    user.email = request.form['email']
    user.gender = request.form['gender']
    user.phone_number = request.form['phoneNumber']
    user.address = request.form['address']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
