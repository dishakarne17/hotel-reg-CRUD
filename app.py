from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# ---------------- Configuration ----------------
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # goes inside /instance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- Model ----------------
class Hotel(db.Model):
    __tablename__ = 'hotel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Hotel {self.name}>"

# ---------------- Create DB / Table if not exists ----------------
with app.app_context():
    # If instance/example.db already exists, this will only create
    # tables that don't exist yet (won't touch existing ones/data).
    db.create_all()

# ---------------- CREATE + READ ----------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        rooms = request.form.get('rooms')
        price = request.form.get('price_per_night')

        if not name or not location or not rooms or not price:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))

        new_hotel = Hotel(
            name=name,
            location=location,
            rooms=int(rooms),
            price_per_night=float(price)
        )
        db.session.add(new_hotel)
        db.session.commit()
        flash('Hotel registered successfully!', 'success')
        return redirect(url_for('index'))

    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels)

# ---------------- UPDATE ----------------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    hotel = Hotel.query.get_or_404(id)

    if request.method == 'POST':
        hotel.name = request.form.get('name')
        hotel.location = request.form.get('location')
        hotel.rooms = int(request.form.get('rooms'))
        hotel.price_per_night = float(request.form.get('price_per_night'))

        db.session.commit()
        flash('Hotel updated successfully!', 'success')
        return redirect(url_for('index'))

    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels, edit_hotel=hotel)

# ---------------- DELETE ----------------
@app.route('/delete/<int:id>')
def delete(id):
    hotel = Hotel.query.get_or_404(id)
    db.session.delete(hotel)
    db.session.commit()
    flash('Hotel deleted successfully!', 'success')
    return redirect(url_for('index'))

# ---------------- Run ----------------
if __name__ == '__main__':
    app.run(debug=True)