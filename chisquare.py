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

def plot_antibiotic_resistance(organism):
    mapping = {
        "Escherichia coli" : ["./resource/resource/Final data/Ecoli data/Final_Ecoli1.csv","./resource/resource/Final data/Ecoli data/Final_Ecoli2.csv"],
        "Enterococcus faecium" : "./resource/resource/Final data/EF data/Final_EF.csv",
        "Klebsiella pneumoniae" : "./resource/resource/Final data/KP data/Final_KP.csv",
        "Acinetobacter baumannii" : "./resource/resource/Final data/AB data/Final_AB.csv",
        "Pseudomonas aeruginosa" : "./resource/resource/Final data/PA data/Final_PA.csv",
        "Staphylococcus aureus" : ["./resource/resource/Final data/SA data/Final_SA1.csv","./resource/resource/Final data/SA data/Final_SA2.csv"],
        "Enterobacter cloacae" : "./resource/resource/Final data/EB data/Final_EB.csv"
    }
    #df = pd.read_csv("cs_res2.csv",low_memory=False)
    df = pd.read_csv("cs_res.csv", encoding='ISO-8859-1', low_memory=False)

    print(df.head())
    # Convert 'R' and 'S' columns to numeric, coercing errors to NaN
    df['R'] = pd.to_numeric(df['R'], errors='coerce')
    df['S'] = pd.to_numeric(df['S'], errors='coerce')

    # Drop rows where 'S' is zero or NaN to avoid division by zero and invalid calculations
    df = df[df['S'] > 0]

    # Group by Organism, Antibiotics, and Year, and sum R and S values
    grouped_df = df.groupby(['Organism', 'Antibiotics', 'Year']).agg({'R': 'sum', 'S': 'sum'}).reset_index()

    # Calculate the percentage of resistant cases
    grouped_df['%R'] = (grouped_df['R'] / (grouped_df['R'] + grouped_df['S'])) * 100

    # Debugging: Print columns and head of grouped_df to check if %R is present
    print("Columns in grouped_df:", grouped_df.columns)
    print("Head of grouped_df:", grouped_df.head())

    # Filter data for the specific organism
    if "Enterobacter" in organism:
        organism = "Enterobacter spp"
    organism_data = grouped_df[grouped_df['Organism'] == organism]

    # Get unique antibiotics for this organism
    antibiotics = organism_data['Antibiotics'].unique()

    # Create a new figure for this organism
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot data for each antibiotic with markers
    for antibiotic in antibiotics:
        antibiotic_data = organism_data[organism_data['Antibiotics'] == antibiotic]
        # Check if %R column is present
        if '%R' in antibiotic_data.columns:
            ax.plot(antibiotic_data['Year'], antibiotic_data['%R'], label=antibiotic, marker='o')
        else:
            print(f"%R column not found for {antibiotic}")

    # Customize the plot
    ax.set_xlabel('Year')
    ax.set_ylabel('% of R')
    ax.set_title(f'Antibiotic Resistant Profile for {organism}')
    ax.legend(title='Antibiotics')
    ax.grid(True)

    # Format x-axis ticks as whole numbers
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels([int(x) for x in ax.get_xticks()])

    # Return the plot object
    return fig

def get_cons(organism):
    import pandas as pd
    import numpy as np
    mapping = {
        "Escherichia coli" : ["./resource/resource/Final data/Ecoli data/Final_Ecoli1.csv","./resource/resource/Final data/Ecoli data/Final_Ecoli2.csv"],
        "Enterococcus faecium" : "./resource/resource/Final data/EF data/Final_EF.csv",
        "Klebsiella pneumoniae" : "./resource/resource/Final data/KP data/Final_KP.csv",
        "Acinetobacter baumannii" : "./resource/resource/Final data/AB data/Final_AB.csv",
        "Pseudomonas aeruginosa" : "./resource/resource/Final data/PA data/Final_PA.csv",
        "Staphylococcus aureus" : ["./resource/resource/Final data/SA data/Final_SA1.csv","./resource/resource/Final data/SA data/Final_SA2.csv"],
        "Enterobacter cloacae" : "./resource/resource/Final data/EB data/Final_EB.csv"
    }
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
def plot_country_group(organism,country):
    import pandas as pd
    import numpy as np
    mapping = {
        "Escherichia coli" : ["./resource/resource/Final data/Ecoli data/Final_Ecoli1.csv","./resource/resource/Final data/Ecoli data/Final_Ecoli2.csv"],
        "Enterococcus faecium" : "./resource/resource/Final data/EF data/Final_EF.csv",
        "Klebsiella pneumoniae" : "./resource/resource/Final data/KP data/Final_KP.csv",
        "Acinetobacter baumannii" : "./resource/resource/Final data/AB data/Final_AB.csv",
        "Pseudomonas aeruginosa" : "./resource/resource/Final data/PA data/Final_PA.csv",
        "Staphylococcus aureus" : ["./resource/resource/Final data/SA data/Final_SA1.csv","./resource/resource/Final data/SA data/Final_SA2.csv"],
        "Enterobacter cloacae" : "./resource/resource/Final data/EB data/Final_EB.csv"
    }
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
    dff = ec_pv_plot1_final
    import pandas as pd
    import plotly.graph_objects as go

    # Load the dataset
    data = dff

    # Filter data for a specific country, e.g., 'Ukraine'
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
            hovertemplate=(
                '<br>------------------<br>' +
                'Age Group: %{x}<br>' +
                'Resistance: %{y:.2f} %<br>' +  # Properly formatted percentage
                # Separation line added
                'R count: %{customdata[0]:,.0f}<br>' +  # Ensure numbers are formatted
                'S count: %{customdata[1]:,.0f}<br>' +
                'Antibiotic: %{text}<extra></extra>'
            ),
            text=[antibiotic] * len(antibiotic_data),  # Set the text for each hover entry
            customdata=antibiotic_data[['R', 'S']].values  # Include R and S in hover data
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
        margin=dict(l=40, r=40, t=40, b=40),
        hovermode='x unified'  # Shows hover information for all traces at once
    )

    # Show the figure
    return fig

