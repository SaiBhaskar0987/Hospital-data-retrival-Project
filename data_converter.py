import pandas as pd
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root", # Enter your SQL user name
    password="00000", # Enter your SQL password
    database="hospital"
)
cursor = conn.cursor()

# 1. Import patients
patients = pd.read_excel("basic_information.xlsx")
patients.columns = [
    "patient_id", "height", "weight", "education", "income",
    "age_at_menarche", "age_at_marriage", "age_at_first_pregnancy",
    "district", "village", "occupation", "diet", "condition"
]
for _, row in patients.iterrows():
    cursor.execute("""
        INSERT INTO patients VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# 2. Import deliveries
deliveries = pd.read_excel("delivery_information.xlsx")
deliveries.columns = [
    "patient_id", "date_of_delivery", "age_at_delivery",
    "weight_at_delivery", "hemoglobin_at_delivery",
    "placental_weight", "term_of_delivery", "type_of_delivery"
]
for _, row in deliveries.iterrows():
    cursor.execute("""
        INSERT INTO deliveries (
            patient_id, date_of_delivery, age_at_delivery, weight_at_delivery,
            hemoglobin_at_delivery, placental_weight, term_of_delivery, type_of_delivery
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# 3. Import followups in long format
followup = pd.read_excel("followup_data.xlsx")
followup_data = []
for _, row in followup.iterrows():
    pid = row["patient_id"]
    for i in range(1, 5):
        followup_data.append([
            pid,
            i,
            row[f"Visit{i}_bpdis"],
            row[f"Visit{i}_bpsys"],
            row[f"Visit{i}_date"],
            row[f"Visit{i}_wt"]
        ])

for row in followup_data:
    cursor.execute("""
        INSERT INTO followups (
            patient_id, visit_number, bp_dis, bp_sys, visit_date, weight
        ) VALUES (%s, %s, %s, %s, %s, %s)
    """, row)

conn.commit()
cursor.close()
conn.close()

print("✅ Data imported into MySQL successfully.")
