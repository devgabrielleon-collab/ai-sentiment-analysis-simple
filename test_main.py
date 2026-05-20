from main import analyze_sentiment


def test_positive_sentiment():
    assert analyze_sentiment("O produto é excelente") == "Positivo"


def test_negative_sentiment():
    assert analyze_sentiment("Péssimo atendimento") == "Negativo"


def test_neutral_sentiment():
    assert analyze_sentiment("O preço é justo") == "Neutro"
