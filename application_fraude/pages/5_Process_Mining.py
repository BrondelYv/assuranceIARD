import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from streamlit_elements import elements, mui, html

# Configuration de la page
st.set_page_config(page_title="ClearFraudExpert - Process Mining", page_icon="💼",
                   layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

# Barre latérale pour la navigation dans le menu
st.sidebar.title("ClearFraudExpert")
st.sidebar.write("")
menu_option = st.sidebar.radio("Menu", ["Process Mining"])

st.markdown(
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
        font-size: 150px;}
    
    /* Main page background */
    .stApp {
        background-color: #EBF4F7;
    }
    
    /* Style for the main container (white background) */
    .main-container {
        max-width: 1200px;
        background-color: #FFFFFF;
        border-radius: 20px;
        font-family: 'Arial';
        
    }
    
    /* Style for col1 and col2 containers */
    .col-container {
        background-color: #FFFBEC;
        border-radius: 50px;
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


# Titre de la page
st.markdown("#### Processus de réclamation d'assurance")
with st.container(height=570):
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    # Créez deux colonnes pour afficher les contenus côte à côte
    col1, col2 = st.columns(2)

    # Colonne de gauche (Étapes principales du processus)
    with col2.container(height=500):
        #st.markdown("<div class='col-container'>", unsafe_allow_html=True)
        st.markdown("""### Étapes principales du processus""")
           
        st.markdown("""    
                <strong>Enregistrement de la demande (start - register request) :</strong>
                <p>L'utilisateur (représenté par une personne) enregistre une réclamation pour un sinistre, par exemple, une demande de compensation après un accident ou un incendie.</p>
           

           
                <strong>C1 - Examiner de manière occasionnelle (examine casually) :</strong>
                <p>Cette étape représente une vérification initiale légère. Pour un cas normal, cette vérification pourrait se limiter à des contrôles de base sans approfondir la légitimité de la réclamation.</p>
            

           
                <strong>C2 - Examiner en détail (examine thoroughly) :</strong>
                <p>En cas de soupçon de fraude, cette étape pourrait déclencher une enquête approfondie. Les détails de la réclamation sont étudiés minutieusement pour vérifier la véracité des faits.</p>
            

            
                <strong>C3 - Vérification des tickets (check ticket) :</strong>
                <p>Cela peut correspondre à la vérification des preuves ou documents fournis, tels que les reçus de réparation, les rapports de police, etc., pour confirmer que les informations sont cohérentes et valides.</p>
            

            
                <strong>C4 - Réinitiation de la demande (reinitiate request) :</strong>
                <p>Si des incohérences ou des problèmes sont détectés lors des vérifications, il peut être nécessaire de réitérer la demande. Cela pourrait être une étape où l'assureur demande des clarifications ou des informations supplémentaires.</p>
           

            
                <strong>C5 - Prendre une décision (decide) :</strong>
                <p>Cette étape correspond à la décision finale de l'assureur. Soit la demande est acceptée, soit elle est rejetée, en fonction de la validité des informations et des suspicions de fraude.</p>
            

            
                <strong>Fin du processus :</strong>
                <p>Si la décision est favorable : Paiement de l'indemnité (pay compensation) : L'assureur accepte de payer la réclamation.</p>
                <p>Si la décision est défavorable : Rejet de la demande (reject request) : La réclamation est refusée, souvent en raison de preuves de fraude ou d'incohérences dans les informations fournies.</p>
            
            
        """, unsafe_allow_html=True)

    # Colonne de droite (Modèle de Process Mining)

    with col1.container(height=500):
        st.markdown( """### Modèle de Process Mining""")
        # Créeon un jeu de données d'événements dans un DataFrame (modèle simplifié)
        data = {
            'Caseid': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6],
            'Eventid': [35654423, 35654424, 35654425, 35654426, 35654427, 35654483, 35654485, 35654487, 35654488, 35654489, 
                        35654521, 35654522, 35654524, 35654525, 35654526, 35654527, 35654530, 35654531, 35654641, 35654643, 
                        35654644, 35654645, 35654711, 35654712, 35654714, 35654715, 35654716, 35654718, 35654719, 35654720, 
                        35654721, 35654871, 35654873, 35654874, 35654875, 35654877],
            'Timestamp': ['30-12-2010:11.02', '31-12-2010:10.06', '05-01-2011:15.12', '06-01-2011:11.18', '07-01-2011:14.24',
                        '30-12-2010:11.32', '30-12-2010:12.12', '30-12-2010:14.16', '05-01-2011:11.22', '08-01-2011:12.05',
                        '30-12-2010:14.32', '30-12-2010:15.06', '30-12-2010:16.34', '06-01-2011:09.18', '06-01-2011:12.18',
                        '06-01-2011:13.06', '08-01-2011:11.43', '09-01-2011:09.55', '06-01-2011:15.02', '07-01-2011:12.06',
                        '08-01-2011:14.43', '09-01-2011:12.02', '06-01-2011:09.02', '07-01-2011:10.16', '08-01-2011:11.22',
                        '10-01-2011:13.28', '11-01-2011:16.18', '14-01-2011:14.33', '16-01-2011:15.50', '19-01-2011:11.18',
                        '20-01-2011:12.48', '06-01-2011:15.02', '06-01-2011:16.06', '07-01-2011:16.22', '07-01-2011:16.52', '16-01-2011:11.47'],
            'Activity': ['registerrequest', 'examinethoroughly', 'checkticket', 'decide', 'rejectrequest',
                        'registerrequest', 'checkticket', 'examinecasually', 'decide', 'paycompensation',
                        'registerrequest', 'examinecasually', 'checkticket', 'decide', 'reinitiaterequest', 'examinethoroughly',
                        'checkticket', 'decide', 'registerrequest', 'checkticket', 'examinethoroughly', 'decide',
                        'registerrequest', 'examinecasually', 'checkticket', 'decide', 'reinitiaterequest', 'checkticket',
                        'examinecasually', 'decide', 'reinitiaterequest', 'registerrequest', 'examinecasually', 'checkticket',
                        'decide', 'paycompensation'],
            'Resource': ['Pete', 'Sue', 'Mike', 'Sara', 'Pete', 'Mike', 'Mike', 'Pete', 'Sara', 'Ellen', 'Pete', 'Mike',
                        'Ellen', 'Sara', 'Sara', 'Sean', 'Pete', 'Sara', 'Pete', 'Mike', 'Sean', 'Sara', 'Ellen', 'Mike', 'Pete',
                        'Sara', 'Sara', 'Ellen', 'Mike', 'Sara', 'Sara', 'Mike', 'Ellen', 'Mike', 'Sara', 'Mike']
        }

        df = pd.DataFrame(data)

        # Les rôles et leurs icônes correspondantes
        role_icons = {
            'Assistant': 'D:/assuranceIARD/application_fraude/JOB/pictures/assistante.png',  # Bonhomme vert pour assistant
            'Expert': 'D:/assuranceIARD/application_fraude/JOB/pictures/expert.png',        # Bonhomme bleu pour expert
            'Manager': 'D:/assuranceIARD/application_fraude/JOB/pictures/manager.png'       # Bonhomme rouge pour manager
        }

        # Associons les acteurs avec leurs rôles
        actor_roles = {
            'Pete': 'Assistant',
            'Mike': 'Assistant',
            'Ellen': 'Assistant',
            'Sue': 'Expert',
            'Sean': 'Expert',
            'Sara': 'Manager'
        }

        # Fonction pour ajouter une image au graphe
        def add_image(ax, pos, image_path, zoom=0.1):
            img = plt.imread(image_path)
            imagebox = OffsetImage(img, zoom=zoom)
            ab = AnnotationBbox(imagebox, pos, frameon=False)
            ax.add_artist(ab)

        # Création du graphe
        G = nx.DiGraph()

        # Ajoutons les places (cercles) et transitions (carrés)
        places = ['start', 'c1', 'c2', 'c3', 'c4', 'c5', 'end']
        place_labels = {'start': 'start', 'c1': 'C1', 'c2': 'C2', 'c3': 'C3', 'c4': 'C4', 'c5': 'C5', 'end': 'end'}
        transitions = {
            'a': 'register request', 'b': 'examine thoroughly', 'c': 'examine casually',
            'd': 'check ticket', 'e': 'decide', 'f': 'reinitiate request',
            'g': 'pay compensation', 'h': 'reject request'
        }
        edges = [
            ('start', 'a'), ('a', 'c1'), ('a', 'c2'), ('c1', 'b'), ('c1', 'c'), 
            ('b', 'c3'), ('c', 'c3'), ('c2', 'd'), ('d', 'c4'), ('c4', 'e'), ('c3', 'e'),
            ('e', 'c5'), ('c5', 'g'), ('c5', 'h'), ('f', 'c1'), ('c5', 'f'),
            ('g', 'end'), ('h', 'end')
        ]
        edges_inverse = [('f', 'c5'), ('c1', 'f')]

        # Ajoutons les nœuds et les arêtes dans le graphe
        for place in places:
            G.add_node(place, shape='circle')
        for t in transitions:
            G.add_node(t, shape='square')

        G.add_edges_from(edges)
        G.add_edges_from(edges_inverse)

        # Positionnement des nœuds
        pos = {
            'start': (0, 0), 'a': (2, 0), 'c1': (3, 1), 'c2': (3, -1),
            'b': (4.5, 0.5), 'c': (4.5, 2), 'd': (4.5, -2), 'e': (6, 0),
            'f': (6.5, -2.5), 'c3': (6, 1), 'c4': (6, -1), 'c5': (8, 0),
            'g': (8, 1), 'h': (8, -1), 'end': (10, 0)
        }

        # Taille dynamique des carrés
        def get_node_size(label):
            base_size = 1500
            length = len(label)
            return base_size + (length * 100)

        # Dessin du graphe
        fig, ax = plt.subplots(figsize=(10, 6))
        nx.draw_networkx_nodes(G, pos, nodelist=places, node_shape='o', node_color='lightblue', node_size=2000)
        nx.draw_networkx_labels(G, pos, labels=place_labels, font_size=10)
        nx.draw_networkx_nodes(G, pos, nodelist=transitions.keys(), node_shape='s', node_color='lightgreen', node_size=[get_node_size(transitions[t]) for t in transitions])
        nx.draw_networkx_labels(G, pos, labels=transitions, font_size=10)

        nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=20)
        nx.draw_networkx_edges(G, pos, edgelist=edges_inverse, arrowstyle='<-', arrowsize=20, edge_color='red')

        # Ajoutons les icônes des rôles sur les nœuds où ils apparaissent
        role_positions = {'a': (1, 0), 'b': (3, 0.5), 'e': (5, 0), 'f': (4, -2), 'g': (7, 0.5), 'h': (7, -0.5)}
        role_actors = {'a': 'Pete', 'b': 'Sue', 'e': 'Sara', 'f': 'Sara', 'g': 'Ellen', 'h': 'Mike'}

        # Ajoutons les images au-dessus des nœuds à la place des acteurs
        for node, actor in role_actors.items():
            role = actor_roles[actor]
            icon_path = role_icons[role]
            
            # Position du nœud
            node_x, node_y = pos[node]
            
            # Ajustons la position pour mettre l'image au-dessus du nœud
            image_position = (node_x, node_y + 0.5)  # 0.5 correspond à l'écart entre l'image et le nœud
            
            # Ajoutons l'image au-dessus du nœud
            add_image(ax, image_position, icon_path, zoom=0.1)

        # Affichons le graphe dans l'application Streamlit
        st.pyplot(fig)
     # Fermeture de la balise div pour le conteneur principal
    st.markdown("</div>", unsafe_allow_html=True)
