from flask import Flask, render_template, request, jsonify
import spacy
from spacy.lang.en import English

app = Flask(__name__)

nlp = spacy.load('en_core_web_sm')

RESPONSE = {
    "greeting": "Hola, en que puedo ayudarte",
    "help_order": "Parece que necesitas ayuda con un pedido, cuéntame más",
    "farewell": "Chau, espero haber ayudado. Saludos",
    "thank_you": "No tienes por qué, estoy para ayudarte.",
    "product_inquiry": "Puedo ayudarte con eso, ¿qué producto te interesa?",
    "complaint": "Lamento leer que tengas un inconveniente con eso, cuéntame más para poder ayudarte",
    "delivery_status": "Para ayudarte con tu pedido, necesito el número de comprobante.",
    "payment_issues": "Parece que tienes un problema con el pago, ¿puedes proporcionar algún detalle más?",
}

PRODUCT_STOCK = {
    "cemento": {"precio": 8000, "stock": True},
    "hormigon": {"precio": 10000, "stock": False},
    "hierro del 4": {"precio": 5000, "stock": True},
    "hierro del 6": {"precio": 6000, "stock": True},
    "hierro del 8": {"precio": 10000, "stock": True},
    "hierro del 10": {"precio": 12000, "stock": False},
    "caños de pvc": {"precio": 2000, "stock": True},
    "accesorios para baño": {"precio": 3000, "stock": True},
    "telgopor": {"precio": 1500, "stock": True},
    "inodoro": {"precio": 8000, "stock": True},
    "bidet": {"precio": 6000, "stock": True},
    "griferia_fv": {"precio": 5000, "stock": False},
}

INTENT_KEYWORDS = {
    "greeting": ["hola", "buenos dias", "buenas tardes", "buenas noches"],
    "help_order": ["ayuda", "pedido", "remito", "orden", "factura", "problema", "reparto"],
    "farewell": ["adios", "hasta luego", "nos vemos", "chau"],
    "thank_you": ["gracias", "agradecido", "te agradezco", "muchas gracias"],
    "product_inquiry": ["productos", "informacion", "detalles", "materiales", "repartos", "domicilios"],
    "complaint": ["queja", "reclamo", "enojo", "insatisfecho", "no llega", "atraso", "demorado", "demora", "lento"],
    "delivery_status": ["entrega", "envio", "estado", "reparto", "bolsas", "hierro", "arena", "ripio", "hormigon", "cemento", "que paso"],
    "payment_issues": ["pago", "factura", "problema con el pago", "problema con la fecha", "error en la factura", "error importe"],
}

def verificar_existencia(producto):
    for key, value in PRODUCT_STOCK.items():
        if key in producto.lower():
            return f"Sí, tenemos {key}. Su precio es ${value['precio']}."
    return f"No reconocemos el producto {producto}."

def get_intent(text):
    doc = nlp(text.lower())
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword in doc.text for keyword in keywords):
            return intent
    return "unknown"

def process_text(text):
    intent = get_intent(text)
    if intent == "product_inquiry":
        words = text.lower().split()
        for product in PRODUCT_STOCK.keys():
            if product in words:
                return verificar_existencia(product)
        return "Lo siento, no tengo información sobre ese producto en este momento."

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import spacy
# from spacy.lang.en import English

# app = Flask(__name__)

# nlp = spacy.load('en_core_web_sm')

# RESPONSE = {
#     "greeting": "Hola, en que puedo ayudarte",
#     "help_order": "Parece que necesitas ayuda con un pedido, cuéntame más",
#     "farewell": "Chau, espero haber ayudado. Saludos",
#     "thank_you": "No tienes por qué, estoy para ayudarte.",
#     "product_inquiry": "Puedo ayudarte con eso, ¿qué producto te interesa?",
#     "complaint": "Lamento leer que tengas un inconveniente con eso, cuéntame más para poder ayudarte",
#     "delivery_status": "Para ayudarte con tu pedido, necesito el número de comprobante.",
#     "payment_issues": "Parece que tienes un problema con el pago, ¿puedes proporcionar algún detalle más?",
# }

# PRODUCT_STOCK = {
#     "cemento": {"precio": 8000, "stock": True},
#     "hormigon": {"precio": 10000, "stock": False},
#     "hierro del 4": {"precio": 5000, "stock": True},
#     "hierro del 6": {"precio": 6000, "stock": True},
#     "hierro del 8": {"precio": 10000, "stock": True},
#     "hierro del 10": {"precio": 12000, "stock": False},
#     "caños de pvc": {"precio": 2000, "stock": True},
#     "accesorios para baño": {"precio": 3000, "stock": True},
#     "telgopor": {"precio": 1500, "stock": True},
#     "inodoro": {"precio": 8000, "stock": True},
#     "bidet": {"precio": 6000, "stock": True},
#     "griferia_fv": {"precio": 5000, "stock": False},
# }

# INTENT_KEYWORDS = {
#     "greeting": ["hola", "buenos dias", "buenas tardes", "buenas noches"],
#     "help_order": ["ayuda", "pedido", "remito", "orden", "factura", "problema", "reparto"],
#     "farewell": ["adios", "hasta luego", "nos vemos", "chau"],
#     "thank_you": ["gracias", "agradecido", "te agradezco", "muchas gracias"],
#     "product_inquiry": ["productos", "informacion", "detalles", "materiales", "repartos", "domicilios"],
#     "complaint": ["queja", "reclamo", "enojo", "insatisfecho", "no llega", "atraso", "demorado", "demora", "lento"],
#     "delivery_status": ["entrega", "envio", "estado", "reparto", "bolsas", "hierro", "arena", "ripio", "hormigon", "cemento", "que paso"],
#     "payment_issues": ["pago", "factura", "problema con el pago", "problema con la fecha", "error en la factura", "error importe"],
# }

