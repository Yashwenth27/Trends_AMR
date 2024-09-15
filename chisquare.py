import pandas as pd
import matplotlib.pyplot as plt

# import getresource as gr
# import os
# gdrive_link = "https://drive.google.com/uc?id=1mgKajVm3IpFw2a52d_j5VXz5v0K0F9sX"  # Replace with the actual file ID
# folder_name = "resource"
# download_path = "./downloads"  # Path to store the zip file
# extract_path = "./resource"  # Path to extract the folder

# # Ensure the download path exists
# if not os.path.exists(download_path):
#     os.makedirs(download_path)

# # Download and extract folder
# flag = 1
# if flag==0:
#     gr.download_and_extract_with_gdown(gdrive_link, folder_name, download_path, extract_path)

mapping = {
        "Escherichia coli" : ["./Final_Ecoli1.csv","./Final_Ecoli2.csv"],
        "Enterococcus faecium" : "./Final_EF.csv",
        "Klebsiella pneumoniae" : "./Final_KP.csv",
        "Acinetobacter baumannii" : "./Final_AB.csv",
        "Pseudomonas aeruginosa" : "./Final_PA.csv",
        "Staphylococcus aureus" : ["./Final_SA1.csv","./Final_SA2.csv"],
        "Enterobacter spp" : "./Final_EB.csv"
    }

import pandas as pd
import plotly.graph_objects as go

def plot_antibiotic_resistance(organism):
    # Read data from the CSV file
    df = pd.read_csv("cs_res.csv", encoding='ISO-8859-1', low_memory=False)
    
    # Convert 'R' and 'S' columns to numeric, coercing errors to NaN
    df['R'] = pd.to_numeric(df['R'], errors='coerce')
    df['S'] = pd.to_numeric(df['S'], errors='coerce')

    # Drop rows where 'S' is zero or NaN to avoid division by zero and invalid calculations
    df = df[df['S'] > 0]

    # Group by Organism, Antibiotics, and Year, and sum R and S values
    grouped_df = df.groupby(['Organism', 'Antibiotics', 'Year']).agg({'R': 'sum', 'S': 'sum'}).reset_index()

    # Calculate the percentage of resistant cases
    grouped_df['%R'] = (grouped_df['R'] / (grouped_df['R'] + grouped_df['S'])) * 100
    grouped_df['%S'] = (grouped_df['S'] / (grouped_df['R'] + grouped_df['S'])) * 100
    print("Columns in grouped_df:", grouped_df.columns)
    print("Head of grouped_df:", grouped_df.head())
    print(organism)
    if "neto" in organism:
        organism_data = grouped_df[grouped_df['Organism'] == "Acinetobacter baumannii"]
    else:
        organism_data = grouped_df[grouped_df['Organism'] == organism]

    # Get unique antibiotics for this organism
    antibiotics = organism_data['Antibiotics'].unique()

    # Create a Plotly figure
    import plotly.graph_objects as go
    fig = go.Figure()

    # Add a trace for each antibiotic
    for antibiotic in antibiotics:
        antibiotic_data = organism_data[organism_data['Antibiotics'] == antibiotic]
        
        # Add trace for each antibiotic

        fig.add_trace(go.Scatter(
            x=antibiotic_data['Year'],
            y=antibiotic_data['%S'],
            mode='markers+lines',
            name=antibiotic,
            text=[f"Antibiotics: {year}<br>R: {R}<br>S: {S}<br>%S: {percent_R}" 
                  for year, R, S, percent_R in zip(
                      antibiotic_data['Antibiotics'],
                      antibiotic_data['R'],
                      antibiotic_data['S'],
                      antibiotic_data['%S']
                  )],
            hoverinfo='text',
            marker=dict(size=8)
        ))

    # Update layout of the figure
    fig.update_layout(
        title=f'Antibiotic Susceptibility Profile for {organism}',
        xaxis_title='Year',
        yaxis_title='% of R',
        xaxis=dict(tickmode='linear'),
        legend_title='Antibiotics'
    )
    import plotly.graph_objects as go

    # Create an empty figure
    fig1 = go.Figure()

    # Add a trace for each antibiotic
    for antibiotic in antibiotics:
        antibiotic_data = organism_data[organism_data['Antibiotics'] == antibiotic]
        
        # Add box plot trace for each antibiotic
        fig1.add_trace(go.Box(
            x=antibiotic_data['Antibiotics'],
            y=antibiotic_data['%R'],
            name=antibiotic
        ))

    # Update layout of the figure
    fig1.update_layout(
        title=f'Antibiotic Resistance Profile for {organism}',
        xaxis_title='Antibiotics',
        yaxis_title='% of R',
        xaxis=dict(tickmode='linear'),
        legend_title='Antibiotics',  # Set a legend title
        hovermode='closest'  # Ensure hover info is shown when closest to the data point
    )



    return fig, organism_data, fig1

