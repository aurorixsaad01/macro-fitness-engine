🚀 Macro & Fitness Engine

A Python-based CLI application that calculates BMR, TDEE, macro distribution, tracks weight progress, predicts trends using regression, and visualizes results.

🛠 Tech Stack

Python 3.10+

Pandas

NumPy

Matplotlib

Virtual Environment (venv)

Git

⚙️ How to Run This Project
🔹 Prerequisites (Both Windows & Linux)

Make sure you have:

Python 3.10 or higher

Git installed

Check versions:

python --version
git --version


If Python is not installed:

Download from: https://www.python.org/downloads/

🐧 Running on Linux (Ubuntu)
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/macro-fitness-engine.git
cd macro-fitness-engine

2️⃣ Create Virtual Environment
python3 -m venv venv

3️⃣ Activate Virtual Environment
source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt does not exist:

pip install pandas numpy matplotlib


If you get plotting issues:

sudo apt install python3-tk

5️⃣ Run the Application
python main.py

🪟 Running on Windows
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/macro-fitness-engine.git
cd macro-fitness-engine

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment
venv\Scripts\activate


If PowerShell blocks activation:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Then activate again.

4️⃣ Install Dependencies
pip install -r requirements.txt


If requirements file not present:

pip install pandas numpy matplotlib

5️⃣ Run the Application
python main.py

📊 Features

BMR Calculation (Mifflin-St Jeor)

TDEE Estimation

Goal-based Calorie Adjustment

Macro Distribution

Weight Logging

Linear Regression Trend Prediction

Data Visualization

📁 Project Structure
macro-fitness-engine/
│
├── main.py
├── metabolism.py
├── macros.py
├── tracker.py
├── prediction.py
├── visualizer.py
├── data/
└── requirements.txt

🔮 Future Improvements

Moving average smoothing

SQLite database integration

Flask web dashboard

Cloud deployment

User authentication