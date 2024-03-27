![jsr2](https://github.com/raj18verma/Job-Filtering-App/blob/main/utilities/resumes/A%20cutting-edge%20%20c5f52a77-b1e6-4bb5-8c97-571ea2b468b2.png)

# Job Filtering Prototype using Machine Learning
This repository contains the code and instructions to build a job recommendation system using machine learning. The system is designed to provide personalized job recommendations based on user preferences and historical job data. The data for this project will be scraped from UNSTOP itself (but here we're using GLASSDOOR), and the system can be deployed using a cloud platform.

## Business Understanding
The goal of this feature is to enhance the filter system of UNSTOP platform which can helps users to find relevant job opportunities based on their preferences and historical data. By leveraging machine learning techniques, we can provide personalized recommendations that align with the user's skills, interests, and career goals. The system will take into account various factors such as job title, salary estimate, company rating, location, industry, and more to generate accurate recommendations.

## Data Scraping
To collect the necessary data for training our prototype, we will scrape job-related information from UNSTOP. The following columns will be extracted:

Job Title
Salary Estimate
Job Description
Rating
Company Name
Location
Headquarters
Size
Founded
Type of Ownership
Industry
Sector
Revenue
Competitors

## Feature Engineering
Once the data is collected, we will perform feature engineering to preprocess and transform the raw data into a suitable format for training our filter model. This step includes:

Handling Missing Data: Deal with missing values in the dataset by either imputing them or removing the corresponding rows/columns.
Encoding Categorical Variables: Convert categorical variables such as job title, location, industry, and sector into numerical representations using techniques like one-hot encoding or label encoding.
Feature Scaling: Normalize numerical features, such as salary estimate and company rating, to ensure they have a similar scale and prevent dominance of certain features in the model.

## Machine Learning Techniques:
To provide personalized job recommendations, we employ the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique. The TF-IDF vectorizer from the scikit-learn library to transform job descriptions and user preferences into numerical feature vectors. These vectors capture the importance of each word in the documents, enabling the system to find similar job opportunities based on user preferences. The Nearest Neighbors algorithm is then used to identify the most relevant job recommendations.

skill extractor segment provides functions and utilities to extract skills from a PDF file using the Spacy library and perform text processing and matching operations. These extracted skills can be used for further analysis and processing in the job recommendation system.

## Streamlit Application
To make the job recommendation system easily accessible and user-friendly, we have developed a Streamlit application. Streamlit provides an intuitive web interface where users can upload their resumes. The application processes the user input, applies the machine learning models, and displays the top-recommended jobs based on the user's preferences and historical data.


## Must Go Through the Live Working Demo of this Prototype :- https://drive.google.com/file/d/10nRaomiDdyatcG-2d6T_ogLrKVFouxVu/view?usp=drive_link
