import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the gene cell photo image
cell_image = Image.open('4.png')

# Convert the image to a numpy array
cell_image_data = np.array(cell_image)

# Get the dimensions of the image
height, width, channels = cell_image_data.shape

# Reshape the image array to a 2D array with pixel values
gene_expression_data = cell_image_data.reshape(height * width, channels)

# Create a pandas DataFrame with the pixel values
gene_expression_df = pd.DataFrame(gene_expression_data)

# Add a column for the gene expression values
# NOTE: Replace with actual gene expression values
rng = np.random.default_rng()
gene_expression_df['Gene_Expression'] = rng.normal(loc=0, scale=1, size=len(gene_expression_df))

# Add a column for the cell type
# NOTE: Replace with actual cell type values
gene_expression_df['Cell_Type'] = rng.binomial(n=1, p=0.5, size=len(gene_expression_df))

# Print the first few rows of the DataFrame
print(gene_expression_df.head())

# Visualize the distribution of gene expression values
plt.violinplot(gene_expression_df['Gene_Expression'])
plt.title('Gene Expression Distribution')
plt.xlabel('Gene Expression')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between gene expression and cell type
plt.scatter(gene_expression_df['Gene_Expression'], gene_expression_df['Cell_Type'])
plt.title('Gene Expression vs Cell Type')
plt.xlabel('Gene Expression')
plt.ylabel('Cell Type')
plt.show()