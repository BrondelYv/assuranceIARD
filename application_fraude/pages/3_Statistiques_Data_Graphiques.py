# Importation des modules
from matplotlib import pyplot as plt
import seaborn as sns 
import streamlit as st
import pandas as pd
# pip install st-annotated-text
from annotated_text import annotated_text
import geopandas as gpd



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
    <div class="small-text"> 📊 Statistiques Data Graphiques</div>
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
        if 'colomn_to_delete' not in st.session_state:
            st.session_state['colomn_to_delete'] = []
        
        if 'df_graphiques' not in st.session_state:
            st.session_state['df_graphiques'] = None
        
        if 'colonnes_piechart' not in st.session_state:
            st.session_state['colonnes_piechart'] = []
        


        st.write("### Sélectionnez les colonnes à supprimer")
       
        colonnes = df.columns.tolist()
        
        colomn_to_delete = st.multiselect(
            "Choisissez les colonnes à supprimer :", 
            options=colonnes, 
            default=['Case ID', 'Date_sinistre', 'Date_souscription_contrat', 'Code_Postal', 
                    'Code_Departement', 'Nom_Departement', 'Code_Region', 'Nom_Region']
        )
        if not colomn_to_delete:
            st.error("Veuillez sélectionner au moins une colonne à supprimer.")

        else:
            st.session_state['colomn_to_delete'] = colomn_to_delete

        if st.button("Supprimer les colonnes sélectionnées"):
            # Supprimer les colonnes sélectionnées par l'utilisateur
            df_graphiques = df.drop(columns=colomn_to_delete)
            st.session_state['colomn_to_delete'] = colomn_to_delete
            st.session_state['df_graphiques'] = df_graphiques
            
            # Afficher le DataFrame résultant après suppression
            st.write("### Données après suppression des colonnes sélectionnées :")
            st.write(df_graphiques)
        #----------------------------------------------

        st.write("")
        st.write("#### Graphique de la répartition des pourcentages dans la colonne 'Decision_Finale'")

        if 'df_graphiques' not in st.session_state or st.session_state['df_graphiques'] is None:
            st.error("Aucun DataFrame n'a été chargé car aucune colonnes selectionnes n'a été supprimer.")
        else:
            df_graphiques = st.session_state['df_graphiques']
            col5, col6 = st.columns(2)
            with col5:
                # Calcul de la répartition des pourcentages dans la colonne 'Decision_Finale'
                decision_counts = df_graphiques['Decision_Finale'].value_counts(normalize=True) * 100

                # Utilisation de couleurs personnalisées : rouge pour 'frauduleux', vert pour 'non frauduleux'
                colors = ['#FF0000' if label == 'Fraude' else '#1E90FF' for label in decision_counts.index]

                # Tracer un graphique en camembert (pie chart) avec Matplotlib
                fig, ax = plt.subplots(figsize=(6, 6))
                
                wedges, texts, autotexts = ax.pie(
                    decision_counts, 
                    labels=decision_counts.index, 
                    autopct='%1.1f%%', 
                    colors=colors, 
                    startangle=90, 
                    wedgeprops={'edgecolor': 'black'}, 
                    pctdistance=1.2,  # Positionnement des pourcentages à l'extérieur
                    labeldistance=1.4  # Position des labels plus à l'extérieur
                )

                # Ajout d'un cercle au centre pour un effet "donut"
                centre_circle = plt.Circle((0, 0), 0.70, fc='white')
                fig.gca().add_artist(centre_circle)

                # Ajustement de la taille et de la couleur du texte des pourcentages
                for text in autotexts:
                    text.set_color('black')
                    text.set_fontsize(15)  # Taille du texte des pourcentages

                # Ajustement de la taille des étiquettes
                for text in texts:
                    text.set_fontsize(16)  # Taille des labels

                ax.set_title('Répartition des pourcentages dans la colonne Decision_Finale', fontsize=18)
                ax.legend(wedges, decision_counts.index,
                        title="Décisions",
                        loc="center left",
                        bbox_to_anchor=(1, 0, 0.5, 1))

                st.pyplot(fig)
            with col6:
                pass
        #----------------------------------------------
        st.write("")
        st.write("#### Graphique des fraudes par mois")

        if 'df_graphiques' not in st.session_state or st.session_state['df_graphiques'] is None:
            st.error("Aucun DataFrame n'a été chargé car aucune colonnes selectionnes n'a été supprimer.")

        else:
            df_graphiques = st.session_state['df_graphiques']
            # Définir le nombre de colonnes par ligne
            num_cols = 2
            columns_per_row = st.columns(num_cols)

            # -- Ajout du graphique pour les fraudes par mois --
            if 'Date_fraude_remonte' in df_graphiques.columns:
                df_graph_fraude_per_date = df_graphiques.copy()
                df_graphiques['Date_fraude_remonte'] = pd.to_datetime(df_graph_fraude_per_date['Date_fraude_remonte'], format='%d/%m/%Y', errors='coerce')
                df_graph_fraude_per_date['Annee'] = pd.to_datetime(df_graph_fraude_per_date['Date_fraude_remonte'], format='%d/%m/%Y').dt.year

                # Filtrer uniquement les "frauduleux" dans la colonne 'Decision_Finale'
                df_fraude = df_graph_fraude_per_date[df_graph_fraude_per_date['Decision_Finale'] == 'frauduleux']

                # Convertir la colonne 'année' en entier pour la sélection
                df_fraude['Annee'] = df_graph_fraude_per_date['Annee'].astype(int)
                annees_disponibles = df_graph_fraude_per_date['Annee'].dropna().unique().tolist()
                # trie les années disponibles
                annees_disponibles = sorted(annees_disponibles)
                annee_choisie = st.selectbox("Choisissez une année à observer :",\
                        options=sorted(annees_disponibles))

                # Filtrer les fraudes pour l'année choisie
                df_fraude_annee = df_fraude[df_fraude['Annee'] == annee_choisie]

                # Conversion de 'date_fraude_remonte' en datetime pour extraire les mois
                df_fraude_annee['Mois'] = pd.to_datetime(df_graph_fraude_per_date['Date_fraude_remonte'], format='%d/%m/%Y').dt.month
                fraudes_par_mois = df_fraude_annee.groupby('Mois').size()

                # Créer un graphique des fraudes par mois
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.barplot(x=fraudes_par_mois.index, y=fraudes_par_mois.values, palette='viridis', ax=ax, legend=False, hue=fraudes_par_mois.index)
                ax.set_title(f"Nombre de fraudes remontées par mois en {annee_choisie}")
                ax.set_xlabel("Mois")
                ax.set_ylabel("Nombre de fraudes")
                ax.set_xticks(range(1, 13))  # Mois de 1 à 12
                ax.set_xticklabels(['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])

                st.pyplot(fig)

            else:
                st.warning("La colonne 'Date_fraude_remonte' n'est pas présente dans le DataFrame.")
        
        #----------------------------------------------
        st.write("")
        st.write("#### Graphique valeurs totales pour les colonnes précédentes")

        if 'df_graphiques' not in st.session_state or st.session_state['df_graphiques'] is None:
            st.error("Aucun DataFrame n'a été chargé car aucune colonnes selectionnes n'a été supprimer.")
        else:
            df_graphiques = st.session_state['df_graphiques']
            colonnes_histo = st.multiselect(
                "Choisissez les colonnes pour afficher des graphiques :",
                options=df_graphiques.columns.tolist(), 
                default=['Type_Fraude','Incohérences_Déclarations','Type_Client']
            )
            #if st.button("Afficher les histogrammes des colonnes sélectionnées"):
            # Nombre de colonnes par ligne pour les graphiques
            num_cols = 2
            columns_per_row = st.columns(num_cols)
            
            for idx, col in enumerate(colonnes_histo):
                # Chaque graphique est placé dans une colonne différente
                with columns_per_row[idx % num_cols]:
                    # Si la colonne est catégorielle (de type object)
                    if df_graphiques[col].dtype == 'object':
                        fig, ax = plt.subplots(figsize=(6, 4))
                        sns.countplot(y=col, data=df_graphiques, palette="Set2", ax=ax)
                        ax.set_title(f"Répartition des valeurs dans {col}")
                        ax.set_ylabel(col)
                        st.pyplot(fig)
                    
                    # Si la colonne est numérique
                    elif pd.api.types.is_numeric_dtype(df_graphiques[col]):
                        fig, ax = plt.subplots(figsize=(6, 4))
                        sns.histplot(df_graphiques[col], bins=20, kde=True, color="blue", ax=ax)
                        ax.set_title(f"Histogramme de {col}")
                        ax.set_xlabel(col)
                        st.pyplot(fig)
                
                # Réinitialiser les colonnes lorsque l'on atteint la limite définie par num_cols
                if (idx + 1) % num_cols == 0:
                    columns_per_row = st.columns(num_cols)
    
        #----------------------------------------------
        st.write("")
        st.write("#### Graphiques piechart pour les colonnes sélectionnées")

        if 'df_graphiques' not in st.session_state or st.session_state['df_graphiques'] is None:
            st.error("Aucun DataFrame n'a été chargé car aucune colonnes selectionnes n'a été supprimer.")
        else:
            df_graphiques = st.session_state['df_graphiques']
            colonnes_piechart = st.multiselect(
                "Choisissez les colonnes à séléectionner :", 
                options=df_graphiques.columns.tolist(), 
                default=['Type_Fraude','Incohérences_Déclarations','Type_Client', 'Statut_Familial', 'Canal_Communication_Prefere', 'Risque_Geographique']
            )
            #if st.button("Afficher les piechart des colonnes sélectionnées"):
            # Définir le nombre de colonn|es par ligne
            num_cols_pie = 3

            # Sélectionner les colonnes catégorielles
            df_cat = df_graphiques.select_dtypes(include=['object'])
            columns_per_row_pie= st.columns(num_cols_pie)

            # Afficher les graphiques piechart pour chaque colonne sélectionnée
            for idx, column in enumerate(colonnes_piechart):
                # Sélectionner la colonne correspondante
                with columns_per_row_pie[idx % num_cols_pie]:
                    # Fixer la taille du graphique pour garantir l'uniformité (par exemple, 6x6)
                    fig, ax = plt.subplots(figsize=(8, 8))
                    df_cat[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
                    ax.set_ylabel('')
                    ax.set_title(f'Distribution de {column}')
                    st.pyplot(fig)

                # Réinitialiser les colonnes lorsque l'on atteint la limite définie par num_cols
                if (idx + 1) % num_cols_pie == 0:
                    columns_per_row_pie = st.columns(num_cols_pie)
        
        #----------------------------------------------
        st.write("")
        st.write("#### Graphique de l'évolution du montant final recouvré")

        if 'df_graphiques' not in st.session_state or st.session_state['df_graphiques'] is None:
            st.error("Aucun DataFrame n'a été chargé car aucune colonnes selectionnes n'a été supprimer.")
        else:
            df_graphiques = st.session_state['df_graphiques']

            # Vérification si la colonne 'Date_fraude_remonte' est présente
            if 'Date_fraude_remonte' in df_graphiques.columns:
                df_graphiques['Date_fraude_remonte'] = pd.to_datetime(df_graphiques['Date_fraude_remonte'], format='%d/%m/%Y', errors='coerce')
                df_graphiques['Annee'] = df_graphiques['Date_fraude_remonte'].dt.year
                df_graphiques['Mois'] = df_graphiques['Date_fraude_remonte'].dt.month

                # Récupération des années disponibles dans les données
                annees_disponibles = df_graphiques['Annee'].dropna().unique().tolist()
                annees_disponibles = sorted(annees_disponibles)

                # Sélection de l'année par l'utilisateur
                annee_choisie = st.selectbox("Choisissez une année :", options=annees_disponibles)

                # Filtrer les données pour l'année sélectionnée et l'année précédente
                df_annee_choisie = df_graphiques[df_graphiques['Annee'] == annee_choisie]
                df_annee_precedente = df_graphiques[df_graphiques['Annee'] == (annee_choisie - 1)]

                # Concatenation des données pour l'année choisie et l'année précédente
                df_concat = pd.concat([df_annee_precedente, df_annee_choisie])

                # Grouper les données par mois et année et calculer la somme du 'Montant_Final_Recouvre'
                montant_mensuel = df_concat.groupby(['Annee', 'Mois'])['Montant_Final_Recouvre'].sum().reset_index()

                # Création du graphique
                fig, ax = plt.subplots(figsize=(10, 6))
                
                # Tracé pour l'année précédente
                sns.lineplot(
                    data=montant_mensuel[montant_mensuel['Annee'] == (annee_choisie - 1)],
                    x='Mois', y='Montant_Final_Recouvre', marker='o', label=f"Année {annee_choisie - 1}",
                    color="blue", ax=ax
                )
        
                # Tracé pour l'année sélectionnée
                sns.lineplot(
                    data=montant_mensuel[montant_mensuel['Annee'] == annee_choisie],
                    x='Mois', y='Montant_Final_Recouvre', marker='o', label=f"Année {annee_choisie}",
                    color="green", ax=ax
                )

                # Ajustements des labels et titre du graphique
                ax.set_title(f"Évolution du Montant Final Recouvré - Année {annee_choisie} et {annee_choisie - 1}", fontsize=16)
                ax.set_xlabel("Mois", fontsize=12)
                ax.set_ylabel("Montant Final Recouvré", fontsize=12)
                ax.set_xticks(range(1, 13))
                ax.set_xticklabels(['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])
                ax.legend(title="Année")

                # Affichage du graphique
                st.pyplot(fig)

            else:
                st.warning("La colonne 'Date_fraude_remonte' n'est pas présente dans le DataFrame.")

        #----------------------------------------------
        # see: afficher France avec densité de fraude

    else:
        st.warning("Veuillez sélectionner au moins une colonne pour afficher les graphiques.")

else:
    st.error("Aucun fichier ou base de données n'a été chargé. Veuillez charger les données sur la page '💼 New Data'.")    