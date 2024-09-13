import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

# Navbar HTML
navbar_html = '''
<style>
    .st-emotion-cache-12fmjuu{
        z-index: 100;
    }
    .st-emotion-cache-h4xjwg{
        z-index: 100;
    }
    h2{
    color: white;
    }
    .css-hi6a2p {padding-top: 0rem;}
    .navbar {
        background-color: #355E3B;
        padding: 0.3rem;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar .logo {
        display: flex;
        align-items: center;
    }
    .navbar .logo img {
        height: 40px;
        margin-right: 10px;
    }
    .navbar .menu {
        display: flex;
        gap: 1.5rem;
    }
    .navbar .menu a {
        color: white;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .content {
        padding-top: 5rem;  /* Adjust this based on navbar height */
    }
</style>

<nav class="navbar">
    <div class="logo">
        <h2 id="hh">MERIT Dashboard</h2>
    </div>
    <div class="menu">
        <a href="">Dashboard</a>
        <a href="mvp">Multi Variable Plots</a>
        <a href="mlp">ML Predictions</a>
        <a href="ml-predictions">About Us</a>
    </div>
</nav>

<div class="content">
'''

# Injecting the navigation bar and content padding into the Streamlit app
st.markdown(navbar_html, unsafe_allow_html=True)

a,b = st.columns([0.3,0.7])

# with st.spinner("Fetching Datasets..."):
#     import getresource as gr
#     import os
#     gdrive_link = "https://drive.google.com/uc?id=1mgKajVm3IpFw2a52d_j5VXz5v0K0F9sX"  # Replace with the actual file ID
#     folder_name = "resource"
#     download_path = "./downloads"  # Path to store the zip file
#     extract_path = "./resource/resource"  # Path to extract the folder
#     gr.download_and_extract_with_gdown(gdrive_link, folder_name, download_path, extract_path)
# with b:
#     st.write(os.listdir("./resource/resource/Final Data/Ecoli data"))

with a:
    with st.container(border=True):
        
        st.subheader("Available Plots")
        st.write("---")
        with st.expander("% of Resistance over Years"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter cloacae",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=1)
            age_group = st.selectbox("Choose Age Group",["0 to 2 Years","3 to 12 Years","13 to 18 Years","19 to 64 Years","65 to 84 Years","85 and over"])
            if st.button("Display Plot",key=12):
                import chisquare as c
                fig= c.plot_age_group(org,age_group)
        
                with b:
                    st.subheader(f"% of Resistance Over the Years - Age Group: {age_group}")
                    st.plotly_chart(fig)
        with st.expander("% of Resistance over Country"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter cloacae",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=2)
            import chisquare as c
            con = "India"
            try:
                con = st.selectbox("Choose Country",c.get_cons(org))
            except:
                pass
            if st.button("Display Plot",key=99):
                with b:
                    st.plotly_chart(c.plot_country_group(org,con))


        with st.expander("Antibiotic Resistant Profile for Organism"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter cloacae",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=3)
            if st.button("Display Plot",key=22):
                import chisquare as c
                with a:
                    fig=c.plot_antibiotic_resistance(org)
                    with b:
                        st.pyplot(fig)
        
        with st.expander("Country Wise Resistant Profile"):
            org = st.selectbox("Choose Organism",["Not Chosen","Acinetobacter baumannii", "Enterobacter cloacae",
            "Escherichia coli", "Enterococcus faecium", "Klebsiella pneumoniae",
            "Pseudomonas aeruginosa", "Staphylococcus aureus"
            ],key=4)
            if st.button("Display Plot",key=23):
                import chisquare as c
                with a:
                    fig=c.conplot_geo(org)
                    with b:
                        st.plotly_chart(fig)
    
            
            

            
