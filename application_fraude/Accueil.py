# Importation des modules
import streamlit as st
# pip install st-annotated-text
from annotated_text import annotated_text

import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd


# Configuration de la page
st.set_page_config(page_title="ClearFraudExpert - Accueil", page_icon="🏠")

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
    <div class="small-text"> 🏠 Accueil</div>
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

st.write("")


# Chargement des données
df = pd.read_excel('D:/assuranceIARD/IN/Fichier_fraude_assurance.xlsx')
try:
    df = pd.read_excel('D:/assuranceIARD/IN/Fichier_fraude_assurance.xlsx')
except FileNotFoundError:
    st.error("Le fichier 'Fichier_fraude_assurance.xlsx' est introuvable. Veuillez vérifier le chemin ou le nom du fichier.")

# Filtrons les colonnes pertinentes pour notre analyse
df_accueil = df[['Case ID', 'Date_sinistre', 'Decision_Finale', 'Montant_reclame_par_client']]

# Convertissons les dates au format datetime
df_accueil['Date_sinistre'] = pd.to_datetime(df_accueil['Date_sinistre'], format='%d/%m/%Y')

# Extraction de l'année et le mois pour la sélection
df_accueil['YearMonth'] = df_accueil['Date_sinistre'].dt.to_period('M')

# Barre latérale pour la navigation dans le menu
st.sidebar.title("ClearFraudExpert")
st.sidebar.write("")
menu_option = st.sidebar.radio("Menu", ["Accueil"])


