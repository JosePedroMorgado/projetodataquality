import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    def count_text_values(self):
        """
        Conta os valores de texto únicos de cada coluna do DataFrame.
        """
        text_columns = self.df.select_dtypes(include=['object']).columns
        text_counts = {col: self.df[col].nunique() for col in text_columns}
        print("Contagem de valores de texto únicos por coluna:")
        print(pd.Series(text_counts))
        return text_counts
    
    def count_float_values(self):
        """
        Conta os valores float únicos de cada coluna do DataFrame.
        """
        float_columns = self.df.select_dtypes(include=['float64']).columns
        float_counts = {col: self.df[col].nunique() for col in float_columns}
        print("Contagem de valores float únicos por coluna:")
        print(pd.Series(float_counts))
        return float_counts
    
    def count_int_values(self):
        """
        Conta os valores inteiros únicos de cada coluna do DataFrame.
        """
        int_columns = self.df.select_dtypes(include=['int64']).columns
        int_counts = {col: self.df[col].nunique() for col in int_columns}
        print("Contagem de valores inteiros únicos por coluna:")
        print(pd.Series(int_counts))
        return int_counts

    def plot_categorical_distribution(self):
        """
        Gera gráficos de barras para a distribuição de valores em colunas categóricas.
        """
        categorical_columns = self.df.select_dtypes(include='object').columns
        for col in categorical_columns:
            plt.figure(figsize=(10, 5))
            self.df[col].value_counts().plot(kind='bar')
            plt.title(f'Distribuição de valores para {col}')
            plt.xlabel('Valores')
            plt.ylabel('Contagem')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def plot_numeric_distribution(self):
        """
        Gera histogramas para a distribuição de valores em colunas numéricas.
        """
        numeric_columns = self.df.select_dtypes(include=['int64', 'float64']).columns
        for col in numeric_columns:
            plt.figure(figsize=(10, 5))
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Distribuição de valores para {col}')
            plt.xlabel('Valores')
            plt.ylabel('Contagem')
            plt.tight_layout()
            plt.show()

    def generate_report(self):
        """
        Gera um relatório completo de qualidade de dados, retornando uma string.
        """
        report = []
        
        report.append("=== Relatório de Qualidade de Dados ===\n")
        
        report.append("1. Contagem de valores ausentes:")
        report.append(str(self.df.isnull().sum()) + "\n")
        
        report.append("2. Contagem de valores únicos:")
        report.append(str(self.df.nunique()) + "\n")
        
        report.append("3. Contagem de valores de texto únicos:")
        text_columns = self.df.select_dtypes(include=['object']).columns
        text_counts = {col: self.df[col].nunique() for col in text_columns}
        report.append(str(pd.Series(text_counts)) + "\n")
        
        report.append("4. Contagem de valores float únicos:")
        float_columns = self.df.select_dtypes(include=['float64']).columns
        float_counts = {col: self.df[col].nunique() for col in float_columns}
        report.append(str(pd.Series(float_counts)) + "\n")
        
        report.append("5. Contagem de valores inteiros únicos:")
        int_columns = self.df.select_dtypes(include=['int64']).columns
        int_counts = {col: self.df[col].nunique() for col in int_columns}
        report.append(str(pd.Series(int_counts)) + "\n")
        
        report.append("6. Contagem de valores para colunas categóricas:")
        for col in text_columns:
            report.append(f"\nContagem de valores para {col}:")
            report.append(str(self.df[col].value_counts()) + "\n")
        
        report.append("7. Descrição estatística das colunas numéricas:")
        report.append(str(self.df.describe()) + "\n")
        
        return "\n".join(report)