def get_cons(organism):
    import pandas as pd
    import numpy as np
    
    if type(mapping[organism])==type([1,2]):
        import pandas as pd
        def combine_csv(file1, file2):
            # Load the two CSV files
            df1 = pd.read_csv(file1)
            df2 = pd.read_csv(file2)
            
            # Concatenate the two dataframes to get the original dataframe
            combined_df = pd.concat([df1, df2], ignore_index=True)
            
            return combined_df

        # Usage
        original_df = combine_csv(mapping[organism][0], mapping[organism][1])
        ecoli = original_df
    else:
        ecoli = pd.read_csv(mapping[organism],low_memory=False)
    if  organism=="Escherichia coli":
        ecoli.Source.replace("Vomit","Others",inplace=True)
        ecoli.Source.replace("Paracentesis Fluid","Bodily Fluids",inplace=True)
        ecoli.Source.replace("Ascetic Fluid","Bodily Fluids",inplace=True)
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if  organism=="Staphylococcus aureus":
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if organism=="Enterobacter spp":
        ecoli["Species"] = "Enterobacter spp"
        

        
    ec=ecoli.copy()
    ec['Age Group'].value_counts()
    clean_ec=ec[ec['Age Group'] != 'Unknown']
    clean_ec_cols=list(clean_ec.columns[clean_ec.columns.str.contains("_I")])
    ec_plot1 = clean_ec.melt(id_vars=['Country','Age Group'], 
                    value_vars=clean_ec_cols,
                    var_name='Antibiotic', value_name='Resistance')
    ec_pv_plot1 = ec_plot1.pivot_table(index=['Country', 'Age Group','Antibiotic'], 
                               columns='Resistance', 
                               aggfunc='size', 
                               fill_value=0).reset_index()
    ec_pv_plot1['R_S_sum']=ec_pv_plot1['R']+ec_pv_plot1['S']
    ec_pv_plot1_final=ec_pv_plot1[ec_pv_plot1['R_S_sum']>10]
    dff = ec_pv_plot1
    import pandas as pd
    import plotly.graph_objects as go
    data = dff
    return data['Country'].unique()
def plot_country_group(organism, country):
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    
    if type(mapping[organism]) == type([1, 2]):
        def combine_csv(file1, file2):
            # Load the two CSV files
            df1 = pd.read_csv(file1)
            df2 = pd.read_csv(file2)
            
            # Concatenate the two dataframes to get the original dataframe
            combined_df = pd.concat([df1, df2], ignore_index=True)
            
            return combined_df

        # Usage
        original_df = combine_csv(mapping[organism][0], mapping[organism][1])
        ecoli = original_df
    else:
        ecoli = pd.read_csv(mapping[organism], low_memory=False)
    if  organism=="Escherichia coli":
        ecoli.Source.replace("Vomit","Others",inplace=True)
        ecoli.Source.replace("Paracentesis Fluid","Bodily Fluids",inplace=True)
        ecoli.Source.replace("Ascetic Fluid","Bodily Fluids",inplace=True)
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if  organism=="Staphylococcus aureus":
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if organism=="Enterobacter spp":
        ecoli["Species"] = "Enterobacter spp"
    
    ec = ecoli.copy()
    ec['Age Group'] = ec['Age Group'].str.replace('3 to 12 Years', '03 to 12 Years')
    ec['Age Group'].value_counts()
    clean_ec = ec[ec['Age Group'] != 'Unknown']
    clean_ec_cols = list(clean_ec.columns[clean_ec.columns.str.contains("_I")])
    ec_plot1 = clean_ec.melt(id_vars=['Country', 'Age Group'], 
                    value_vars=clean_ec_cols,
                    var_name='Antibiotic', value_name='Resistance')
    ec_pv_plot1 = ec_plot1.pivot_table(index=['Country', 'Age Group', 'Antibiotic'], 
                               columns='Resistance', 
                               aggfunc='size', 
                               fill_value=0).reset_index()
    ec_pv_plot1['R_S_sum'] = ec_pv_plot1['R'] + ec_pv_plot1['S']
    ec_pv_plot1_final = ec_pv_plot1[ec_pv_plot1['R_S_sum'] > 10]
    dff = ec_pv_plot1_final

    # Load the dataset
    data = dff

    # Filter data for a specific country
    country_data = data[data['Country'] == country]

    # Remove the antibiotic "Colistin"
    country_data = country_data[country_data['Antibiotic'] != 'Colistin_I']

    # Calculate resistance percentage
    country_data['Resistance_Percentage'] = (country_data['R'] / (country_data['R'] + country_data['S'])) * 100

    # Clean antibiotic names (remove trailing "_I")
    country_data['Antibiotic'] = country_data['Antibiotic'].str.replace('_I', '')
    

    # Create the figure
    fig = go.Figure()

    # Generate unique colors for each antibiotic line
    colors = [
        'blue', 'red', 'green', 'purple', 'orange', 'brown', 'pink', 'gray', 'cyan', 'magenta'
    ]

    # Add line plots for each antibiotic with unique colors
    for i, antibiotic in enumerate(country_data['Antibiotic'].unique()):
        antibiotic_data = country_data[country_data['Antibiotic'] == antibiotic]

        # Ensure there's data for the age group, otherwise skip it
        if antibiotic_data.empty:
            continue

        fig.add_trace(go.Scatter(
            x=antibiotic_data['Age Group'], 
            y=antibiotic_data['Resistance_Percentage'], 
            mode='lines+markers',
            name=antibiotic,
            line=dict(color=colors[i % len(colors)]),  # Use different colors for each line
            text=[f"Age Group: {age_group}<br>R: {r}<br>S: {s}<br>%R: {percent_r:.2f}" 
                  for age_group, r, s, percent_r in zip(
                      antibiotic_data['Antibiotic'],
                      antibiotic_data['R'],
                      antibiotic_data['S'],
                      antibiotic_data['Resistance_Percentage']
                  )],
            hoverinfo='text'
        ))

    # Update layout to ensure the legend is placed on the right and hovermode is unified
    fig.update_layout(
        xaxis_title='Age Group',
        yaxis_title='Resistance Percentage (%)',
        title=f'Resistance Percentage by Age Group and Antibiotic in {country}',
        legend=dict(
            x=1.05,  # Place the legend outside the plot
            y=1,
            bgcolor='rgba(255, 255, 255, 0)',  # Transparent background
            bordercolor='black',
            borderwidth=1
        ),
        margin=dict(l=40, r=40, t=40, b=40)# Shows hover information for all traces at once
    )

    # Show the figure
    return fig,country_data


