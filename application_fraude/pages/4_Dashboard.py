# Importation des modules
import streamlit as st
# pip install st-annotated-text
from annotated_text import annotated_text
import streamlit.components.v1 as components
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder,StandardScaler, MinMaxScaler
import joblib
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve, precision_recall_curve, f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from utils import encoder_categoriel, normaliser_colonnes, separate_features_and_target

# Configuration de la page
st.set_page_config(page_title="ClearFraudExpert - Dashboard", page_icon="🖼️")

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
    <div class="small-text"> 🖼️ Dashboard</div>
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
# Charger les données
def load_data():
    try:
        df = pd.read_excel('Fichier_fraude_assurance.xlsx')
        st.session_state.data = {"file_name": 'Fichier_fraude_assurance.xlsx', "data": df}
        return df
    except FileNotFoundError:
        st.error("Pas de fichier trouvé.")
        return None
        

# Si le fichier n'est pas chargé dans session_state, le charger par défaut
if ('data' or 'db_connection') in st.session_state and \
    (st.session_state.data or st.session_state.db_connection)  is not None:
    text_size_title = "30px"
    st.write("")
    if 'data' in st.session_state:
        df = st.session_state.data["data"]
        st.write("")

        if df is not None:
            st.write("#### Informations sur le dataset")

            # Suppression des colonnes
            if 'colonnes_a_supprimer' not in st.session_state:
                st.session_state['colonnes_a_supprimer'] = ['Case ID', 'Date_fraude_remonte', 'Date_sinistre', 'Date_souscription_contrat', 'Code_Postal', 
                    'Code_Departement', 'Nom_Departement', 'Code_Region', 'Nom_Region','Montant_Final_Recouvre','Incohérences_Déclarations']

            colonnes = df.columns.tolist()
                
            colonnes_a_supprimer = st.multiselect("Choisissez les colonnes à supprimer :", options=colonnes, default=st.session_state['colonnes_a_supprimer'])

            # Gestion des erreurs en cas d'absence de sélection de colonnes
            if not colonnes_a_supprimer:
                st.error("Veuillez sélectionner au moins une colonne à supprimer.")
            else:
                st.session_state['colonnes_a_supprimer'] = colonnes_a_supprimer

                if st.button("Supprimer les colonnes sélectionnées"):
                    df_graphiques = df.drop(columns=colonnes_a_supprimer)
                    st.session_state['df_graphiques'] = df_graphiques

                    # Définir les colonnes pour la normalisation et l'encodage, en s'assurant que celles à supprimer sont retirées
                    colonnes_numeriques = ['Montant_reclame_par_client','Montant_Total_Souscrit','Temps_Investigation (jours)']
                    colonnes_numeriques = [col for col in colonnes_numeriques if col not in colonnes_a_supprimer]  # Supprimer les colonnes à supprimer
                    df_normalized = normaliser_colonnes(df_graphiques, colonnes_numeriques, "standard")
                    st.session_state['df_normalized'] = df_normalized

                    colonnes_onehot = ['Canal_Souscription', 'Type_Client', 'Tranche_Age', 'Genre','Statut_Familial','Tranche_nombre_Reclamations',
                                        'Tranche_Revenu_Annuel', 'Tranche_Anciennete','Tranche_nombre_sinistre','Tranche_Nombre_Produits_Souscrits',
                                        'Type_Fraude','Tranche_Delai_entre_Souscription_sinistre','Canal_Communication_Prefere']
                    colonnes_onehot = [col for col in colonnes_onehot if col not in colonnes_a_supprimer]  # Supprimer les colonnes à supprimer
                        
                    colonnes_ordinal = ['Jeune_conducteur','Monorisque','Réclamations_Multiples_Même_Sinistre', 
                                        'Réclamations_Similaires_Réseau','Moyens_Paiement','Participation_Campagnes_Promo','Score_Relation_Client',
                                        'Risque_Geographique']
                    colonnes_ordinal = [col for col in colonnes_ordinal if col not in colonnes_a_supprimer]  # Supprimer les colonnes à supprimer

                    # Appliquer l'encodage après avoir filtré les colonnes à supprimer
                    df_encoded = encoder_categoriel(df_normalized, colonnes_onehot, colonnes_ordinal)
                    st.session_state['df_encoded'] = df_encoded
                    st.write("Colonnes supprimées avec succès.")
                    
            # Charger les données préparées dans st.session_state
            if 'df_encoded' in st.session_state:
                df_encoded = st.session_state['df_encoded']

                # Choisir la colonne cible après encodage
                target_column = 'Decision_Finale'

                # Si une cible est sélectionnée, séparer les données
                if target_column:
                    if 'X_train' not in st.session_state or 'y_train' not in st.session_state:
                        # Séparer les features et la cible à partir du dataframe encodé
                        X, y = separate_features_and_target(df_encoded, target_column)
                        # Remplacer les valeurs 'Fraude' et 'Pas de Fraude' directement dans la série y
                        y = y.replace({'Fraude': 1, 'Pas de Fraude': 0})

                        # Diviser les données en ensemble d'entraînement et de test
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                    
                        # Stocker les résultats dans st.session_state
                        st.session_state['X_train'] = X_train
                        st.session_state['y_train'] = y_train
                        st.session_state['X_test'] = X_test
                        st.session_state['y_test'] = y_test

                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("Features (X) :")
                            st.write(X)
                        with col2:
                            st.write("Cible (y) :")
                            st.write(y)
                    else:
                        X_train = st.session_state['X_train']
                        y_train = st.session_state['y_train']
                        X_test = st.session_state['X_test']
                        y_test = st.session_state['y_test']
            else:
                st.error("Aucune donnée disponible pour l'entraînement. Veuillez vérifier la normalisation et l'encodage.")
                st.stop()
    else:
        st.error("Aucune donnée disponible. Veuillez charger un fichier.")
        st.stop()
