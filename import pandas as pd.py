import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
installations_df = pd.read_csv("C:\Chemin\Vers\Installations.csv")
logons_df = pd.read_csv("C:\Chemin\Vers\Logons.csv")

# Convertir la colonne de date en format de date
installations_df['TimeCreated'] = pd.to_datetime(installations_df['TimeCreated'])
logons_df['TimeCreated'] = pd.to_datetime(logons_df['TimeCreated'])

# Groupement par semaine
installations_by_week = installations_df.resample('W-Mon', on='TimeCreated').count()
logons_by_week = logons_df.resample('W-Mon', on='TimeCreated').count()

# Tracer le nombre d'événements au fil des semaines
plt.plot(installations_by_week.index, installations_by_week['EventID'], label='Installations')
plt.plot(logons_by_week.index, logons_by_week['EventID'], label='Logons')

# Ajouter des étiquettes et une légende
plt.title('Nombre d\'Événements au Fil des Semaines')
plt.xlabel('Semaines')
plt.ylabel('Nombre d\'Événements')
plt.legend()

# Afficher le graphique
plt.show()