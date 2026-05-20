import sys

# Simulação simples de análise de sentimentos sem dependências externas pesadas para garantir execução imediata
def analyze_sentiment(text):
    positive_words = ['bom', 'ótimo', 'excelente', 'maravilhoso', 'gostei', 'recomendo', 'incrível', 'parabéns']
    negative_words = ['mau', 'péssimo', 'horrível', 'odiei', 'não recomendo', 'lento', 'caro', 'defeito']
    
    text = text.lower()
    score = 0
    
    for word in positive_words:
        if word in text:
            score += 1
    for word in negative_words:
        if word in text:
            score -= 1
            
    if score > 0:
        return "Positivo"
    elif score < 0:
        return "Negativo"
    else:
        return "Neutro"

def main():
    feedbacks = [
        "O produto é excelente e chegou muito rápido!",
        "Péssimo atendimento, não recomendo a ninguém.",
        "O preço é justo, mas a entrega demorou um pouco.",
        "Simplesmente maravilhoso, superou as expectativas.",
        "O produto veio com defeito e o suporte é lento."
    ]
    
    print("--- Relatório de Análise de Sentimentos ---")
    for fb in feedbacks:
        sentiment = analyze_sentiment(fb)
        print(f"Feedback: {fb}")
        print(f"Sentimento: {sentiment}")
        print("-" * 20)

if __name__ == "__main__":
    main()
