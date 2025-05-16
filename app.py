import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.title("Mall Customer Segmentation")

@st.cache
def load_data():
    df = pd.read_csv('Mall_Customers.csv')
    # Basic preprocessing: encode gender
    df['Gender_Numeric'] = df['Gender'].map({'Male': 0, 'Female': 1})
    
    # Manual Age Grouping
    def assign_age_group(age):
        if age < 28:
            return 'Young'
        elif 28 <= age < 45:
            return 'Middle-aged'
        else:
            return 'Senior'
    df['Age_Group'] = df['Age'].apply(assign_age_group)
    
    # Spending Category Binning
    spending_labels = ['Low', 'Medium', 'High']
    df['Spending_Category'] = pd.qcut(df['Spending Score (1-100)'], q=3, labels=spending_labels)
    
    # Income to Spending Ratio
    df['Income_Spending_Ratio'] = df['Annual Income (k$)'] / (df['Spending Score (1-100)'] + 1)
    
    # One-hot encoding
    df = pd.get_dummies(df, columns=['Age_Group', 'Spending_Category'])
    
    return df

df = load_data()

st.header("Raw Data")
if st.checkbox("Show raw data"):
    st.write(df)

features_to_use = [
    'Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender_Numeric',
    'Income_Spending_Ratio', 'Age_Group_Middle-aged', 'Age_Group_Senior',
    'Age_Group_Young', 'Spending_Category_Low', 'Spending_Category_Medium',
    'Spending_Category_High'
]

X = df[features_to_use]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose number of clusters
k = st.slider("Select number of clusters (k)", min_value=2, max_value=10, value=5)

# Run KMeans
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(X_scaled)

df['Cluster'] = labels

st.header("Cluster Counts")
st.write(df['Cluster'].value_counts())

st.header("Cluster Visualization")
fig, ax = plt.subplots()
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='Set1', ax=ax)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Clusters: Annual Income vs Spending Score')
st.pyplot(fig)