def plot_age_group(organism,selected_country):
    import pandas as pd
    import numpy as np
    
    if type(mapping[organism])==type([1,2]):
        import pandas as pd
        def combine_csv(file1, file2):
            # Load the two CSV files
            df1 = pd.read_csv(file1)
            df2 = pd.read_csv(file2)
            
            # Concatenate the two dataframes to get the original dataframe
            combined_df = pd.concat([df1, df2], ignore_index=True)
            
            return combined_df

        # Usage
        original_df = combine_csv(mapping[organism][0], mapping[organism][1])
        ecoli = original_df
    else:
        ecoli = pd.read_csv(mapping[organism],low_memory=False)
    if  organism=="Escherichia coli":
        ecoli.Source.replace("Vomit","Others",inplace=True)
        ecoli.Source.replace("Paracentesis Fluid","Bodily Fluids",inplace=True)
        ecoli.Source.replace("Ascetic Fluid","Bodily Fluids",inplace=True)
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if  organism=="Staphylococcus aureus":
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if organism=="Enterobacter spp":
        ecoli["Species"] = "Enterobacter spp"
    ec=ecoli.copy()
    df = ec[ec['Age Group'] != 'Unknown']

    # Filter data for the selected country
    df_country = df[df['Country'] == selected_country]

    # Calculate %R (resistance percentage)
    df_country['%R'] = (df_country['R'] / df_country['R_S_sum']) * 100

    # Remove '_I' from antibiotic names
    df_country['Antibiotic'] = df_country['Antibiotic'].str.replace('_I', '')

    # Pivot to show antibiotics and age groups with %R
    pivot_df = df_country.pivot(index='Antibiotic', columns='Age Group', values='%R').fillna(0)

    # Normalize the data
    pivot_df_normalized = (pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100).fillna(0)

    # Default color map for age groups
    default_colors = ['blue', 'orange', 'green', 'purple', 'red', 'cyan', 'magenta']

    # Create a dynamic color dictionary for all age groups found in the dataset
    age_groups = pivot_df_normalized.columns
    colors = {age_group: default_colors[i % len(default_colors)] for i, age_group in enumerate(age_groups)}

    # Create an empty list to hold traces (bars for each age group)
    traces = []

    # Loop through each age group to create a stacked bar trace
    for age_group in age_groups:
        # Prepare hover text for each antibiotic and age group
        hover_text = [
            f'Antibiotic: {antibiotic}<br>Age Group: {age_group}<br>% of R: {round(percent, 2)}%'
            for antibiotic, percent in zip(pivot_df_normalized.index, pivot_df_normalized[age_group])
        ]
        
        # Add the trace for the age group
        traces.append(go.Bar(
            x=pivot_df_normalized.index,  # Antibiotic names
            y=pivot_df_normalized[age_group],  # Normalized %R
            name=age_group,
            marker_color=colors[age_group],
            hoverinfo='text',
            hovertext=hover_text,  # Use hovertext for hover info
            showlegend=True,
            hoverlabel=dict(namelength=-1)  # Allow full name in hover
        ))

    # Create the figure with the stacked bar chart
    fig = go.Figure(data=traces)

    # Update layout for title, labels, and other aesthetic details
    fig.update_layout(
        title=f'Normalized R% by Antibiotic and Age Group in {selected_country}',
        xaxis_title='Antibiotic',
        yaxis_title='Normalized R%',
        barmode='stack',  # Stacked bar chart mode
        hovermode='closest',  # Show hover info only for the closest sub-bar
        legend_title_text='Age Group'
    )

    return fig
    
