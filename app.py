import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Analyse interactive de fichier CSV ou Excel")

# Upload du fichier CSV ou Excel
uploaded_file = st.file_uploader("Choisis un fichier CSV ou Excel", type=["csv", "xls", "xlsx"])

if uploaded_file is not None:
    try:
        # Lire selon l'extension
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success(f"Fichier '{uploaded_file.name}' chargé avec succès !")
        
        # Nettoyer noms de colonnes
        df.columns = df.columns.str.strip()
        
        # Affichage aperçu
        st.subheader("Aperçu des données")
        st.dataframe(df.head())
        
        # Conversion des colonnes date si elles existent
        for col in df.columns:
            if "date" in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Statistiques descriptives
        st.subheader("Statistiques descriptives")
        st.dataframe(df.describe(include='all'))
        
        # Sélection colonne pour graphique
        colonne = st.selectbox("Choisis une colonne à visualiser", df.columns)
        
        # Affichage graphique selon type de colonne
        if pd.api.types.is_numeric_dtype(df[colonne]):
            fig = px.histogram(df, x=colonne, nbins=30, title=f"Histogramme de {colonne}")
            st.plotly_chart(fig, key=f"hist_{colonne}")
        elif pd.api.types.is_datetime64_any_dtype(df[colonne]):
            fig = px.histogram(df, x=colonne, title=f"Évolution temporelle de {colonne}")
            st.plotly_chart(fig, key=f"time_{colonne}")
        else:
            fig = px.histogram(df, x=colonne, title=f"Répartition de {colonne}")
            st.plotly_chart(fig, key=f"cat_{colonne}")
        
        # Graphiques pour toutes les colonnes numériques
        st.subheader("Graphiques pour toutes les colonnes numériques")
        numeriques = df.select_dtypes(include='number')
        for i, col in enumerate(numeriques.columns):
            fig = px.histogram(df, x=col, nbins=30, title=f"Histogramme de {col}")
            st.plotly_chart(fig, key=f"hist_all_{i}")
        
    except Exception as e:
        st.error(f"Erreur lors du traitement du fichier : {e}")
else:
    st.info("Charge un fichier CSV ou Excel pour commencer l'analyse.")
