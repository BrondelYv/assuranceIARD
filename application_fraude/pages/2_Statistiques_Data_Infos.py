# Importation des modules
import streamlit as st
# pip install st-annotated-text
from annotated_text import annotated_text


# Configuration de la page
st.set_page_config(page_title="ClearFraudExpert - Statistiques Data Infos", page_icon="📊")

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
    <div class="small-text"> 📊 Statistiques Data Infos</div>
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


# Vérifier si les données existent dans st.session_state
if ('data' or 'db_connection') in st.session_state and \
    (st.session_state.data or st.session_state.db_connection)  is not None:
    text_size_title = "30px"

    st.write("")
    st.write(("#### Informations sur le dataset"))
    if 'data' in st.session_state:
        st.write("Nom du fichier:", st.session_state.data["file_name"])
        df = st.session_state.data["data"]
        st.write("")
        #----------------------------------------------

        # Afficher les informations sur le DataFrame
        st.write("#### Aperçu des données")
        st.write(df.head())

        # Utilisation de colonnes pour un affichage plus ordonné
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### Dimensions du dataset")
            st.write(f"Nombre de lignes: {df.shape[0]}")
            st.write(f"Nombre de colonnes: {df.shape[1]}")

        with col2:
            st.write("#### Nombre de valeurs manquantes")
            st.write(f"Valeur : {df.isna().sum().sum()}")
        st.write("")
        #----------------------------------------------

        st.write("#### Liste des colonnes")
        # Création de 3 colonnes pour afficher les noms des colonnes du DataFrame
        col3, col4, col5 = st.columns(3)

        # Diviser la liste des colonnes en trois parties égales
        columns = df.columns.tolist()
        col3_list = columns[:len(columns)//3]
        col4_list = columns[len(columns)//3:2*len(columns)//3]
        col5_list = columns[2*len(columns)//3:]
        text_size_col = "12px"

        # Afficher les noms des colonnes dans chaque colonne de Streamlit
        with col3:
            for col in col3_list:
                st.markdown(f"<p style='font-size:{text_size_col};'>{col}</p>", unsafe_allow_html=True)

        with col4:
            for col in col4_list:
                st.markdown(f"<p style='font-size:{text_size_col};'>{col}</p>", unsafe_allow_html=True)

        with col5:
            for col in col5_list:
                st.markdown(f"<p style='font-size:{text_size_col};'>{col}</p>", unsafe_allow_html=True)
        #----------------------------------------------

        col6, col7 = st.columns(2)
        # Colonnes de types numériques
        with col6:
            st.write("#### Colonnes numériques")
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            st.write(numeric_columns)

        # Colonnes de types objet (catégorielles)
        with col7:
            st.write("#### Colonnes catégorielles")
            categorical_columns = df.select_dtypes(include=['object']).columns
            st.write(categorical_columns)
        #----------------------------------------------


        # Affichage des statistiques descriptives pour les colonnes numériques clés
        key_columns_int = ['Montant_Total_Souscrit', 'Montant_reclame_par_client', 'Temps_Investigation (jours)',\
                           'Montant_Final_Recouvre', 'Historique_Paiements_En_Retard']
        
        st.write("#### Statistiques descriptives des colonnes numériques clés")
        st.write(df[key_columns_int].describe())
        #----------------------------------------------


        # Affichage des valeurs uniques pour certaines colonnes catégorielles
        key_columns_obj = ['Canal_Souscription', 'Type_Client', 'Tranche_Age', 'Genre', 'Code_Postal', 'Code_Departement',\
            'Nom_Departement','Code_Region', 'Nom_Region', 'Statut_Familial', 'Tranche_Revenu_Annuel', 'Tranche_Anciennete',\
            'Jeune_conducteur','Tranche_nombre_sinistre', 'Tranche_nombre_Reclamations', 'Monorisque', \
            'Tranche_Nombre_Produits_Souscrits','Montant_Total_Souscrit', 'Type_Fraude', 'Montant_reclame_par_client',\
            'Decision_Finale', 'Temps_Investigation (jours)', 'Montant_Final_Recouvre', 'Incohérences_Déclarations',\
            'Réclamations_Multiples_Même_Sinistre', 'Réclamations_Similaires_Réseau','Tranche_Delai_entre_Souscription_sinistre',\
            'Moyens_Paiement', 'Historique_Paiements_En_Retard', 'Canal_Communication_Prefere','Participation_Campagnes_Promo',\
            'Score_Relation_Client', 'Risque_Geographique']
        
        st.write("#### Valeurs uniques pour certaines colonnes catégorielles")
        # Paramètre pour définir combien de colonnes Streamlit afficher
        num_cols = 3  # Nombre de colonnes de la mise en page
        columns_per_row = st.columns(num_cols)

        # Compteur pour savoir dans quelle colonne on écrit
        col_counter = 0

        # Boucle pour afficher les colonnes catégorielles et leurs valeurs uniques
        for column in key_columns_obj:
            if column in df.columns:
                unique_values = df[column].unique()

                # Ajouter l'affichage dans la colonne actuelle
                with columns_per_row[col_counter]:
                    st.write(f"**{column}**")
                    st.write(unique_values)

                # Passer à la colonne suivante
                col_counter += 1

                # Réinitialiser le compteur lorsqu'on atteint le nombre maximal de colonnes par ligne
                if col_counter == num_cols:
                    col_counter = 0
                    columns_per_row = st.columns(num_cols) 

        # Affichage de la distribution des décisions finales
        if 'Decision_Finale' in df.columns:
            st.write("#### Distribution des décisions finales")
            st.write(df['Decision_Finale'].value_counts())
            st.bar_chart(df['Decision_Finale'].value_counts())
        else:
            st.warning("La colonne 'Decision_Finale' est manquante.")

else:
    st.error("Aucun fichier ou base de données n'a été chargé. Veuillez charger les données sur la page '💼 New Data'.")