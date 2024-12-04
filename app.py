import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


# Load the dataset
df = pd.read_csv(r"datasets/wuzzuf_dataset.csv",index_col=False)
df.drop(columns="Unnamed: 0", inplace=True)


# Set up the Streamlit app layout
st.title("Wuzzuf Jobs Analysis")
st.sidebar.header("Navigation")


# Sidebar - Selection
sidebar_option = st.sidebar.radio("Choose an Option:", ["Data Overview", "EDA"])


# Display the data overview
if sidebar_option == "Data Overview":
    st.header("Data Overview")
    st.write("This is a scraped data of jobs from wuzzuf")
    st.write(df.head(7))
    st.markdown("### Dataset Summary (categorical)")
    st.write(df.describe(include='object'))


elif sidebar_option == "EDA":
    st.header("Exploratory Data Analysis")
    #                                                                       0                   0                       0                   0                           0                       0
    analysis_type_option = st.sidebar.radio("Choose Analysis:", ["Top 5 Job Titles", "Top 5 Companies Hiring","Job Type Distribution","Workplace Distribution","Top 5 Locations for Jobs","Career Level Distribution","Most Frequent Job Types per Country"])


    if analysis_type_option == "Top 5 Job Titles":
        st.subheader("Top 5 Job Titles")
        data=df['job title'].value_counts().head(5)
        plt.figure(figsize=(8, 5))
        data.plot(kind='bar', color='skyblue')
        plt.title('Top 5 Job Titles', fontsize=16)
        plt.xlabel('Job Titles', fontsize=12)
        plt.ylabel('Number of Listings', fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        st.pyplot(plt)
        st.write("##### Insights:")
        st.write("* The top 5 job titles are in high demand, showing the main areas where companies are hiring.")
        st.write("* These roles reflect important sectors in the job market.")
        st.write("* The Accountant role stands out with the highest demand.")
        st.write("##### Recommendations:")
        st.write("* For Job Seekers: Focus on applying for these popular roles if your skills and interests match them.")


    elif analysis_type_option == "Top 5 Companies Hiring":
        st.subheader("Top 5 Companies Hiring")
        data=df['company'].value_counts().head(5)
        plt.figure(figsize=(8, 5))
        sns.barplot(x=data.values, hue=data.index,y=data.index ,palette='viridis')
        plt.title('Top 5 Companies Hiring', fontsize=16)
        plt.xlabel('Number of Listings', fontsize=12)
        plt.ylabel('Company', fontsize=12)
        st.pyplot(plt)
        st.write("##### Insights:")
        st.write("* The top 5 companies have the most listings, reflecting their active employment. ")
        st.write("* These companies might provide more opportunities but may also have competitive hiring processes.")
        st.write("##### Recommendations:")
        st.write("* Job seekers can target these top companies for job opportunities.")


    elif analysis_type_option == "Job Type Distribution":
        st.subheader("Job Type Distribution")
        data = df['job_type_list'].value_counts()
        fig = px.pie(
            names=data.index,
            values=data.values,
            title='Job Type Distribution'
        )
        st.plotly_chart(fig)
        st.write("##### Insights:")
        st.write("* The distribution of job types (e.g., full-time, part-time, freelance) showcases the work market's structure and flexibility.")
        st.write("* Most jobs are Full-time, it means companies are looking for long-term employees.")
        st.write("##### Recommendations:")
        st.write("* Employers can align their hiring strategies to match popular job types, while job seekers should target roles that suit their preferred working styles.")


    elif analysis_type_option == "Workplace Distribution":
        st.subheader("Workplace Distribution")
        data = df['workplace'].value_counts(normalize=True) * 100
        fig = px.bar(
            x=data.index,
            y=data.values,
            title='Workplace Distribution',
            labels={'x': 'Workplace Type', 'y': 'Percentage'},
            color=data.index,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig)
        st.write("##### Insights:")
        st.write("* This indicates that most companies prefer employees to work from their offices.")
        st.write("##### Recommendations:")
        st.write("* If you're open to On-site jobs, you'll have a larger pool of opportunities to choose from.")


    elif analysis_type_option == "Top 5 Locations for Jobs":
        st.subheader("Top 5 Locations for Jobs")
        data = df['location'].value_counts().head(5)
        plt.figure(figsize=(8, 5))
        sns.barplot(x=data.values, y=data.index,hue=data.index, palette='coolwarm')
        plt.title('Top 5 Locations for Jobs', fontsize=16)
        plt.xlabel('Number of Listings', fontsize=12)
        plt.ylabel('Location', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
        st.write("##### Recommendations:")
        st.write("- For Job Seekers: \n\t* Focus your job search on Cairo if you're seeking more opportunities, especially in districts like Maadi, New Cairo, and Nasr City.")



    elif analysis_type_option == "Career Level Distribution":
        st.subheader("Career Level Distribution")
        data = df['career_level'].value_counts()
        plt.figure(figsize=(8, 5))
        data.plot(kind='bar', color='salmon')
        plt.title('Career Level Distribution', fontsize=16)
        plt.xlabel('Career Level', fontsize=12)
        plt.ylabel('Number of Listings', fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.tight_layout()
        st.pyplot(plt)
        st.write("##### Insights:")
        st.write("* The majority of job listings target Experienced professionals, indicating a strong demand for individuals with proven expertise.")
        st.write("* Entry-level roles have a noticeable presence, suggesting opportunities for fresh graduates or early-career professionals.")
        st.write("* A higher spread of a particular career level can guide job seekers to fit their applications to match demand.")
        st.write("##### Recommendations:")
        st.write("* For Job Seekers:\n\t* Experienced professionals have the most opportunities; those with relevant experience should capitalize on this trend.\n\t* Fresh graduates should focus on entry-level openings and internships to build experience.")
       

    elif analysis_type_option == "Most Frequent Job Types per Country":
        st.subheader("Most Frequent Job Types per Country (Top 5 Countries)")
        top_countries = df['country'].value_counts().head(5).index
        filtered_data = df[df['country'].isin(top_countries)]
        job_types_per_country = filtered_data.groupby(['country', 'job_type_list']).size().unstack(fill_value=0)

        job_types_per_country.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
        plt.title('Most Frequent Job Types per Country (Top 5 Countries)', fontsize=16)
        plt.xlabel('Country', fontsize=12)
        plt.ylabel('Number of Listings', fontsize=12)
        plt.xticks(rotation=45)
        st.pyplot(plt)
        st.write("##### Insights:")
        st.write("* The majority of jobs are Full-Time positions in Egypt.")
        st.write("* This reflects a preference in the Egyptian job market for stable, long-term roles in Egypt.")
        st.write("* Other countries show a more diverse distribution of job types (such as part-time or remote work). However, data for some countries might be limited compared to Egypt.")
        st.write("##### Recommendations:")
        st.write("* For Job Seekers If you're looking for opportunities outside Egypt, focus on the common job types in those countries (e.g., remote or part-time work).")





    
    