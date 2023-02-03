import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv (r'NBS.csv')
print (df)
sns.set_theme(style="whitegrid")
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="NBS", y="Chromosomes", data=df,
            label="NBS", color="c")
sns.set_color_codes("muted")
sns.barplot(x="RLP", y="Chromosomes", data=df,
            label="RLP", color="b")
sns.set_color_codes("muted")
sns.barplot(x="RLK", y="Chromosomes", data=df,
            label="RLK", color="c")
ax.legend(ncol=2, loc="best", frameon=True)
ax.set(xlim=(0, 30), ylabel="",
       xlabel="RLK, RLP and NBS distributions across the chromosomes")
sns.despine(left=True, bottom=True)
plt.show()