# def verificar_existencia(producto):
#     if producto.lower() in PRODUCT_STOCK:
#         if PRODUCT_STOCK[producto.lower()]["stock"]:
#             return f"Sí, tenemos {producto}. Su precio es ${PRODUCT_STOCK[producto.lower()]['precio']}."
#         else:
#             return f"Lo siento, no tenemos {producto} en este momento."
#     else:
#         return f"No reconocemos el producto {producto}."

# def get_intent(text):
#     doc = nlp(text.lower())
#     for intent, keywords in INTENT_KEYWORDS.items():
#         if any(keyword in doc.text for keyword in keywords):
#             return intent
#     return "unknown"

# def process_text(text):
#     intent = get_intent(text)
#     return RESPONSE.get(intent, "Lo siento, no sé cómo responder a eso; ya te paso con Luca")




# import spacy
# from spacy.lang.en import English

# nlp = spacy.load('en_core_web_sm')

# RESPONSE = {
#     "greeting": "Hola, en que puedo ayudarte",
#     "help_order": "Parece que necesitas ayuda con un pedido, cuéntame más",
#     "farewell": "Chau, espero haber ayudado. Saludos",
#     "thank_you": "No tienes por qué, estoy para ayudarte.",
#     "product_inquiry": "Puedo ayudarte con eso, ¿qué producto te interesa?",
#     "complaint": "Lamento leer que tengas un inconveniente con eso, cuéntame más para poder ayudarte",
#     "delivery_status": "Para ayudarte con tu pedido, necesito el número de comprobante.",
#     "payment_issues": "Parece que tienes un problema con el pago, ¿puedes proporcionar algún detalle más?",
# }

# INTENT_KEYWORDS = {
#     "greeting": ["hola", "buenos dias", "buenas tardes", "buenas noches"],
#     "help_order": ["ayuda", "pedido", "remito", "orden", "factura", "problema", "reparto"],
#     "farewell": ["adios", "hasta luego", "nos vemos", "chau"],
#     "thank_you": ["gracias", "agradecido", "te agradezco", "muchas gracias"],
#     "product_inquiry": ["productos", "informacion", "detalles", "materiales", "repartos", "domicilios"],
#     "complaint": ["queja", "reclamo", "enojo", "insatisfecho", "no llega", "atraso", "demorado", "demora", "lento"],
#     "delivery_status": ["entrega", "envio", "estado", "reparto", "bolsas", "hierro", "arena", "ripio", "hormigon", "cemento", "que paso"],
#     "payment_issues": ["pago", "factura", "problema con el pago", "problema con la fecha", "error en la factura", "error importe"],
# }

# def get_intent(text):
#     doc = nlp(text.lower())
#     for intent, keywords in INTENT_KEYWORDS.items():
#         if any(keyword in doc.text for keyword in keywords):
#             return intent
#     return "unknown"

# def process_text(text):
#     intent = get_intent(text)
#     return RESPONSE.get(intent, "Lo siento, no sé cómo responder a eso; ya te paso con Luca")



# import spacy
# import en_core_web_sm

# nlp = spacy.load('en_core_web_sm')

# RESPONSE = {
#     "greeting":"Hola, en que puedo ayudarte",
#     "help_order":"parece que necesitas ayuda con un pedido, contame !",
#     "farewell":"Chau, espero haber ayudado. Saludos",
#     "thank_you":"no tienes por que, estoy para ayudarte.",
#     "product_inquiry":"puedo ayudarte con eso, que producto te interesa ?",
#     "complaint":"Lamento leer que tengas un inconveniente con eso, contame mas para poder ayudarte",
#     "delivery_status":"para poder ayudar con tu pedido, necesito el número de comprobante.",
#     "payment_issues":"parece que tienes un problema con el pago, puedes proporcionar algún detalle más ?",
# }

# INTENT_KEYWORDS = {
#     "greeting": ["Hola", "buenos dias", "buenas tardes", "buenas noches", "hola Gordo", "Hola Dodi"],
#     "help_order":["ayuda", "pedido", "remito","orden", "factura", "problema", "reparto" ],
#     "farewell":["Adios", "Hasta luego", "nos vemos", "chau"],
#     "thank_you": ["gracias", "agradecido", "te agradezco", "muchas gracias"],
#     "product_inquiry":["productos", "indormacion", "detalles", "materiales", "repartos", "domicilios"],
#     "complaint":["queja", "reclamo", "enojo", "insatisfecho", "no llega", "atraso", "demorado", "demora", "lento"],
#     "delivery_status":["entrega", "envio", "estado", "reparto", "bolsas", "hierro", "arena", "ripio", "hormigon", "cemento", "que paso"],
#     "payment_issues":["pago", "factura", "problema con el pago", "problema con la fecha", "error en la factura", "error importe"],
# }

# def get_intent(text):
#     doc = nlp(text.lower())
#     for token in doc:
#         for intent, keywords in INTENT_KEYWORDS.items():
#             if token.text in keywords:
#                 return intent
#     return "unknown"

# def process_text(text):
#     intent = get_intent(text)
#     return RESPONSE.get(intent, "lo siento, no se como responder a eso; ya te paso con Luca")

# while True:
#     user_input = input('Tu:')
#     if user_input.lower() in ["salir", "exit"]:
#         print('DodiBot: nos vemos !')
#         break
#     if not user_input.strip():
#         print('parece que no ingresaste nada, probá de nuevo...')
#         continue
#     response = process_text(user_input)
#     print('DodiBot: ',response)

