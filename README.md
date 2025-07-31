# 🏥 Hospital Checker by TEAM HYPERSCALER

A modern, interactive health and hospital information platform. Easily check your health metrics, find nearby hospitals, and access NHS resources

---

## 🚀 Features
- **Hospital Finder:** Search for hospitals by specialty and postcode, view distances, and access NHS resources.
- **Weight Management:** Calculate BMI, RMR, and get personalized calorie recommendations.
- **Wellbeing Resources:** Quick links to NHS and health resources.
- **Modern UI:** Cognizant-themed, responsive, and visually appealing.

---

## 🛠️ Getting Started

### Prerequisites
- Access to your company portal for platform and GitHub setup

### Setup Instructions

1. **Install Python** from your company portal.
2. **Activate your platform** (e.g., windsurf) using company portal and FAQs.
3. **Install GitHub Development Community** from your company portal.
    - Identify where Git Bash is installed and add its path to your environment variable `PATH`.
    - Create a GitHub account with your company email.
4. **Clone this repository:**
    ```sh
    git clone https://github.com/your-username/hospital-checker.git
    cd hospital-checker
    ```
5. **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    # Or
    source .venv/bin/activate  # On Mac/Linux
    ```
6. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
7. **Run the app:**
    ```sh
    streamlit run app.py
    ```

---

## 📁 Project Structure

```text
hospital-checker/
├── app.py                  # Main Streamlit entry point
├── data/                   # Raw and cleaned hospital data
├── requirements.txt        # Python dependencies
├── utils/                  # Utility modules (geocode, filter, preprocess, etc.)
├── views/                  # Streamlit page logic and UI helpers
│   ├── health_metrics.py
│   ├── health_metrics_ui.py
│   ├── hospital_finder.py
│   ├── hospital_finder_ui.py
│   └── wellbeing.py
└── .streamlit/
    └── config.toml         # Custom theme and settings
```

---

## 💡 Usage
- Navigate between **Hospital Finder**, **Weight Management**, and **Wellbeing** from the sidebar.
- Enter your details in the forms and get instant feedback, recommendations, and resource links.

---

## ❓ Troubleshooting
- If you see errors about missing packages, re-run `pip install -r requirements.txt`.
- If the app does not launch, make sure your virtual environment is activated.
- For platform-specific issues, refer to your company portal or FAQs.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