else :
    df = load_data()


# S'assurer que les données d'entraînement sont prêtes
if 'X_train' not in st.session_state or 'y_train' not in st.session_state:
    st.error("Données d'entraînement non disponibles.")
else:
    X_train = st.session_state['X_train']
    y_train = st.session_state['y_train']
    
    # Créer un dictionnaire pour stocker les résultats des modèles
    st.session_state['model_results'] = {}

    # Modélisation en backend
    # Random Forest
    base_model = RandomForestClassifier()
    bagging_model_RF = BaggingClassifier(base_model, n_estimators=50, random_state=42)
    bagging_model_RF.fit(X_train, y_train)

    y_pred_rf = bagging_model_RF.predict(X_train)
    accuracy_RF = accuracy_score(y_train, y_pred_rf)
    report_RF = classification_report(y_train, y_pred_rf, output_dict=True)
    joblib.dump(bagging_model_RF, 'RF_model.pkl')

    # Stocker les résultats du Random Forest dans session_state
    st.session_state['model_results']['Random Forest'] = {
        'accuracy': accuracy_RF,
        'classification_report': report_RF
    }

    # XGBoost
    xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    bagging_model_xgboost = BaggingClassifier(estimator=xgb_model, n_estimators=50, random_state=42, n_jobs=-1)
    bagging_model_xgboost.fit(X_train, y_train)

    y_pred_xgb = bagging_model_xgboost.predict(X_train)
    accuracy_XGB = accuracy_score(y_train, y_pred_xgb)
    report_XGB = classification_report(y_train, y_pred_xgb, output_dict=True)
    joblib.dump(bagging_model_xgboost, 'XGBoost_model.pkl')

    # Stocker les résultats du XGBoost dans session_state
    st.session_state['model_results']['XGBoost'] = {
        'accuracy': accuracy_XGB,
        'classification_report': report_XGB
    }

    # MLP
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    mlp_model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
    mlp_model.fit(X_train_scaled, y_train)

    y_pred_mlp = mlp_model.predict(X_train_scaled)
    accuracy_MLP = accuracy_score(y_train, y_pred_mlp)
    report_MLP = classification_report(y_train, y_pred_mlp, output_dict=True)
    joblib.dump(mlp_model, 'MLP_model.pkl')

    # Stocker les résultats du MLP dans session_state
    st.session_state['model_results']['MLP'] = {
        'accuracy': accuracy_MLP,
        'classification_report': report_MLP
    }
    # Optionnel : Afficher un résumé des métriques
    #st.write("### Résultats des modèles :")
    #for model_name, results in st.session_state['model_results'].items():
    #    st.write(f"**{model_name}**")
    #    st.write(f"Précision : {results['accuracy']:.2f}")
    #    st.write(pd.DataFrame(results['classification_report']).transpose())

    # Affichage des résultats finaux (ou message de fin)
    st.success("Modélisation terminée avec succès.")

