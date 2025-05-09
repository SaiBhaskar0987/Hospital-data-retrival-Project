from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '00000'
app.config['MYSQL_DB'] = 'hospital'

mysql = MySQL(app)

@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/patients', methods=['GET'])
def get_patients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients")
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)

@app.route('/patients/<string:patient_id>', methods=['GET'])
def get_patient(patient_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
    row = cur.fetchone()
    cur.close()
    return jsonify(row)

@app.route('/patients/<string:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM patients WHERE patient_id = %s", (patient_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': f'Patient {patient_id} deleted successfully'})

@app.route('/patients/<string:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE patients SET
            height = %s, weight = %s, education = %s, income = %s,
            age_at_menarche = %s, age_at_marriage = %s, age_at_first_pregnancy = %s,
            district = %s, village = %s, occupation = %s, diet = %s, `condition` = %s
        WHERE patient_id = %s
    """, (
        data.get('height'), data.get('weight'), data.get('education'), data.get('income'),
        data.get('age_at_menarche'), data.get('age_at_marriage'), data.get('age_at_first_pregnancy'),
        data.get('district'), data.get('village'), data.get('occupation'),
        data.get('diet'), data.get('condition'), patient_id
    ))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': f'Patient {patient_id} updated successfully'})

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO patients (
            patient_id, height, weight, education, income, age_at_menarche,
            age_at_marriage, age_at_first_pregnancy, district, village,
            occupation, diet, `condition`
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data.get('patient_id'), data.get('height'), data.get('weight'), data.get('education'),
        data.get('income'), data.get('age_at_menarche'), data.get('age_at_marriage'),
        data.get('age_at_first_pregnancy'), data.get('district'), data.get('village'),
        data.get('occupation'), data.get('diet'), data.get('condition')
    ))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Patient added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