def plot_age_group(organism,age):
    import pandas as pd
    import numpy as np
    mapping = {
        "Escherichia coli" : ["./resource/resource/Final data/Ecoli data/Final_Ecoli1.csv","./resource/resource/Final data/Ecoli data/Final_Ecoli2.csv"],
        "Enterococcus faecium" : "./resource/resource/Final data/EF data/Final_EF.csv",
        "Klebsiella pneumoniae" : "./resource/resource/Final data/KP data/Final_KP.csv",
        "Acinetobacter baumannii" : "./resource/resource/Final data/AB data/Final_AB.csv",
        "Pseudomonas aeruginosa" : "./resource/resource/Final data/PA data/Final_PA.csv",
        "Staphylococcus aureus" : ["./resource/resource/Final data/SA data/Final_SA1.csv","./resource/resource/Final data/SA data/Final_SA2.csv"],
        "Enterobacter cloacae" : "./resource/resource/Final data/EB data/Final_EB.csv"
    }
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
    ec=ecoli.copy()
    ec['Age Group'].value_counts()
    clean_ec=ec[ec['Age Group'] != 'Unknown']
    clean_ec_cols_plot2=list(clean_ec.columns[clean_ec.columns.str.contains("_I")])
    ec_plot2 = clean_ec.melt(id_vars=['Age Group','Year'], 
                    value_vars=clean_ec_cols_plot2,
                    var_name='Antibiotic', value_name='Resistance')
    ec_pv_plot2 = ec_plot2.pivot_table(index=['Age Group','Year','Antibiotic'], 
                               columns='Resistance', 
                               aggfunc='size', 
                               fill_value=0).reset_index()
    ec_pv_plot2['R_S_sum']=ec_pv_plot2['R']+ec_pv_plot2['S']
    ec_pv_plot2_final=ec_pv_plot2[ec_pv_plot2['R_S_sum']>10]
    dff = ec_pv_plot2_final
    import pandas as pd
    import plotly.graph_objects as go

    # Load the dataset
    data = dff

    # Remove '_I' from all antibiotic names
    data['Antibiotic'] = data['Antibiotic'].str.replace('_I', '', regex=False)

    # Remove Colistin antibiotic for all age groups
    data = data[data['Antibiotic'] != 'Colistin']

    
    filtered_data = data[data['Age Group'] == age]

    # Check if there is data for this age group, if not, skip plotting
    if filtered_data.empty:
        print(f"No data available for the age group: {age}")
    else:
        # Calculate the percentage of resistance (R / (R + S) * 100) for each antibiotic
        filtered_data['Resistance_Percent'] = (filtered_data['R'] / (filtered_data['R'] + filtered_data['S'])) * 100

        # Create the figure
        fig = go.Figure()

        # Add line plots for each antibiotic
        for antibiotic in filtered_data['Antibiotic'].unique():
            antibiotic_data = filtered_data[filtered_data['Antibiotic'] == antibiotic]
            fig.add_trace(go.Scatter(
                x=antibiotic_data['Year'], 
                y=antibiotic_data['Resistance_Percent'], 
                mode='lines+markers',
                name=antibiotic,
                hovertemplate=(
                    'Year: %{x}<br>Resistance: %{y:.2f}%<br>Antibiotic: ' + antibiotic +
                    '<br>------------------<br>' +  # Separation line added
                    'R: %{customdata[0]}<br>S: %{customdata[1]}'
                ),
                customdata=antibiotic_data[['R', 'S']].values  # Include R and S in hover data
            ))

        # Update layout to ensure the x-axis uses whole numbers and the legend is placed on the right
        fig.update_layout(
            xaxis=dict(title='Year', tickmode='linear', tick0=filtered_data['Year'].min(), dtick=1),
            yaxis_title='Resistance (%)',
            title=f"Resistance (%) Over the Years - Age Group: {age}",
            legend=dict(
                x=1.05,  # Place the legend outside the plot
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',  # Transparent background
                bordercolor='black',
                borderwidth=1
            ),
            hovermode='x unified'  # Shows hover information for all traces at once
        )

        # Show the figure
        return fig
    
def conplot_geo(organism):
    import pandas as pd
    import plotly.express as px
    mapping = {
        "Escherichia coli" : ["./resource/resource/Final data/Ecoli data/Final_Ecoli1.csv","./resource/resource/Final data/Ecoli data/Final_Ecoli2.csv"],
        "Enterococcus faecium" : "./resource/resource/Final data/EF data/Final_EF.csv",
        "Klebsiella pneumoniae" : "./resource/resource/Final data/KP data/Final_KP.csv",
        "Acinetobacter baumannii" : "./resource/resource/Final data/AB data/Final_AB.csv",
        "Pseudomonas aeruginosa" : "./resource/resource/Final data/PA data/Final_PA.csv",
        "Staphylococcus aureus" : ["./resource/resource/Final data/SA data/Final_SA1.csv","./resource/resource/Final data/SA data/Final_SA2.csv"],
        "Enterobacter cloacae" : "./resource/resource/Final data/EB data/Final_EB.csv"
    }
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
        
        
        