# S'assurer que les données d'entraînement et de test sont prêtes
# Partie pour afficher les métriques et comparaisons avec les données de test
if 'X_test' not in st.session_state or 'y_test' not in st.session_state:
    st.error("Données de test non disponibles.")
else:
    X_test = st.session_state['X_test']
    y_test = st.session_state['y_test']
    
    # Charger les modèles préalablement entraînés
    model_mlp = joblib.load('MLP_model.pkl')
    model_RF = joblib.load('RF_model.pkl')
    model_Xgboost = joblib.load('XGBoost_model.pkl')

    # Définir une fonction pour afficher les indicateurs de performance (KPI)
    def display_kpis(y_true, y_pred):
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)

    # Fonction d'affichage des résultats des modèles
    def display_model_results(model_name, y_true, y_pred, y_pred_proba=None):
        st.subheader(f"Résultats pour le modèle {model_name}")
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        # Affichage de la précision du modèle
        accuracy = accuracy_score(y_true, y_pred)

        with col1 :
            # Affichage du rapport de classification
            st.text("Rapport de classification:")
            st.text(classification_report(y_true, y_pred))

        with col2 :
            # Affichage de la matrice de confusion
            cm = confusion_matrix(y_true, y_pred)
            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
            ax.set_xlabel('Prédictions')
            ax.set_ylabel('Vérités')
            st.pyplot(fig)
        
        # Courbe ROC et AUC si applicable
        if y_pred_proba is not None:
            fpr, tpr, _ = roc_curve(y_true, y_pred_proba[:, 1])
            auc_score = roc_auc_score(y_true, y_pred_proba[:, 1])
            st.metric(label="Score AUC-ROC", value=f"{auc_score:.2f}")

            with col3 :
                # Tracer la courbe ROC
                fig, ax = plt.subplots()
                ax.plot(fpr, tpr, label=f'ROC curve (AUC = {auc_score:.2f})', color='darkorange')
                ax.plot([0, 1], [0, 1], color='navy', linestyle='--')
                ax.set_xlim([0.0, 1.0])
                ax.set_ylim([0.0, 1.05])
                ax.set_xlabel('Taux de faux positifs')
                ax.set_ylabel('Taux de vrais positifs')
                ax.set_title('Courbe ROC')
                ax.legend(loc="lower right")
                st.pyplot(fig)

            with col4 :
                # Courbe Précision-Rappel
                precision, recall, _ = precision_recall_curve(y_true, y_pred_proba[:, 1])
                fig, ax = plt.subplots()
                ax.plot(recall, precision, color='purple', label='Precision-Recall curve')
                ax.set_xlabel('Rappel')
                ax.set_ylabel('Précision')
                ax.set_title('Courbe Précision-Rappel')
                ax.legend(loc="lower left")
                st.pyplot(fig)

    # Comparaison des scores AUC des différents modèles
    def compare_auc_scores(y_true, proba_rf, proba_mlp, proba_xgb):
        # Calcul des AUC pour chaque modèle
        auc_rf = roc_auc_score(y_true, proba_rf[:, 1])
        auc_mlp = roc_auc_score(y_true, proba_mlp[:, 1])
        auc_xgb = roc_auc_score(y_true, proba_xgb[:, 1])

        # Création du graphique de comparaison des AUC
        auc_scores = {'Random Forest': auc_rf, 'MLP': auc_mlp, 'XGBoost': auc_xgb}
        
        fig, ax = plt.subplots()
        ax.bar(auc_scores.keys(), auc_scores.values(), color=['#FFA07A', '#87CEEB', '#90EE90'])
        ax.set_ylabel('Score AUC')
        ax.set_title('Comparaison des Scores AUC des Modèles')
        st.pyplot(fig)

    # Initialiser les prédictions de probabilités pour chaque modèle
    y_pred_proba_rf = None
    y_pred_proba_mlp = None
    y_pred_proba_xgb = None

   
    # Sélectionner un modèle avec un selectbox
    model_choice = st.selectbox("Choisissez le modèle à afficher :", ['Random Forest', 'MLP', 'XGBoost'])
    y_pred_rf = model_RF.predict(X_test)
    y_pred_proba_rf = model_RF.predict_proba(X_test)
    y_pred_mlp = model_mlp.predict(X_test)
    y_pred_proba_mlp = model_mlp.predict_proba(X_test)
    y_pred_xgb = model_Xgboost.predict(X_test)
    y_pred_proba_xgb = model_Xgboost.predict_proba(X_test)

    # Afficher les résultats pour le modèle choisi
    if model_choice == 'Random Forest':
        display_model_results('Random Forest', y_test, y_pred_rf, y_pred_proba_rf)
        #display_kpis(y_test, y_pred_rf)

    elif model_choice == 'MLP':
        display_model_results('MLP', y_test, y_pred_mlp, y_pred_proba_mlp)
        #display_kpis(y_test, y_pred_mlp)

    elif model_choice == 'XGBoost':
        display_model_results('XGBoost', y_test, y_pred_xgb, y_pred_proba_xgb)
        #display_kpis(y_test, y_pred_xgb)


    # Comparaison des scores AUC
    if y_pred_proba_rf is not None and y_pred_proba_mlp is not None and y_pred_proba_xgb is not None:
        st.markdown("### Comparaison des scores AUC des modèles")
        compare_auc_scores(y_test, y_pred_proba_rf, y_pred_proba_mlp, y_pred_proba_xgb)
        # Sélection du meilleur modèle en fonction de la précision

        # Stocker les résultats du Random Forest dans session_state
    st.session_state['model_results']['Random Forest'] = {
        'accuracy': accuracy_RF,
        'classification_report': report_RF,
        'model': bagging_model_RF  # Stocker le modèle
    }
        # Stocker les résultats du XGBoost dans session_state
    st.session_state['model_results']['XGBoost'] = {
        'accuracy': accuracy_XGB,
        'classification_report': report_XGB,
        'model': bagging_model_xgboost  # Stocker le modèle
    }

    # Stocker les résultats du MLP dans session_state
    st.session_state['model_results']['MLP'] = {
        'accuracy': accuracy_MLP,
        'classification_report': report_MLP,
        'model': mlp_model  # Stocker le modèle
    }

    accuracies = {
        'Random Forest': accuracy_RF,
        'XGBoost': accuracy_XGB,
        'MLP': accuracy_MLP
    }

    best_model_name = max(accuracies, key=accuracies.get)  # Modèle avec la meilleure précision
    best_model = st.session_state['model_results'][best_model_name]['model']

    # Stocker le meilleur modèle dans session_state
    st.session_state['best_model'] = best_model

    # Affichage des résultats
    st.write("### Meilleur modèle sélectionné :")
    st.write(f"Modèle : {best_model_name} avec une précision de {accuracies[best_model_name]:.2f}")


    # Créer un bouton pour télécharger les résultats des prédictions
    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    # Créer un DataFrame des prédictions
    results_df = pd.DataFrame({
        'Actual': y_test,
        'Random_Forest_Pred': y_pred_rf,
        'MLP_Pred': y_pred_mlp,
        'XGBoost_Pred': y_pred_xgb
    })

    # Convertir les résultats en CSV
    csv_results = convert_df_to_csv(results_df)

    # Bouton de téléchargement
    st.download_button(
        label="Télécharger les prédictions en CSV",
        data=csv_results,
        file_name='predictions_results.csv',
        mime='text/csv'
    )