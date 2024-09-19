# Importation des modules
import streamlit as st
# pip install st-annotated-text
from annotated_text import annotated_text


# Configuration de la page
st.set_page_config(page_title="ClearFraudExpert - Logout", page_icon="🔐")

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
    <div class="small-text"> 🔐 Logout</div>
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