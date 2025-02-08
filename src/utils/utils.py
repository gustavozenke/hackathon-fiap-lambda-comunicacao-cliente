def inserir_pais_telefone(numero: str) -> str:
    if not numero.startswith("+") or len(numero) < 4:
        raise ValueError("Número de telefone inválido")
    return numero.replace("+", "+55", 1)
