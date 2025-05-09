# Hospital-data-retrival-Project

Assignment Structure:

    project/
    │
    ├── app.py                    # Main Flask backend
    ├── data_converter.py         # Script to import Excel data into MySQL
    ├── analytics.ipynb           # Jupyter Notebook to generate graphs
    ├── schema.sql                # SQL script to set up DB schema
    ├── templates/
    │   ├── index.html
    │   └── analytics.html
    ├── static/
    │   └── graphs/
    │       ├── correlation.png
    │       ├── bp_over_time.png
    │       └── weight_over_time.png
    ├── basic_information.xlsx    # (Required data file)
    ├── delivery_information.xlsx # (Required data file)
    └── followup_data.xlsx        # (Required data file)


✅ Requirements:

    Python 3.8+
    MySQL Server
    pip

⚙️ Setup Instructions:

1. 🔧 Clone the Repository
          git clone <repo-url>
          cd project
2. 🐍 Create a Virtual Environment (optional but recommended)
          python -m venv venv
          venv\Scripts\activate         # Windows
3. 📦 Install Python Dependencies
          pip install flask flask-mysqldb flask-cors pandas openpyxl mysql-connector-python
          🛠️ MySQL Setup
4. 🧱 Create and Populate the Database
          Step A: Launch MySQL and run:
          mysql -u root -p < schema.sql
          This will create the hospital database and all necessary tables.
   
🧾 Import Patient Data:
Ensure the following Excel files are in the project root:

          basic_information.xlsx
          delivery_information.xlsx
          followup_data.xlsx

Then run:
        python data_converter.py
You should see:
        ✅ Data imported into MySQL successfully.
        📊 Generate Analytics Graphs
Open and run analytics.ipynb in Jupyter:
        jupyter notebook analytics.ipynb
Ensure the generated .png files are saved inside:
        static/graphs/
        🚀 Start the Web App
        python app.py
        Visit:
        👉 http://127.0.0.1:5000/

🧩 Features:
        Full CRUD interface for patient data.
        Graphs for correlation, blood pressure, and weight trends.
        Separate pages for dashboard (index.html) and graph viewer (analytics.html).

🔒 Notes
Update DB credentials in app.py and data_converter.py.
