import pandas as pd
import numpy as np

# Given data
data = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    'Title': ['The Witcher 3: Wild Hunt', 'Grand Theft Auto V', 'Red Dead Redemption 2', 'The Legend of Zelda: Breath of the Wild',
              'Fortnite', 'Minecraft', 'Overwatch', 'Call of Duty: Modern Warfare', 'FIFA 21', 'Assassin\'s Creed Valhalla',
              'Cyberpunk 2077', 'Super Mario Odyssey', 'God of War', 'Spider-Man: Miles Morales', 'Destiny 2', 'Apex Legends',
              'Animal Crossing: New Horizons', 'Battlefield V', 'Rainbow Six Siege', 'Halo Infinite',
              'Final Fantasy XV', 'DOOM Eternal', 'Cuphead', 'Among Us', 'Valorant', 'Genshin Impact', 'Fall Guys',
              'Borderlands 3', 'Dota 2', 'The Elder Scrolls V: Skyrim', 'Rocket League', 'NieR: Automata', 'Dead by Daylight',
              'Stardew Valley', 'GTA Online', 'The Last of Us Part II', 'League of Legends', 'Mortal Kombat 11',
              'Sekiro: Shadows Die Twice', 'Monster Hunter: World', 'Star Wars Jedi: Fallen Order', 'Tom Clancy\'s The Division 2',
              'CyberConnect2', 'Persona 5', 'Terraria', 'Resident Evil Village', 'StarCraft II', 'Far Cry 5', 'No Man\'s Sky',
              'Madden NFL 21', 'Watch Dogs: Legion', 'Rust', 'Mortal Shell'],
    'Platform': ['PS4', 'Xbox One', 'PC', 'Nintendo Switch', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform',
                 'Multiplatform', 'Nintendo Switch', 'PS4', 'PS5', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Nintendo Switch', 'Multiplatform', 'Multiplatform',
                 'Multiplatform', 'Multiplatform', 'PC', 'Multiplatform', 'Multiplatform', 'PC', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'PC', 'Multiplatform',
                 'PS4', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'PC', 'PS4', 'Multiplatform', 'PS4', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform',
                 'Multiplatform', 'PC', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform',
                 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform', 'Multiplatform'],
    'Sales (Millions)': [15, 110, 30, 20, 350, 200, 50, 120, 10, 60, 25, 17, 40, 7, 5, 80, 100, 180, 15, 70, 
                         12, 30, 5, 8, 30, 25, 18, 15, 40, 10, 60, 22, 8, 4, 3, 45, 7, 25, 90, 30, 
                         3, 12, 60, 30, 8, 15, 20, 9, 6, 15, 25, 7, 40, 5, 30, 2, 10, 6, 2, 0.5,
                         3, 8, 2, 5, 0.8]
}

# Find the maximum length among the arrays
max_length = max(len(data['Rank']), len(data['Title']), len(data['Platform']), len(data['Sales (Millions)']))

# Pad the arrays with NaN values to make them of equal length
data['Rank'] += [np.nan] * (max_length - len(data['Rank']))
data['Title'] += [np.nan] * (max_length - len(data['Title']))
data['Platform'] += [np.nan] * (max_length - len(data['Platform']))
data['Sales (Millions)'] += [np.nan] * (max_length - len(data['Sales (Millions)']))

# Create DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('video_games_dataset.csv', index=False)

# Display a message indicating the success
print("Data has been successfully saved to 'video_games_dataset.csv'")
