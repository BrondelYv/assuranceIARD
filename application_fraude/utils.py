from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder,StandardScaler, MinMaxScaler
import pandas as pd

# Fonction d'encodage des variables catégorielles
def encoder_categoriel(df, colonnes_onehot, colonnes_ordinal):
    # Encodage OneHot
    if colonnes_onehot:
        encoder_onehot = OneHotEncoder(sparse_output=False, drop='first')
        encoded_onehot_data = encoder_onehot.fit_transform(df[colonnes_onehot])
        df_onehot_encoded = pd.DataFrame(encoded_onehot_data, columns=encoder_onehot.get_feature_names_out(colonnes_onehot))
        df = pd.concat([df.drop(columns=colonnes_onehot), df_onehot_encoded], axis=1)
    
    # Encodage Ordinal
    if colonnes_ordinal:
        encoder_ordinal = OrdinalEncoder()
        df[colonnes_ordinal] = encoder_ordinal.fit_transform(df[colonnes_ordinal])
    
    return df

# Fonction de normalisation
def normaliser_colonnes(df, colonnes_numeriques, type_normalisation="standard"):
    if type_normalisation == "standard":
        scaler = StandardScaler()
    else:
        scaler = MinMaxScaler()

    df[colonnes_numeriques] = scaler.fit_transform(df[colonnes_numeriques])
    return df
# Fonction pour séparer les features et la cible
def separate_features_and_target(df, target_column):
    """
    Sépare les features (X) et la variable cible (y) dans un dataframe.

    :param df: Le dataframe contenant les données.
    :param target_column: Le nom de la colonne cible à séparer.
    :return: X (features) et y (target)
    """
    X = df.drop(target_column, axis=1)  # Supprimer la colonne cible des features
    y = df[target_column]  # Cible
    return X, y