# Fonction permettant d'afficher l'analyse des tendances
def analyse_tendances():
    # Appliquons un style CSS pour la mise en page avec les conteneurs
    st.markdown("""
        <style>
        .description-container {
            float: right;
            width: 100%;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            font-family: 'Arial';
        }
        .description-title {
            font-size: 24px;
            font-weight: bold;
            color: #4C566A;
            margin-bottom: 10px;
        }
        .description-content {
            font-size: 16px;
            color: #434C5E;
            line-height: 1.5;
        }
        .metric-container {
            float: left;
            width: 38%;
            padding: 20px;
            background-color: #F5F5F5;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .graph-container {
            clear: both;
            padding: 20px;
            background-color: #FFFFFF;
            border-radius: 10px;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Soit un conteneur principal pour la description et l'analyse des tendances
    st.markdown("<div style='display: flex; justify-content: space-between;'>", unsafe_allow_html=True)

    # Conteneur de description
    st.title("Bienvenue sur ClearFraudExpert")
    st.subheader("Analyse des sinistres et des fraudes en assurance")
    st.markdown("""
        **ClearFraudExpert** est un système intelligent de détection de la fraude, conçu pour vous aider à identifier et prévenir les sinistres frauduleux dans le domaine de l'assurance IARD.

        - Visualisez des analyses détaillées des réclamations et des sinistres.
        - Obtenez des informations sur les membres et leurs réclamations.
        - Identifiez rapidement les comportements suspects grâce à des graphiques et des analyses claires.
        - Comparez les performances des périodes et optimisez la gestion des sinistres.
    """)
    st.subheader("Description de notre SI")
    st.markdown("""
        <div class="description-content">
        Notre solution de détection de fraude par apprentissage automatique vous permet d'analyser rapidement et efficacement les sinistres et réclamations suspectes. 
        Grâce à une interface intuitive et des outils analytiques puissants, vous pouvez identifier les comportements frauduleux potentiels, visualiser des statistiques clés 
        et prendre des décisions éclairées.
        
        * Importez vos nouvelles données pour les analyser.
        * Obtenez des analyses descriptives des données de sinistres, des fraudes et des pertes financières.
        * Accédez à une vue détaillée des graphiques explicatifs des sinistres et des fraudes.
        * Visualisez un résumé des cas de fraude détectés par l'application.
        * Recherchez des clients spécifiques et examinez les détails de leurs sinistres.
        * Suivez les alertes de fraudes générées en fonction des règles métier.
        * Comparez les résultats prédictifs du modèle avec ceux des experts métiers.
        Si vous le souhaitez, téléchargez les résultats et rapports en différents formats.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Conteneur des métriques et de l'analyse
    st.subheader("Analyse tendances")
    selected_month = st.selectbox(
        "Sélectionnez un mois :",
        pd.date_range(start='2015-01', end='2018-12', freq='M').strftime('%Y-%m').tolist()
    )

    # Filtrons les données pour le mois sélectionné
    filtered_data = df_accueil[df_accueil['YearMonth'] == pd.to_datetime(selected_month).to_period('M')]

    # Agrégeons les données pour le mois sélectionné
    if not filtered_data.empty:
        aggregated_data = filtered_data.groupby('YearMonth').agg(
            Pertes=('Montant_reclame_par_client', 'sum'),
            Membres=('Case ID', 'nunique'),
            Fraude=('Decision_Finale', lambda x: (x == "Fraude").sum())
        ).reset_index()

        # Extraction des valeurs agrégées
        total_pertes = aggregated_data['Pertes'].iloc[0]
        total_membres = aggregated_data['Membres'].iloc[0]
        total_fraude = aggregated_data['Fraude'].iloc[0]
        pourcentage_fraude = (total_fraude / total_membres) * 100 if total_membres > 0 else 0

        # Comparaison avec le mois précédent pour comprendre les tendances
        previous_month = (pd.to_datetime(selected_month) - pd.DateOffset(months=1)).to_period('M')
        previous_data = df_accueil[df_accueil['YearMonth'] == previous_month]
        previous_aggregated_data = previous_data.groupby('YearMonth').agg(
            Pertes=('Montant_reclame_par_client', 'sum'),
            Membres=('Case ID', 'nunique'),
            Fraude=('Decision_Finale', lambda x: (x == "Fraude").sum())
        ).reset_index()

        if not previous_aggregated_data.empty:
            pertes_precedent = previous_aggregated_data['Pertes'].iloc[0]
            membres_precedent = previous_aggregated_data['Membres'].iloc[0]
            fraude_precedent = previous_aggregated_data['Fraude'].iloc[0]

            delta_pertes = ((total_pertes - pertes_precedent) / pertes_precedent * 100) if pertes_precedent != 0 else 0
            delta_membres = ((total_membres - membres_precedent) / membres_precedent * 100) if membres_precedent != 0 else 0
            delta_fraude = ((pourcentage_fraude - (fraude_precedent / membres_precedent * 100)) if membres_precedent != 0 else 0)
        else:
            delta_pertes = delta_membres = delta_fraude = 0
    else:
        total_pertes = total_membres = pourcentage_fraude = delta_pertes = delta_membres = delta_fraude = 0
        st.write(f"Aucune information trouvée pour le mois {selected_month}.")

    # Affichage des métriques lié au mois sélectionné
    st.subheader("Métriques par rapport au dernier mois")
    metrics = [
        {"label": "Pertes", "value": f"{total_pertes:.0f} €", "delta": f"{delta_pertes:.2f}% mois dernier"},
        {"label": "Membres", "value": f"{total_membres}", "delta": f"{delta_membres:.2f}% mois dernier"},
        {"label": "Coût de Fraude", "value": f"{pourcentage_fraude:.2f}%", "delta": f"{delta_fraude:.2f}% mois dernier"}
    ]
    cols = st.columns(len(metrics))
    for col, metric in zip(cols, metrics):
        col.metric(label=metric["label"], value=metric["value"], delta=metric["delta"])

    st.markdown("</div>", unsafe_allow_html=True)

    # Fin de la mise en page en flex
    st.markdown("</div>", unsafe_allow_html=True)

    # Graphiques en bas après les autres contenus
    st.subheader("Graphiques cas de fraude")
    #st.write("Cas de fraude")

    # Données pour le graphique en anneau
    fraud_data = filtered_data['Decision_Finale'].value_counts()
    fraud_labels = ['Frauduleux', 'Non Frauduleux']
    fraud_values = [fraud_data.get('Fraude', 0), fraud_data.get('Pas de Fraude', 0)]
    fraud_colors = ['#FF5733', '#33C3F0']

    # Création du graphique en anneau (donut chart)
    fig1 = go.Figure(data=[go.Pie(labels=fraud_labels, values=fraud_values, hole=.5)])

    # Configuration des traces et des couleurs
    fig1.update_traces(
        hoverinfo='label+percent', 
        textinfo='percent', 
        textfont_size=15,
        marker=dict(colors=fraud_colors, line=dict(color='#000000', width=2))
    )

    # Configuration de la disposition du graphique
    fig1.update_layout(
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.2,
            xanchor="center",
            x=0.5
        ),
        margin=dict(t=0, b=0, l=0, r=0),
        annotations=[   
            dict(
                text="Cas de Fraude", 
                x=1, y=1.15,  
                xref="paper", yref="paper",
                showarrow=False
            )
        ]
    )

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig1, use_container_width=True)

    # Graphique des pertes financières
    st.write("Pertes financières")
    weekly_losses = filtered_data.groupby(filtered_data['Date_sinistre'].dt.day_name())['Montant_reclame_par_client'].sum()
    days = weekly_losses.index.tolist()
    losses = weekly_losses.values

    fig2, ax = plt.subplots()
    bars = ax.bar(days, losses, color=['#FF5733', '#FFBD33', '#33FF57','#3357FF', '#FF33A1', '#33FFF5', '#8D33FF'])

    # Ajoutons les étiquettes de données au-dessus des barres
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:0} €', ha='center', va='bottom')

    ax.set_xlabel('Jours')
    ax.set_ylabel('Perte (Euro)')
    ax.set_title("Pertes financières hebdomadaires")

    # Affichons le graphique dans Streamlit
    st.pyplot(fig2)

    st.markdown("</div>", unsafe_allow_html=True)  # Fin du conteneur des graphiques
    
# Choix de la page à afficher
if menu_option == "Accueil":
    analyse_tendances()