def conplot_geo(organism):
    import pandas as pd
    import plotly.express as px
    
    if type(mapping[organism])==type([1,2]):
        import pandas as pd
        def combine_csv(file1, file2):
            # Load the two CSV files
            df1 = pd.read_csv(file1)
            df2 = pd.read_csv(file2)
            
            # Concatenate the two dataframes to get the original dataframe
            combined_df = pd.concat([df1, df2], ignore_index=True)
            
            return combined_df

        # Usage
        original_df = combine_csv(mapping[organism][0], mapping[organism][1])
        ecoli = original_df
    else:
        ecoli = pd.read_csv(mapping[organism],low_memory=False)
    if  organism=="Escherichia coli":
        ecoli.Source.replace("Vomit","Others",inplace=True)
        ecoli.Source.replace("Paracentesis Fluid","Bodily Fluids",inplace=True)
        ecoli.Source.replace("Ascetic Fluid","Bodily Fluids",inplace=True)
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if  organism=="Staphylococcus aureus":
        ecoli["In / Out Patient"].replace(np.NaN,"None Given",inplace=True)
        ecoli["Gender"].replace(np.NaN,"N",inplace=True)
    if organism=="Enterobacter spp":
        ecoli["Species"] = "Enterobacter spp"
    ec=ecoli.copy()
    ec_country_above_500=ec[ec.Country.isin(ec.Country.value_counts()[ec.Country.value_counts()>500].index)]
    clean_ec_cols_plot3=list(ec_country_above_500.columns[ec_country_above_500.columns.str.contains("_I")])
    ec_plot3 = ec_country_above_500.melt(id_vars=['Country'], 
                    value_vars=clean_ec_cols_plot3,
                    var_name='Antibiotic', value_name='Resistance')
    ec_pv_plot3 = ec_plot3.pivot_table(index=['Country'], 
                               columns='Resistance', 
                               aggfunc='size', 
                               fill_value=0).reset_index()
    data = ec_pv_plot3.copy()

    # Calculate R% as (R / (R + S)) * 100
    data['R%'] = (data['R'] / (data['R'] + data['S'])) * 100

    # Creating a new column to categorize R% into the required ranges
    def categorize_r_percentage(r):
        if 0 <= r <= 10:
            return '0-10'
        elif 11 <= r <= 20:
            return '11-20'
        elif 21 <= r <= 30:
            return '21-30'
        elif 31 <= r <= 40:
            return '31-40'
        elif 41 <= r <= 50:
            return '41-50'
        else:
            return '51-100'

    data['r_category'] = data['R%'].apply(categorize_r_percentage)

    # Sort the categories to ensure the legend appears in the right order
    category_order = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-100']

    # Create the Choropleth map with hover data formatted as required
    fig = px.choropleth(
        data_frame=data,
        locations="Country",  # Column with country names
        locationmode="country names",  # Mode to use full country names
        color="r_category",  # The color based on the r% range
        hover_name="Country",  # Display country name on hover
        hover_data={
            "R%": ':.2f',  # Show R% with 2 decimal places
            "R": True,  # Display R count
            "S": True  # Display S count
        },
        color_discrete_sequence=["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#8B00FF"],  # 6 bright colors
        category_orders={"r_category": category_order},  # Ensure correct legend order
        title="Country Map Shaded by % of R",
        labels={"r_category": "% of R Range"}
    )

    # Customize hover template to match the requested format
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>" +  # Country name
                    "% of R: %{customdata[0]:.2f}<br>" +  # Correct format for % of R
                    "#R: %{customdata[1]}<br>" +  # R count
                    "#S: %{customdata[2]}"  # S count
    )

    # Customize layout for horizontal dynamic resizing
    fig.update_layout(
        autosize=True,
        width=None,  # Map width will dynamically adjust
        height=500,  # Fixed height to make it horizontally dynamic
    )

    fig.update_geos(
        showcoastlines=True,
        projection_type="natural earth"
    )

    # Show the dynamic map
    return fig
        
        
        
