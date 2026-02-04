#!/usr/bin/env python3
"""Flask application to display data from JSON or CSV files."""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_data(filename='products.json'):
    """Read and parse data from JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def read_csv_data(filename='products.csv'):
    """Read and parse data from CSV file."""
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            products = []
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
            return products
    except FileNotFoundError:
        return None


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/products')
def products():
    """Render the products page with data from JSON or CSV."""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Read data based on source
    if source == 'json':
        products_data = read_json_data()
    else:
        products_data = read_csv_data()

    # Handle file not found
    if products_data is None:
        return render_template('product_display.html', error="File not found")

    # Filter by id if provided
    if product_id is not None:
        products_data = [p for p in products_data if p['id'] == product_id]
        if not products_data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
