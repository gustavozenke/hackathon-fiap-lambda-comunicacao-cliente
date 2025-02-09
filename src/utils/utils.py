def inserir_prefixo_codigo_pais(numero: str) -> str:
    if not numero.startswith("+") or len(numero) < 4:
        raise ValueError("Número de telefone inválido")
    return numero.replace("+", "+55", 1)
