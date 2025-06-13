import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("product_info.csv")

df=df.dropna(subset=['id','title','brand','category','price'])

#barchart of product category
catg_count=df['category'].value_counts()
plt.figure(figsize=(6,6))
plt.bar(catg_count.index,catg_count.values,color="green")
plt.title("barchart for category for products")
plt.xlabel('category')
plt.ylabel('quantity')
plt.grid(color="gray",linestyle=":")
plt.savefig('\python folder\projects\barchart.png',dpi=100)


#horizontal-barchart for ratings fro products
prod_count=df['title']
rating_count=df['rating']
plt.figure(figsize=(8,8))
plt.barh(prod_count,rating_count,color='yellow')
plt.title("h-barchart for ratings display")
plt.xlabel('ratings')
plt.ylabel('products')
plt.grid(color='gray',linestyle='--',linewidth=1.2)
plt.savefig('python folder\projects\h-barchart.png',dpi=100,bbox_inches='tight')

# #pie chart for brands of products
brand_count=df['brand'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(brand_count,labels=brand_count.index,autopct='%1.f%%')
plt.title("Pie Chart of Brands of Products")
plt.savefig('python folder\projects\visualization.py\piechart.png',dpi=100,bbox_inches='tight')

plt.tight_layout()
plt.show()
