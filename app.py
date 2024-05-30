from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'database-1.c3mic80s2nwr.ap-southeast-2.rds.amazonaws.com',
    'user': 'admin',
    'password': 'admin123'
}


# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    age = request.form['age']

    # Insert data into the database
    connection = pymysql.connect(**db_config)

    with connection.cursor() as cursor:
        sql1 = '''use TestDB1'''
        cursor.execute(sql1)
        sql2 = '''INSERT INTO Persons (FirstName, LastName, Age) VALUES (%s, %s, %s)'''
        cursor.execute(sql2, (first_name, last_name, age))
        connection.commit()
    connection.close()

    return jsonify({'message': 'Record submitted successfully!'})


# Route to get all records
@app.route('/records', methods=['GET'])
def records():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        sql1 = '''use TestDB1'''
        cursor.execute(sql1)
        sql2 = '''SELECT FirstName, LastName, Age FROM Persons'''
        cursor.execute(sql2)
        results = cursor.fetchall()
    connection.close()

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
