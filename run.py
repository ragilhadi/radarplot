import app.radarplot.src.radarplot as rd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('penguins')
species_mass = df[['species', 'bill_length_mm', 
                   'bill_depth_mm', 'body_mass_g',
                   'flipper_length_mm']].groupby('species').mean().reset_index()

rd.radarplot(data=species_mass, 
            category='species', 
            values=species_mass.columns[1:].to_list())
plt.savefig('result2.jpg')

data_minmax = rd.get_minmax(df, columns=['bill_length_mm', 
                   'bill_depth_mm', 'body_mass_g',
                   'flipper_length_mm'])

rd.radarplot(data=species_mass, 
            category='species', 
            data_minmax=data_minmax,
            values=species_mass.columns[1:].to_list())
plt.savefig('result2.jpg')