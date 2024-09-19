# Importation des modules
import streamlit as st
# pip install st-annotated-text
from annotated_text import annotated_text
import streamlit.components.v1 as components
import pandas as pd
from utils import encoder_categoriel, normaliser_colonnes
import matplotlib.pyplot as plt


# Configuration de la page
st.set_page_config(page_title="ClearFraudExpert - Valdiation/Exportation", page_icon="🕵️‍♂️")

# Ajout des styles pour la page (CSS) avec des couleurs personnalisées,
# des bordures arrondies, et des polices de caractères
st.html(
    """
    <style>
    [data-testid="stSidebarContent"] {
        color: grey;
        background-color: #FEFEFE;
    }
    </style>

    <style>
    /* Style for the sidebar */
    .css-1d391kg .css-1l02zno, .css-1d391kg .css-17eq0hr, .css-1d391kg .css-k4mp6c {  /* Sidebar text color */
        color: grey;
        font-size: 50px;}
    
    /* Main page background */
    .stApp {
        background-color: #EBF4F7;
    }
    
    /* Style for the main container (white background) */
    .main-container {
        background-color: #FFFFFF;
        border-radius: 10px;
        font-family: 'Arial';
    }
    
    /* Style for col1 and col2 containers */
    .col-container {
        background-color: #FFFBEC;
        border-radius: 10px;
    }
    
    /* Style for buttons */
    div.stButton > button {
        background-color: #EFE9FF;
        color: black;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
    }
    
    /* Text alignment for header */
    .header-text {
        color: black;
    }
    
    </style>
    """
)

# Navigation du coté Sidebar
# et écriture des titres des différentes pages
st.sidebar.title("ClearFraudExpert")
st.sidebar.write("")
st.sidebar.title("User Panel")
st.sidebar.markdown(
    """
    <style>
    .small-text {
        background-color: #EFE9FF;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px !important;  /* Force smaller text size */
        color: grey;
    }
    </style>
    <div class="small-text"> 🕵️‍♂️ Valdiation/Exportation</div>
    """,
    unsafe_allow_html=True
)

# 1ere section de la page avec mise en forme 
# de la boîte de recherche et de la notification avec le nom de l'utilisateur
col1, col2, col3, col4 = st.columns(4)
with col1:
    pass
with col2:
    pass
with col3:
    st.markdown(
        """
        <style>
        .alert-band {
            background-color: #F6F6F6; /* Light red background for the alert */
            padding: 10px;
            border-radius: 10px;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            color: black;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Optional shadow for better visibility */
        }
        .alert-band .emoji {
            font-size: 15px; /* Adjust size of the emoji */
            margin-left: 10px; /* Space between emoji and text */
        }
        </style>
        <div class="alert-band">
            Rechercher....<span class="emoji">🔍</span> 
        </div>
        """,
        unsafe_allow_html=True
    )
with col4:
        st.markdown(
        """
        <style>
        .alert-band {
            background-color: #F6F6F6; /* Light red background for the alert */
            padding: 10px;
            border-radius: 10px;
            align-items: center;
            justify-content: center;
            font-size: 13x;
            color: black;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Optional shadow for better visibility */
        }
        .alert-band .emoji {
            font-size: 16px; /* Adjust size of the emoji */
            margin-left: 10px; /* Space between emoji and text */
        }
        </style>
        <div class="alert-band">
            <span class="page-title-name-user">Alfred Brandson<span   ><span class="emoji">🔔</span> 
        </div>
        """,
        unsafe_allow_html=True
    )


