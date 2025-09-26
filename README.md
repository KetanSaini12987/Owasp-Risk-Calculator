# OWASP Risk Calculator

A simple web-based "OWASP Risk Rating Calculator" built with Python (Flask).  
It calculates risk levels based on OWASP's methodology:  
Risk = Likelihood × Impact

----------

# Features

- User inputs values (0–9) for OWASP factors.
- Calculates Likelihood Score and Impact Score.
- Displays overall 'Risk Level (Low, Medium, High, Critical)' with color coding.
- Simple, interactive UI with Flask + HTML/CSS.

----------

# Tech Stack
- Python 3
- Flask
- HTML, CSS
- 
-----------

# Project Setup

1. Clone repo:
   ```bash
   git clone https://github.com/your-username/owasp-risk-calculator.git
   cd owasp-risk-calculator

2. Create virtual environment & install dependencies:
   a. python -m venv venv
   b. source venv/bin/activate
   # On Windows: venv\Scripts\activate
   c. pip install -r requirements.txt.txt

4. Run the app:
   python app.py

   <img width="1431" height="370" alt="Screenshot_2025-08-31_14_34_37" src="https://github.com/user-attachments/assets/6f2d2471-fa86-41d8-8878-086e16b4ed2e" />

5. Open in browser:
   http://127.0.0.1:5000/
   
   <img width="1920" height="886" alt="Screenshot_2025-08-31_14_35_07" src="https://github.com/user-attachments/assets/bebab1d3-01d9-470e-a867-cc131147ea12" />

