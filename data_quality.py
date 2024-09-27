import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataQuality:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa o módulo de qualidade de dados com o DataFrame.
        """
        self.df = df
    
    def count_missing(self):
        """
        Conta os valores nulos de cada coluna do DataFrame.
        """
        missing_counts = self.df.isnull().sum()
        print("Contagem de valores nulos por coluna:")
        print(missing_counts)
        return missing_counts
    
    def count_unique(self):
        """
        Conta os valores únicos de cada coluna do DataFrame.
        """
        unique_counts = self.df.nunique()
        print("Contagem de valores únicos por coluna:")
        print(unique_counts)
        return unique_counts
    
    def value_counts_categorical(self):
        """
        Exibe a contagem de valores para cada coluna categórica do DataFrame.
        """
        categorical_columns = self.df.select_dtypes(include='object').columns
        for col in categorical_columns:
            print(f"\nContagem de valores para {col}:")
            print(self.df[col].value_counts())
    
    def describe_numeric(self):
        """
        Exibe a descrição estatística das colunas numéricas.
        """
        print("Descrição estatística das colunas numéricas:")
        print(self.df.describe())
    
    def plot_categorical_distribution(self):
        """
        Gera gráficos de barra para a distribuição das colunas categóricas.
        """
        categorical_columns = self.df.select_dtypes(include='object').columns
        for col in categorical_columns:
            plt.figure(figsize=(10, 5)) # (largura, altura) 
            sns.countplot(y=self.df[col])
            plt.title(f"Distribuição de {col}")
            plt.xticks(rotation=45)
            plt.show()
    
    def plot_numeric_distribution(self):
        """
        Gera gráficos de histograma para a distribuição das colunas numéricas.
        """
        numeric_columns = self.df.select_dtypes(include=['int64', 'float64']).columns
        for col in numeric_columns:
            plt.figure(figsize=(10, 5))
            sns.histplot(self.df[col], kde=True)
            plt.title(f"Distribuição de {col}")
            plt.show()

            
    
    def generate_report(self):
        """
        Gera um relatório completo de qualidade de dados, incluindo contagens, descrição e gráficos.
        """
        print("=== Relatório de Qualidade de Dados ===\n")
        self.count_missing()
        print("\n---------------------------------\n")
        self.count_unique()
        print("\n---------------------------------\n")
        self.value_counts_categorical()
        print("\n---------------------------------\n")
        self.describe_numeric()
        print("\n---------------------------------\n")
        print("Gerando gráficos de distribuição...")
        self.plot_categorical_distribution()
        self.plot_numeric_distribution()
        print("\n=== Fim do Relatório ===")