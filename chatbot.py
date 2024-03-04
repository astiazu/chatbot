import spacy
from spacy.lang.en import English

nlp = spacy.load('en_core_web_sm')

INTENT_KEYWORDS = {
    "greeting": ["hola", "buen dia", "buenas tardes"],
    "farewell": ["Adios", "Que tenga un buen dia", "Nos vemos"],
    "product_inquiry": ["producto", "info", "detalles", "materiales", "reparto", "deposito"],
    "help_order": ["ayuda", "pedido", "remito", "orden", "factura", "problema", "reparto"],
    "thank_you": ["gracias", "agradecido", "te agradezco", "muchas gracias"],
    "complaint": ["queja", "reclamo", "enojo", "insatisfecho", "no llega", "atraso", "demorado", "demora", "lento"],
    "delivery_status": ["entrega", "envio", "estado", "reparto", "bolsas", "hierro", "arena", "ripio", "hormigon", "cemento", "que paso", "tenes"],
    "payment_issues": ["pago", "factura", "problema con el pago", "problema con la fecha", "error en la factura", "error importe"],    
    "unknown": ["null"],
}

RESPONSES = {
    "greeting": "Hola! En que puedo ayudarte?",
    "farewell": "Adios! Si tienes otra consulta, no dudes en preguntar.",
    "help_order": "Parece que necesitas ayuda con un pedido, cuéntame más",
    "thank_you": "No tienes por qué, estoy para ayudarte.",
    "product_inquiry": "Puedo ayudarte con eso, ¿qué producto te interesa?",
    "complaint": "Lamento leer que tengas un inconveniente con eso, cuéntame más para poder ayudarte",
    # "delivery_status": "Para ayudarte con tu pedido, necesito el número de comprobante.",
    "delivery_status": "Si, tenemos ese producto, podes consultar el Precio en nuestra pagina web; tenes alguna otra consulta ?.",
    "payment_issues": "Parece que tienes un problema con el pago, ¿puedes proporcionar algún detalle más?",    
    "unknown": "Perdón, no entiendo tu  consulta, puedes reformularla?",
}

PRODUCT_RESPONSES = {
    "hierro del 8": "Si, tenemos ese producto. comunicate con Luca o visita nuestra pagina para consultar detalles.",
    "cemento": "Seguro, tenemos cemento en stock.",
    "griferia": "Acutalmente no disponemos de estos articulos?",
    "hormigon": "vendemos hormigon por metro cubico, alguna otra pregunta ?",
    "alambres": "Acutalmente no disponemos de estos articulos?",
    # Add more products and responses as needed
}

def get_intent(text):
    print("que viene en text", text)
    doc = nlp(text.lower())
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword in doc.text for keyword in keywords):
            return intent
    # Cambiamos el retorno para que devuelva una "consulta de producto" en lugar de "unknown"
    return "product_inquiry" if any(product in doc.text for product in PRODUCT_RESPONSES) else "unknown"

def get_response(intent, text):
    print(intent, text)
    if intent in RESPONSES:
        return RESPONSES[intent]
    elif text in PRODUCT_RESPONSES:
        return PRODUCT_RESPONSES[text]
    else:
        return RESPONSES["unknown"]

# Ejemplos de uso
user_message = "hola"
intent = get_intent(user_message)
response = get_response(intent, user_message)
print(response)

user_message = "hierro"
intent = get_intent(user_message)
response = get_response(intent, user_message)
print(response)

user_message = "producto"
intent = get_intent(user_message)
response = get_response(intent, user_message)
print(response)

# def get_intent(text):
#     doc = nlp(text.lower())
#     for intent, keywords in INTENT_KEYWORDS.items():
#         if any(keyword in doc.text for keyword in keywords):
#             return intent
#     return "unknown"