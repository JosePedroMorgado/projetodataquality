import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataQuality:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe DataQuality com um DataFrame.
        
        :param df: DataFrame do pandas a ser analisado
        """
        self.df = df
    
    def generate_report(self):
        """
        Gera um relatório completo de qualidade de dados, retornando uma string com formato vertical.
        
        :return: String contendo o relatório completo
        """
        # Lista para armazenar todas as linhas do relatório
        report = []
        
        # Título do relatório
        report.append("=== Relatório de Qualidade de Dados ===\n")
        
        # 1. Contagem de valores ausentes
        report.append("1. Contagem de valores ausentes:")
        for col, count in self.df.isnull().sum().items():
            report.append(f"{col}: {count}")
        report.append("")
        
        # 2. Contagem de valores únicos
        report.append("2. Contagem de valores únicos:")
        for col, count in self.df.nunique().items():
            report.append(f"{col}: {count}")
        report.append("")
        
        # 3. Contagem de valores de texto únicos
        report.append("3. Contagem de valores de texto únicos:")
        # Seleciona apenas as colunas do tipo objeto (geralmente texto)
        text_columns = self.df.select_dtypes(include=['object']).columns
        for col in text_columns:
            report.append(f"{col}: {self.df[col].nunique()}")
        report.append("")
        
        # 4. Contagem de valores float únicos
        report.append("4. Contagem de valores float únicos:")
        # Seleciona apenas as colunas do tipo float64
        float_columns = self.df.select_dtypes(include=['float64']).columns
        for col in float_columns:
            report.append(f"{col}: {self.df[col].nunique()}")
        report.append("")
        
        # 5. Contagem de valores inteiros únicos
        report.append("5. Contagem de valores inteiros únicos:")
        # Seleciona apenas as colunas do tipo int64
        int_columns = self.df.select_dtypes(include=['int64']).columns
        for col in int_columns:
            report.append(f"{col}: {self.df[col].nunique()}")
        report.append("")
        
        # 6. Contagem de valores para colunas categóricas
        report.append("6. Contagem de valores para colunas categóricas:")
        for col in text_columns:
            report.append(f"\nContagem de valores para {col}:")
            # Obtém a contagem de cada valor único na coluna
            value_counts = self.df[col].value_counts()
            for value, count in value_counts.items():
                report.append(f"  {value}: {count}")
        report.append("")
        
        # 7. Descrição estatística das colunas numéricas
        report.append("7. Descrição estatística das colunas numéricas:")
        # Obtém estatísticas descritivas para colunas numéricas
        desc = self.df.describe()
        for col in desc.columns:
            report.append(f"\nEstatísticas para {col}:")
            for stat, value in desc[col].items():
                # Formata o valor para duas casas decimais
                report.append(f"  {stat}: {value:.2f}")
        
        # Junta todas as linhas do relatório em uma única string
        return "\n".join(report)
