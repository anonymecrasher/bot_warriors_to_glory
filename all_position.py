# importation des modules
import time
import pynput

# set up
mouse = pynput.mouse.Controller()

positions = {
    'Combatre': (),
    'Guerrier': (),
    'Boutiques': (),
    'Inventaire': (),
    'Bijoux': (),
    'Maison': (),
    'taverne': (),
    'Option': (),
    'Quitter': (),
    '1c1': (),
    '2c2': (),
    'Chacun pour soi': (),
    'Boss': (),
    'Détendu': (),
    'Brutal': (),
    'Trouver match': (),
    'Attributs': (),
    'For': (),
    'Agi': (),
    'Att': (),
    'Ene': (),
    'Vit': (),
    'Ok': (),
    'Capacité': (),
    'Bete de scene': (),
    'Gros dormeurs': (),
    'Mec de fer': (),
    'Coriacite': (),
    'Defense attaquante': (),
    'Frappes vanpiriques': (),
    'Noix incassable': (),
    'Frappe de la mort': (),
    'Choc ahurissant': (),
    'Point faible': (),
    'Betes acculée': (),
    'Carrossier': (),
    'Assaut continu': (),
    'Ames du combatant': (),
    'Fleches dans le genou': (),
    'Tirs bas': (),
    'Riposte': (),
    'Arrivée en fléches': (),
    'Passe-passe': (),
    'Prompt tireur': (),
    'Attaque en flèche': (),
    'Blessure ouverte': (),
    'Frappe critique': (),
    'Attaque pernicieuse': (),
    'Attaque combinée': (),
    'Oeil du Tigre': (),
    'Fervante garde': (),
    'Brouillard de guerre': (),
    'Célérité': (),
    'Ouverture de la chasse': (),
    'Cadeau sucré': (),
    'Concours de danse': (),
    'Attrapeur d ames': (),
    'Rennaissance': (),
    'Frappe Gavra': (),
    'Main heureuse': (),
    'roi d atouts': (),
    'Désarmement': (),
    'Entrée spectaculaire': (),
    'Homme du peuple': (),
    'Le tranquilisant': (),
    'Control de la foule': (),
    'boutique armure': (),
    'boutique épée': (),
    'boutique hache': (),
    'boutique arc': (),
    'shop item 1': (),
    'shop item 2': (),
    'shop item 3': (),
    'shop item 4': (),
    'shop item 5': (),
    'shop item 6': (),
    'shop suivant': (),
    'shop precedant': (),
    'shop Retour': (),
    'inventaire slot 1': (),
    'inventaire slot 2': (),
    'inventaire slot 3': (),
    'inventaire slot 4': (),
    'inventaire slot 5': (),
    'inventaire slot 6': (),
    'inventaire slot 7': (),
    'inventaire slot 8': (),
    'Gem feu': (),
    'Gem gel': (),
    'Gem ven': (),
    'Gem ter': (),
    'Gem eau': (),
    'Gem niv1': (),
    'Gem niv2': (),
    'Gem niv3': (),
    'Gem niv4': (),
    'Gem niv5': (),
    'Gem niv6': (),
# Bijoux

# Maison

# Taverne






}


# declaration des class


# declaration des fonction
def get_position():
    time.sleep(2)
    for i in range(200):
        print(mouse.position)
        time.sleep(0.1)


# Programme principal

def main():
    get_position()


if __name__ == '__main__':
    main()