# 2e section avec salutation et message de bienvenue
st.write("")
st.write("")
st.markdown(
    """
    <style>
    .page-title {
        font-size: 20px !important;  /* Force smaller text size */
        color: black;
        font-weight: bold;
        
    }
    .page-title-name-user {
        font-weight: bold;
        color: #8239D6;
    }
    </style>
    <div class="page-title"> 👋 Bonjour, <span class="page-title-name-user">Alfred Brandson<span></div>
    """,
    unsafe_allow_html=True
)
# Charger le modèle sélectionné pour faire des prédictions sur un nouveau jeu de données
if 'best_model' in st.session_state:

    # Télécharger un nouveau fichier pour les prédictions
    df_data = st.file_uploader("Téléchargez un nouveau fichier de données pour les prédictions", type=["csv", "xlsx"])
    #df_data = pd.read_excel('Fichier_fraude_assurance_test.xlsx')

    if df_data is not None:
        #Charger les nouvelles données à prédire
        if df_data.name.endswith('.csv'):
           df_data_charged = pd.read_csv(df_data)
        else:
           df_data_charged = pd.read_excel(df_data)

        #st.write("### Données téléchargées :")
        #st.write(df_new)

        # Appliquer le même processus de préparation que sur le jeu de données d'entraînement
        # 1. Suppression des colonnes inutiles
        if 'colonnes_a_supprimer' in st.session_state:
            df_suppressed_new = df_data_charged[st.session_state['colonnes_a_supprimer']].copy()  # Sauvegarder les colonnes supprimées
            df_new = df_data_charged.drop(columns=st.session_state['colonnes_a_supprimer'])
            df_new = df_new.drop(['Decision_Finale'], axis=1)

            # 2. Normalisation et encodage (comme effectué durant l'entraînement)
            colonnes_numeriques = ['Montant_reclame_par_client', 'Montant_Total_Souscrit', 'Temps_Investigation (jours)']
            colonnes_onehot = ['Canal_Souscription', 'Type_Client', 'Tranche_Age', 'Genre', 'Statut_Familial', 'Tranche_nombre_Reclamations',
                            'Tranche_Revenu_Annuel', 'Tranche_Anciennete', 'Tranche_nombre_sinistre', 'Tranche_Nombre_Produits_Souscrits',
                            'Type_Fraude', 'Tranche_Delai_entre_Souscription_sinistre', 'Canal_Communication_Prefere']
            colonnes_ordinal = ['Jeune_conducteur', 'Monorisque', 'Réclamations_Multiples_Même_Sinistre', 'Réclamations_Similaires_Réseau',
                                'Moyens_Paiement', 'Participation_Campagnes_Promo', 'Score_Relation_Client', 'Risque_Geographique']

            # Normaliser les colonnes numériques
            df_new = normaliser_colonnes(df_new, colonnes_numeriques, "standard")

            # Encoder les colonnes catégorielles
            df_new_encoded = encoder_categoriel(df_new, colonnes_onehot, colonnes_ordinal)

            # Faire les prédictions avec le modèle sélectionné
            y_pred_new = st.session_state['best_model'].predict(df_new_encoded)

            # Réintégrer les colonnes supprimées dans les résultats
            df_final = df_data_charged.copy()
            df_final['Prédiction'] = y_pred_new

            # Afficher les résultats avec les colonnes supprimées réintégrées
            st.write("### Résultats des prédictions :")
            st.write(df_final)

            # Fonction pour convertir le DataFrame en CSV
            def convert_df_to_csv(df):
                return df.to_csv(index=False).encode('utf-8')

            # Télécharger les résultats
            csv_results = convert_df_to_csv(df_final)
            
            st.download_button(
                label="Télécharger les prédictions en CSV",
                data=csv_results,
                file_name='predictions_final.csv',
                mime='text/csv'
            )

            df_caseid_decision_predict = df_final[['Case ID', 'Decision_Finale', 'Prédiction']]
            # Fonction pour appliquer le style conditionnel
            def color_row(val):
                if val == 'Pas de Fraude' or val == 0:
                    return 'color: blue'
                elif val == 'Fraude' or val == 1:
                    return 'color: red'
                return ''

            # Application du style aux colonnes Decision_Finale et Prédiction
            styled_df = df_caseid_decision_predict.style.applymap(color_row, subset=['Decision_Finale', 'Prédiction'])

            st.write("#### Résultats des prédictions :")
            st.write(styled_df)

            # Represenation en pie chart
            # Nombre de fraudes et non fraudes
            # Définir le nombre de colonn|es par ligne
            num_cols_pie = 2
            columns_per_row_pie = st.columns(num_cols_pie)

            # Fonction pour associer les couleurs aux valeurs spécifiques
            def get_colors(values):
                color_map = {
                    'Pas de Fraude': '#4f81bd',  # Cas des décisions en texte
                    'Fraude': '#c0504d',
                    0: '#4f81bd',                # Cas des prédictions en entiers
                    1: '#c0504d'
                }
                return [color_map.get(v, 'gray') for v in values]

            # Création des pie charts
            for idx, column in enumerate(['Decision_Finale', 'Prédiction']):
                with columns_per_row_pie[idx % num_cols_pie]:
                    # Sélectionner les données et compter les occurrences
                    counts = df_caseid_decision_predict[column].value_counts()
                    
                    # Associer les couleurs en fonction des catégories
                    colors = get_colors(counts.index)

                    # Créer le graphique en camembert
                    fig, ax = plt.subplots(figsize=(8, 8))
                    counts.plot(
                        kind='pie', 
                        autopct=lambda pct: f'{pct:.1f}%', 
                        startangle=90, 
                        ax=ax, 
                        colors=colors,
                        textprops={'fontsize': 22}  # Taille du texte des pourcentages
                    )
                    
                    ax.set_ylabel('')
                    ax.set_title(f'Distribution de {column}', fontsize=17)  # Optionnel : agrandir aussi le titre
                    st.pyplot(fig)

                # Réinitialiser les colonnes lorsque l'on atteint la limite définie par num_cols_pie
                if (idx + 1) % num_cols_pie == 0:
                    columns_per_row_pie = st.columns(num_cols_pie)

        else:
            st.error("Colonnes à supprimer non disponibles.")
            st.stop()

else:
    st.error("Aucun modèle n'a été sélectionné pour faire des prédictions.")
