import os
from flask import Flask, render_template_string


app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    data = [
        {'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    ]
    return render_template_string('''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 15px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Data Table</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
                <tr>
                    <td>{{ row.name }}</td>
                    <td>{{ row.age }}</td>
                    <td>{{ row.city }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
    ''', data=data)

if __name__ == '__main__':
    app.run(port=5000)

