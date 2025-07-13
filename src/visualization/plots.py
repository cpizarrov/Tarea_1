import os
import matplotlib.pyplot as plt

def plot_f1score(df, save_dir="plots", filename="f1_score_por_mes.png"):
    os.makedirs(save_dir, exist_ok=True)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df["mes"], df["f1_score"], marker='o')
    plt.title("F1-Score por mes")
    plt.xlabel("Mes")
    plt.ylabel("F1-Score")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    
    save_path = os.path.join(save_dir, filename)
    plt.savefig(save_path)
    print(f"Gráfico guardado en {save_path}")
    plt.show()

def plot_casos(df, save_dir="plots", filename="casos_por_mes.png"):
    os.makedirs(save_dir, exist_ok=True)
    
    plt.figure(figsize=(10, 5))
    plt.bar(df["mes"], df["n_casos"])
    plt.title("Cantidad de casos por mes")
    plt.xlabel("Mes")
    plt.ylabel("Volumen de casos")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    save_path = os.path.join(save_dir, filename)
    plt.savefig(save_path)
    print(f"Gráfico guardado en {save_path}")
    plt.show()