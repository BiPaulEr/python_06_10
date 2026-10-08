import logging
import random

class UFilter(logging.Filter):
    def filter(self, record):
        return not "8" in record.getMessage()







livres_logger = logging.getLogger('loggers.livres')
transactions_logger = logging.getLogger('loggers.transactions')

livres_logger.setLevel(logging.INFO) 
transactions_logger.setLevel(logging.WARNING)
livres_f = logging.Formatter(
    '%(asctime)s %(module)s %(levelname)s %(funcName)s %(message)s', datefmt='%d/%m/%Y %H:%M'
)

livres_handler = logging.StreamHandler()
livres_logger.addHandler(livres_handler)
livres_handler.setFormatter(livres_f)
livres_handler.addFilter(UFilter())

stream_handler = logging.StreamHandler()
transactions_f = logging.Formatter(
    '%(name)s %(levelname)s %(message)s'
)
stream_handler.setFormatter(transactions_f)
transactions_logger.addHandler(stream_handler)


bibliotheque = {}

def add_book(title):
    if random.randint(0, 100) >10:
        bibliotheque[title] = True
        livres_logger.info(f"Nouveau livre {title} ajouté à la bibliothèque")
    else:
        livres_logger.warning(f"Le livre {title} n'a pas pu être ajouté à la bibliothèque")


def process_transaction(user_id, book_id):
    if book_id in bibliotheque:
        transactions_logger.info(f"Utilisateur {user_id} a acheté le livre {book_id}")
        del bibliotheque[book_id]
    else:
        transactions_logger.warning(f"Échec de l'achat pour l'utilisateur {user_id} : le livre {book_id} n'existe pas dans la bibliothèque")

livres_a_ajouter = ["Livre1", "Livre2", "Livre3", "Livre4", "Livre5", "Livre6", "Livre7", "Livre8", "Livre9", "Livre10"]
utilisateurs = ["Paul", "Dupont", "Gaorges"]

for livre in livres_a_ajouter:
    add_book(livre)

while len(bibliotheque) > 0:
    for utilisateur in utilisateurs:
        for livre in livres_a_ajouter:
            process_transaction(utilisateur, livre)