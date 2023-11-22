# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
plt.rc('font', size=12) # font size 
plt.rc('axes', labelsize=14, titlesize=14) # font size of axis and label titles 
plt.rc('legend', fontsize=12) # font size of legend
plt.rc('xtick', labelsize=5) # size of ticks on x-axis
plt.rc('ytick', labelsize=10) # size of ticks on y-axis
#
#
#
#
#
#
#
data_source_raw = "../../datasets/pokemon.csv"
data_source_result = pd.read_csv(data_source_raw)
data_source_result
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
- `height_m`
- `percentage_male`
- `weight_kg`
data_source_result.info()
#
#
#
#
#
#
#
#
#
generation_legends = data_source_result[["generation", "is_legendary"]]
generation_legends = generation_legends.rename(columns={'is_legendary':"Legendary", 'generation':"Generation"})
#
#
#
#
#
#
#
#
#
#
#
legendary_per_generation = generation_legends.groupby("Generation").agg({"Legendary":"sum", "Generation":"first"})
legendary_per_generation[['Legendary']].sort_values(by="Legendary", ascending=False)
#
#
#
#
#
legendary_per_generation.plot(kind="bar", x="Generation", y="Legendary", title="Legendary Pokemon Per Generation", ylabel="Number of Legendary Pokemon", legend=False)
plt.axis([-1,7 , 0, 25])
plt.show()
#
#
#
#
#
#
#
generation_num = 7
gen7_pokemon = data_source_result[data_source_result['generation']==generation_num]
#
#
#
#
#
legendary_pokemon = gen7_pokemon['is_legendary']
legendary_percentages = legendary_pokemon.value_counts(normalize=True)
#
#
#
#
#
legendary_percentages = pd.Series(legendary_percentages.values, index=legendary_pokemon.unique())
legendary_percentages
#
#
#
#
legendary_percentages.plot(kind="pie", ylabel="", title="% of Legendary Gen 7 Pokemon", labels=["Not Legendary", "Legendary"], autopct='%.1f%%')
plt.show()
We could also factor in conditional probablity and Bayes' Theorem. If we were to play a guessing game for every single Pokemon in this dataset, guessing the right Pokemon would be really challenging because there is over 800 Pokemon. We would have only a 0.12% chance of guessing right!
total_num_pokemon = data_source_result['pokedex_number'].count()
1/total_num_pokemon * 100
But what if we found out that the Pokemon is in Generation 1 and is also a legendary pokemon? That would certainly increase our odds!

Here we can filter for Pokemon that appear in Generation 1, filter for the legendary Pokemon, and then get the count which is 5. 
gen1_pokemon = data_source_result[data_source_result['generation']==1]
legendary_gen1 = gen1_pokemon[gen1_pokemon['is_legendary']==1]
legendary_gen1_count = legendary_gen1['name'].count()


We then do 1 divided by the count to get our new odds. We have improved our guessing odds from 0.1% to 20%!
1/legendary_gen1_count * 100
#
#
#
