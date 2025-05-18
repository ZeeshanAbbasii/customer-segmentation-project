# Customer Segmentation Project

Welcome! This project performs customer segmentation on mall customer data using clustering algorithms. It helps businesses identify distinct customer groups based on demographics and spending patterns, enabling targeted marketing strategies.

---

## What’s Inside?

- **Dataset:** Customer info including Age, Gender, Income, and Spending Score  
- **Analysis:** Exploratory Data Analysis (EDA) with visuals to understand data  
- **Feature Engineering:** Creating new features like age groups, spending categories, and income-to-spending ratio  
- **Clustering:** Using K-Means and other clustering algorithms to segment customers  
- **Evaluation:** Silhouette scores to assess cluster quality  
- **Visualization:** Interactive plots to explore clusters  
- **Deployment:** A Streamlit app for interactive use  

---

## How to Run the Project Locally

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/customer_segmentation.git
cd customer_segmentation

Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Project Structure

customer_segmentation/
├── Mall_Customers.csv       # The dataset
├── app.py                  # Streamlit app code
├── requirements.txt        # Python packages needed
└── README.md               # This guide


Deploying Online

You can deploy this app easily on Hugging Face Spaces:

Push this repo to GitHub
Create a new Space on Hugging Face, select Streamlit
Connect your GitHub repo
The app will be live and shareable instantly!
Dependencies

pandas
matplotlib
seaborn
scikit-learn
streamlit

Install all at once with:

pip install -r requirements.txt


Thank you for checking out the project! Feel free to explore and build on it.


