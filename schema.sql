CREATE TABLE patients (
    patient_id VARCHAR(10) PRIMARY KEY,
    height FLOAT,
    weight FLOAT,
    education INT,
    income INT,
    age_at_menarche INT,
    age_at_marriage INT,
    age_at_first_pregnancy INT,
    district VARCHAR(100),
    village VARCHAR(100),
    occupation VARCHAR(100),
    diet VARCHAR(50),
    `condition` VARCHAR(100)
);

CREATE TABLE deliveries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id VARCHAR(10),
    date_of_delivery DATE,
    age_at_delivery INT,
    weight_at_delivery FLOAT,
    hemoglobin_at_delivery FLOAT,
    placental_weight FLOAT,
    term_of_delivery VARCHAR(50),
    type_of_delivery VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE followups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id VARCHAR(10),
    visit_number INT,
    bp_dis INT,
    bp_sys INT,
    visit_date DATE,
    weight FLOAT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);