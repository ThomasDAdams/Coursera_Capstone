
import pandas as pd
import wikipedia as wp


# More than one neighborhood can exist in one postal code area. For example, in the table on the Wikipedia page, you will notice that M5A is listed twice and has two neighborhoods: Harbourfront and Regent Park. These two rows will be combined into one row with the neighborhoods separated with a comma as shown in row 11 in the above table.
# If a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough. So for the 9th cell in the table on the Wikipedia page, the value of the Borough and the Neighborhood columns will be Queen's Park.
# Clean your Notebook and add Markdown cells to explain your work and any assumptions you are making.
# In the last cell of your notebook, use the .shape method to print the number of rows of your dataframe.


# grabbed the table from wiki and saved to a df & csv
html = wp.page("List_of_postal_codes_of_Canada:_M").html().encode("UTF-8")
Toronto_FSA = pd.read_html(html)[0]
Toronto_FSA.to_csv('beautifulsoup_toronto.csv',header=0,index=False)

# filter out Not assigned entries
filter_tor1 = Toronto_FSA[Toronto_FSA['Borough'] != 'Not assigned'].reset_index(drop=True)
# if postcode is same for any rows. Combine the two rows with the neighborhoods separated with a comma
#filter_tor1.groupby('Postcode').agg({'Neighbourhood': 'sum', '': lambda x: ' '.join(x)})
filter_tor2 = filter_tor1.groupby('Postcode')['Neighbourhood'].unique().agg(', '.join)
filter_tor2v = filter_tor1.groupby('Postcode')['Borough'].unique().agg(', '.join)
toronto_final = pd.concat([filter_tor2v, filter_tor2], axis=1).reset_index()


print(toronto_final.shape)



    