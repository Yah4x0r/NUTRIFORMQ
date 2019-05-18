from tkinter import *
import sqlite3


# UNE CLASSE REGROUPE DES FONCTIONS ET DES ATTRIBUTS QUI DEFINISSENT UN OBJET.
class ContactManager(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        # SELF ME PERMET DE STOCKER UNE INFORMATION DANS LA CLASSE
        self.configure(background='#41B77F')
        self.language = "French"
        self.title = "NUTRIFORMQ"
        self.Rentrer = "Rentrer!"
        self.pagelabel1 = "VOS DONNÉE PERSONNEL"
        self.pagelabel2 = "Comment voulez vous que je vous apelle ?"
        self.pagelabel3 = "Quel est votre âge ?"
        self.pagelabel4 = "Quel est votre taille (en cm) ?"
        self.pagelabel5 = "Quel est votre poids (en Kg) ?"
        self.pagelabel6 = "Je suis une/un : "
        self.pagelabel7 = "Quel est votre morphologie ?"
        self.pagelabel8 = "Valider !"
        self.pagelabel9 = "RÉSULTATS POUR"
        self.pagelabel10 = "Votre IMC (Indice de Masse Corporelle) en (kg/m²):"
        self.pagelabel11 = "Votre Poids idéal selon Creff (Kg) :"
        self.imc_var = 0
        self.weight = 0
        self.vHeight = 0
        self.pin_var = 0
        self.vAge = 10
        self.sexe_var = 0
        self.vName = ""
        self.mg = 0
        self.corpulence_var = 1
        self.MR = 0
        self.msg = "Chez NUTRIFORM nous voulons absolument " \
                   " utile aux autres et accompagner " \
                   "les utilisateurs dans leur quête de bonne santé physique"
        self.email = "Votre e-mail ?"
        self.IMG = "Votre IMG (Indice de Masse Grasse) est de (%):"
        self.metabase = "Votre métabolisme de base (kcal/j) :"
        self.retour = "Retour"
        self.pagelabel321 = "En savoir plus"
        self.pagelabel322 = "Remerciement"
        self.man = "Homme"
        self.women = "Femme"
        self.what = "Qu'est ce que ?"
        self.ideal = "Poids Idéal"
        self.IMC = "IMC"
        self.FMI = "IMG"
        self.BasicMeta = "Métabolisme de Base"
        self.pititre = "ORIGINES DU POIDS IDÉAL DE CREFF & EXPLICATIONS"
        self.piexplain = "La formule de Creff fait partie des nombreuses " \
                         "formules permettant de connaitre son poids idéal" \
                         "théorique.\nCette formule a l’avantage  de faire" \
                         "rentrer la notion de morphologie.\nUne dimension " \
                         "qui était jusqu’à présent ignorée dans les autres " \
                         "formules les plus populaires.\n La formule dépend " \
                         "de la morphologie de l’individu. Pour une personne "\
                         "à\nla morphologie fine, le résultat « classique » " \
                         "est en effet minoré de 10%, et pour une personne " \
                         "à\nla morphologie « large » ce même résultat est " \
                         "alors majoré de 10%.\n\nLes équations permettant " \
                         "d’utiliser la formule de Creff sont présentées " \
                         "ci-après.\nDans le cas d’une morphologie classique,"\
                         "le poids idéal théorique est donné de cette manière"\
                         ":\nPoids idéal = (T−100+(A/10))∗0,9\nDans le cas " \
                         "d’une morphologie « gracile », le résultat est " \
                         "minoré de 10%, soit laformule suivante :\nPoids " \
                         "idéal = (T−100+(A/10))∗0,9∗0,9\nPour une "\
                         " morphologie « large », le résultat est majoré de " \
                         "10%,* soit la formule suivante :\nPoids idéal" \
                         " = (T−100+(A/10))∗0,9∗1,1\n\n" \
                         "Où la taille est exprimée en centimètres " \
                         "(valeur T), l’âge en années (valeur A) et où le " \
                         "résultat obtenu est fourni en kilogrammes.\nLe " \
                         "principal inconvénient de cette formule est le fait"\
                         "qu’évaluer sa propre morphologienécessite une"\
                         "première interprétation\ntrès subjective de "\
                         "soi-même. \nDe plus, cette notion est vague, elle"\
                         " ne peut pas être clairement déterminée."
        self.piexplainref = "SOURCES ET RÉFÉRENCES Pai MP, Paloucek FP. " \
                            "The origin of the ideal » body weight equations."\
                            "«Ann Pharmacother. 2000;34(9):1066-9. " \
                            "PMID 10981254."
        self.imc0 = "INTERPRÉTATION DE L’INDICE DE MASSE CORPORELLE"
        self.imc1 = "L’interprétation se fait selon la classification de " \
                    "l’OMS (Organisation Mondiale de la Santé)."
        self.imc2 = "Inférieur à 18.5 : Maigreur"
        self.imc3 = "Entre 18.5 & 25 : Corpulence Normal"
        self.imc4 = "Supérieur à 25 : Surpoids"
        self.imc5 = "Le calcul de l’IMC est relativement simple puisqu’il " \
                    "ne nécessite que deux critères: votre taille (en cm)" \
                    "et votre poids (en kg).\n La formule mathématique exacte"\
                    " est la suivante : \nIMC = Poids(kg) / Taille (m)^2" \
                    "\nL’IMC permet de déterminer de manière objective " \
                    "la corpulence d’une personne.\nC’est au mathématicien" \
                    " Adolphe Quetelet (1796-1874) que l’on " \
                    "doit cet indice.\nCette classification a pour rôle " \
                    "d’évaluer les risques liés au surpoids.\nLe fait " \
                    "de calculer de manière régulière " \
                    "son IMC présente donc un intérêt :\nrepérer " \
                    "ses propres évolutions de poids et les " \
                    "interpréter en accord avec les informations " \
                    "fournies par l’OMS.\nLes avantages de l’IMC " \
                    "sont les suivants :\nFacilité de calcul qui ne " \
                    "nécessite que le poids et la taille, à " \
                    "travers une formule simple (voir formule" \
                    " ci-dessus).\nIndicateur généralisé de " \
                    "manière « internationale », permettant donc de" \
                    " faire des statistiques à l’échelle mondiale."
        self.img00 = "INTERPRÉTATION DE L’INDICE DE MASSE GRASSE"
        self.img0 = "L’indice de masse graisseuse permet de " \
                    "faire une estimation\n" \
                    " de la proportion entre sa masse de graisse" \
                    " et sa masse de muscle.\n" \
                    "Connaître son indice de masse grasse " \
                    "est utile pour se rendre compte" \
                    " de la proportion de graisse dans notre " \
                    "corps.\nEn effet, un excès de" \
                    " graisse peut avoir des conséquences plus " \
                    "ou moins grave sur la santé,\n" \
                    " qui peuvent aller de l’essoufflement au " \
                    "cholestérol, voire même provuqer" \
                    " des risques d’AVC (Accidents " \
                    "Cardio-Vasculaire).\nUne surveillance " \
                    "régulière grâce à cet indice est " \
                    "donc tout indiqué pour surveiller " \
                    "sa masse graisseuse et éviter les ennuis de santé."
        self.img1 = "Valeur de l’IMG Interprétation :"
        self.img2 = "Pour les femmes :\n" \
                    "Inférieur à 25% : Trop maigre\n" \
                    "Entre 25% et 30% : Pourcentage normal\n" \
                    "Supérieur à 30% :  Trop de graisse\n"
        self.img3 = "Pour les hommes :\n" \
                    "Inférieur à 15% : Trop maigre\n" \
                    "Entre 15% et 20% : Pourcentage normal\n" \
                    "Supérieur à 20% : Trop de graisse"
        self.MB0 = "INTERPRÉTATION DU MÉTABOLISME DE BASE"
        self.MB1 = "Il s’agit d’une estimation de la quantité " \
                   "d’énergie (en calories)\nque votre corps a " \
                   "besoin de manière quotidienne, lorsqu’il est au repos."
        self.MB2 = "Cette valeur est particulièrement intéressante" \
                   "car muni de votre métabolisme de base,\n" \
                   "vous pourrez ensuite avoir une estimation\n" \
                   "de l’énergie dont votre corps a besoin en " \
                   "fonction de votre niveau d’activité physique.\n" \
                   "Vous pourrez ainsi comparer vos apports caloriques " \
                   "journaliers, à vos dépenses caloriques journalières.\n" \
                   "Après avoir effectué le calcul " \
                   "de votre métabolisme de base (MB),\nvous savez " \
                   "combien d’énergie votre corps dépense " \
                   "quotidiennement lorsqu’il est totalement au repos." \
                   "\nOui mais voilà : votre corps n’est jamais totalement " \
                   "au repos,\nla moindre activité physique et/ou cérébrale " \
                   "entraine une consommation supplémentaire de calories… " \
                   "\nC’est la raison pour laquelle le tableau" \
                   " vous explique, " \
                   "par rapport à votre métabolisme de base (MB),\n" \
                   " quelle est votre dépense énergétique réelle."
        self.MB3 = "Avoir une idée, même approximative," \
                   " de ce que son corps peut " \
                   "consommer de manière quotidienne\n" \
                   "peut évidemment vous aider à " \
                   "mieux gérer votre alimentation.\n" \
                   "Car c’est votre alimentation " \
                   "qui fait rentrer les calories " \
                   "(qui sont ensuite dépensés par " \
                   "votre corps) :\nil faudrait donc, " \
                   "idéalement, qu’il existe un" \
                   " équilibre entre vos apports " \
                   "énergétiques et vos dépenses. " \
                   "\nLe corps fonctionne donc comme une " \
                   "balance énergétique et a " \
                   "pour objectif de dépenser le même" \
                   " nombre de calories que ce " \
                   "qui sera consommé.\nDans ce cas le " \
                   "poids corporel ne change pas. " \
                   "Mais lorsque la balance se dérègle il " \
                   "y a alors deux cas de figure :"
        self.MB4 = "Si l’on mange plus que ce que l’on dépense " \
                   "on grossit, car on stocke l’énergie non utilisée."
        self.MB5 = "Si l’on dépense plus d’énergie que ce que nous " \
                   "apportent nos repas on perd du poids, car le corps " \
                   "puise dans ses réserves d’énergie."

        self.suivant = "Suivant"
        self.parent = parent
        self.initui()

    # PREMIERE FENETRE
    def initui(self):
        self.parent.title(self.title)
        self.parent.minsize(1080, 720)
        self.parent.maxsize(1080, 720)
        self.parent.iconbitmap("logo.ico")
        self.pack(fill=BOTH, expand=1)
        Label(self, text=self.title,
              font=("Times", 40), bg='#41B77F',
              fg='white').place(relx=.5, rely=.3, anchor="center")
        Label(self, text=self.msg,
              font=("Times", 13), bg='#41B77F',
              fg='white').place(relx=.5, rely=.4, anchor="center")

        # CHOIX DE LA LANGUE
        variable = StringVar(self)
        variable.set(self.language)  # default value
        langoption = OptionMenu(self, variable, "English", "French",
                                command=self.selectlang)
        langoption.config(bg="#41B77F", fg='white')
        langoption.place(relx=1, rely=.0, anchor="ne")
        Button(self, text=self.Rentrer, width=10, height=2,
               font=("Times", 10), bg='white', fg='#41B77F',
               command=self.secondpage) \
            .place(relx=.5, rely=.6, anchor="center")

        # POSITIONNEMENT DE L'IMAGE
        image1 = PhotoImage(file='logo.PNG').zoom(35).subsample(50)
        label = Label(self, image=image1)
        label.image = image1  # keep a reference!
        label.place(relx=.5, rely=.8, anchor="center")
        # ASSURER UN ROLE SYNTAXIQUE IMPORTANT DANS LE PROGRAMMES
        pass

    # SI LA LANGUE CHOISIS EST L'ANGLAIS
    def selectlang(self, value):
        self.language = value
        if self.language == "English":
            self.pagelabel2 = "How do you want me to call you?"
            self.title = "NUTRIFORMQ"
            self.pagelabel3 = "What is your age ?"
            self.pagelabel1 = "YOUR PERSONAL DATA"
            self.pagelabel4 = "What is your height (in cm)?"
            self.pagelabel5 = "What is your weight (in Kg)?"
            self.pagelabel6 = "I am Man/ Women:"
            self.pagelabel7 = "What is your morphology?"
            self.pagelabel8 = "Validate!"
            self.Rentrer = "Come in!"
            self.pagelabel9 = "RESULTS FOR"
            self.pagelabel10 = "BMI :"
            self.pagelabel11 = "Ideal Weight :"
            self.msg = "At NUTRIFORM we absolutely want to be useful " \
                       "to others and support " \
                       "users in their quest for good physical health"
            self.email = "Your e-mail ?"
            self.IMG = "Your FMI (Fat mass Index) is (%) :"
            self.metabase = "Your basic metabolism (kcal / day):"
            self.retour = "Return"
            self.pagelabel321 = "Learn more"
            self.pagelabel322 = "Appreciation"
            self.man = "Man"
            self.women = "Women"
            self.what = "What is it ?"
            self.ideal = "Ideal weight"
            self.IMC = "BMI"
            self.FMI = "FMI"
            self.BasicMeta = "Basic Metabolism"
            self.pititre = "ORIGINS OF THE IDEAL WEIGHT OF CREFF &" \
                           " EXPLANATIONS"
            self.piexplain = "The formulas of Creff has the popular number.\n"\
                             "This formula has the advantage of bringing back"\
                             "the notion of morphology.\nA dimension that was"\
                             "previously ignored in other popular " \
                             "formulas.\nThe formula depends on the "\
                             " morphology of the individual." \
                             "For the person to\nthe fine morphology, " \
                             "the result of classic, is at a minoring of" \
                             " 10%, and to\nmorphology, " \
                             "normal, is same to the great " \
                             "of 10%.\nEquations for using the Creff formula"\
                             "are presented below.\nIn the case of " \
                             "classical morphology, the ideal " \
                             "weight is given in this way:\n" \
                             "Ideal weight = (T - 100 + (A / 10))" \
                             " * 0.9\nIn the case of fine " \
                             "morphology, the result is reduced " \
                             "by 10%, ie the following formula\n" \
                             ":Ideal weight = (T - 100 + (A / 10)) " \
                             "* 0.9 0.9\nFor large morphology," \
                             "the result is increased by 10%, ie" \
                             " the following formula:\nIdeal " \
                             "weight = (T - 100 + (A / 10)) * 0.9 1.1\n\n" \
                             "Where the size is expressed " \
                             "in centimeters, the age in years and the " \
                             "result obtained in kilogram.\nThe main " \
                             "drawback of this formula is very real, " \
                             "but its own interpretation\n" \
                             " is very subjective.\nMoreover, this notion" \
                             "is vague, it can not be clearly determined."
            self.piexplainref = "SOURCES AND REFERENCES(1) Pai MP, Paloucek " \
                                "FP. The origin of the" \
                                " ideal equations of body weight. Ann" \
                                " Pharmacother. 2000; 34 (9): " \
                                "1066-109. PMID 10981254."
            self.imc0 = "INTERPRETATION OF THE INDEX OF BODY MASS :"
            self.imc1 = "The interpretation is according to the"\
                        "classification of the OMS " \
                        "(World Health Organization)."
            self.imc2 = "Less than 18.5: Thinness"
            self.imc3 = "Between 18.5 & 25: Normal Body"
            self.imc4 = "Greater than 25: Overweight "
            self.imc5 = "The calculation of the BMI is " \
                        "relatively simple since it does not " \
                        "require only two criteria: your" \
                        " height (in cm) and your weight (in kg)." \
                        "\nThe exact mathematical formula " \
                        "is: \nBMI = Weight (kg) / Height (m) ^ 2" \
                        "\nBMI can be used to objectively" \
                        " determine a person's body size." \
                        "\nIt is to the mathematician " \
                        " Adolphe Quetelet (1796-1874)" \
                        " that we owe this index.\nThe " \
                        "purpose of this classification " \
                        "(see table above) is to assess the" \
                        " risks associated with being overweight." \
                        "\nThe fact of regularly calculating " \
                        "one's BMI is thus of interest: \nto " \
                        "identify one's own changes in weight " \
                        "and to interpret them in accordance " \
                        "with the information provided by OMS. " \
                        "The benefits of BMI are:\n Ease of " \
                        "calculation that requires only weight " \
                        "and size, through a simple formula" \
                        " .\nIndicator generalized in an international way," \
                        " thus making it possible to make" \
                        " statistics on a world scale."
            self.img00 = "INTERPRETATION OF THE INDEX OF FAT MASS"
            self.img0 = "The fat mass index makes it possible " \
                        "to estimate the proportion\n" \
                        " between a mass of fat and a mass of muscle.\n" \
                        "Knowing your body fat index is helpful in realizing" \
                        " the proportion of fat in your body.\nIndeed, excess"\
                        "fat can have more or less serious consequences on " \
                        "health,\nwhich can range from shortness of breath to"\
                        " cholesterol,\nor even provoke the risk of stroke " \
                        "(Cardiovascular Accidents).\nRegular monitoring with"\
                        " this index is ideal for monitoring your body fat " \
                        "and avoiding health problems."
            self.img1 = "Value of IMG Interpretation"
            self.img2 = "For women:\n" \
                        "Less than 25% : too lean \n" \
                        "Between 25% and 30% : Normal percentage\n" \
                        " Greater than 30% : Too much fat\n"
            self.img3 = "For men:\n" \
                        "Less than 15% : Too lean\n" \
                        "Between 15% and 20% : Normal percentage\n" \
                        "Greater than 20% : fat\n"
            self.MB0 = "INTERPRETATION OF BASIC METABOLISM"
            self.MB1 = "This is an estimate of how much energy(in calories)\n"\
                       " your body needs on a daily basis, when it is at rest."
            self.suivant = "Next"
            self.MB2 = "This value is particularly interesting because\n" \
                       " with your basic metabolism, you can then have " \
                       "an estimate of the energy your body needs according\n"\
                       " to your level of physical activity. You will" \
                       " be able to compare your daily calorie intake\n" \
                       "to your daily caloric expenditure. After performing" \
                       " the calculation of your basal metabolism (MB)\n," \
                       " you know how much energy your body spends daily when"\
                       "fully rested.\nYes but here it is: your body is never"\
                       "totally at rest, the least physical activity and / or"\
                       "brain leads to an additional consumption " \
                       "of calories ...\n" \
                       "This is why the table below (which we" \
                       " calculate automatically " \
                       "when you use our tool above)\n," \
                       "explains to you, in relation to " \
                       "your basic metabolism (MB)\n" \
                       ", what is your actual energy expenditure."
            self.MB3 = "Having an idea, even approximate, of what your" \
                       " body can consume on a daily basis" \
                       "can obviously help you better manage your diet.\n" \
                       "Because it is your diet that gets calories (which are"\
                       "then spent by your body):\nideally, there should be a"\
                       "balance between your energy intake and your expenses."\
                       "\nThe body thus functions as an energy balance and" \
                       " aims to spend the same number of calories as"\
                       "  what will be consumed.\nIn this case the body " \
                       " weight does not " \
                       "change.\nBut when the balance goes out " \
                       "of order there are then two cases:"
            self.MB4 = "If you eat more than you spend you get " \
                       "bigger, because you store unused energy."
            self.MB5 = "If we spend more energy than we bring " \
                       "our meals we lose weight, b" \
                       "ecause the body draws on its energy reserves."
            pass
        self.clearframe()
        self.initui()
        pass

    # PASSAGE A LA FENETRE 2 : J'EFFACE TOUT CE QU'IL Y'A DANS LA FENETRE 1
    def clearframe(self):
        for child in self.winfo_children():
            child.destroy()
        pass

    # JE POSSITIONNE MES ELEEMNTS DANS LA FENETRE 2

    def secondpage(self):
        self.clearframe()
        Label(self, text=self.pagelabel1,
              font=("Times", 40), bg='#41B77F',
              fg='white').place(relx=.5, rely=.1, anchor="center")
        image2 = PhotoImage(file='donne.PNG').zoom(35).subsample(50)
        label1 = Label(self, image=image2)
        label1.image = image2  # keep a reference!
        label1.place(relx=.5, rely=.2, anchor="center")

        # NOM
        Label(self, text=self.pagelabel2, font=("Times", 15), bg='#41B77F',
              fg='white').place(relx=.5, rely=.3, anchor="e")
        self.vName = StringVar()
        Entry(self, textvariable=self.vName,
              width=30).place(relx=.5, rely=.3, anchor="w")

        # AGE
        Label(self, text=self.pagelabel3, font=("Times", 15), bg='#41B77F',
              fg='white').place(relx=.5, rely=.35, anchor="e")
        self.vAge = IntVar()
        self.vAge.set(10)
        Spinbox(self, from_=10, to=99,
                textvariable=self.vAge).place(relx=.5, rely=.35, anchor="w")

        # TAILLE
        Label(self, text=self.pagelabel4, font=("Times", 15), bg='#41B77F',
              fg='white').place(relx=.5, rely=.4, anchor="e")
        self.vHeight = IntVar()
        self.vHeight.set(10)
        Spinbox(self, from_=100, to=230,
                textvariable=self.vHeight).place(relx=.5, rely=.4, anchor="w")

        # POIDS
        Label(self, text=self.pagelabel5,
              font=("Times", 15), bg='#41B77F',
              fg='white').place(relx=.5, rely=.45, anchor="e")
        self.weight = IntVar()
        Scale(self, variable=self.weight, from_=10, to=130,
              orient='horizontal', bg='#41B77F',
              fg='white').place(relx=.5, rely=.45, anchor="w")

        # SEXE
        Label(self, text=self.pagelabel6, font=("Times", 15), bg='#41B77F',
              fg='white').place(relx=.5, rely=.5, anchor="e")
        self.sexe_var = IntVar()
        self.sexe_var.set(0)
        Radiobutton(self, text=self.man, font=("Times", 15),
                    variable=self.sexe_var, value=0,
                    bg='#41B77F').place(relx=.5, rely=.5, anchor="w")
        Radiobutton(self, text=self.women, font=("Times", 15),
                    variable=self.sexe_var, value=1,
                    bg='#41B77F').place(relx=.6, rely=.5, anchor="w")
        # CORPULENCE
        Label(self, text=self.pagelabel7, font=("Times", 15), bg='#41B77F',
              fg='white').place(relx=.5, rely=.55, anchor="e")
        self.corpulence_var = IntVar()
        self.corpulence_var.set(3)
        Radiobutton(self, text=" Fine  ", font=("Times", 15),
                    variable=self.corpulence_var, value=1,
                    bg='#41B77F').place(relx=.5, rely=.55, anchor="w")
        Radiobutton(self, text="Normal ", font=("Times", 15),
                    variable=self.corpulence_var, value=2,
                    bg='#41B77F').place(relx=.6, rely=.55, anchor="w")
        Radiobutton(self, text=" Large ", font=("Times", 15),
                    variable=self.corpulence_var, value=3,
                    bg='#41B77F').place(relx=.7, rely=.55, anchor="w")
        Label(self, text=self.email, font=("Times", 15), bg='#41B77F',
              fg='white').place(relx=.5, rely=.60, anchor="e")
        self.vEmail = StringVar()
        Entry(self, textvariable=self.vEmail,
              width=30).place(relx=.5, rely=.60, anchor="w")
        Button(self, text=self.pagelabel8, width=10, height=2,
               font=("Times", 10), bg='white', fg='#41B77F',
               command=self.thirdpage) \
            .place(relx=.5, rely=.70, anchor="center")
        pass

    # MES DEFINIS MES CALCULS QUI SERONT PLACEE DANS LA FENETRE 3
    def thirdpage(self):
        self.calculimc()
        self.clearframe()
        # DANS LE CAS QUE LA CORPULENCE CHOISIS SOIT : FINE
        if self.corpulence_var.get() == 1:
            self.pin = (self.vHeight.get() - 100 +
                        self.vAge.get() / 10) * 0.9 * 0.9
            print("pin :" + str(self.pin))
            pin_var = IntVar()
            pin_var.set(self.pin)
            pass
        # DANS LE CAS QUE LA CORPULENCE CHOISIS SOIT : LARGE
        elif self.corpulence_var.get() == 3:
            self.pin = (self.vHeight.get() - 100 +
                        self.vAge.get() / 10) * 0.9 * 1.1
            pin_var = IntVar()
            pin_var.set(self.pin)
            pass
        # DANS LE CAS QUE LA CORPULENCE CHOISIS SOIT : NORMAL
        else:
            self.pin = (self.vHeight.get() - 100 +
                        self.vAge.get() / 10) * 0.9
            pin_var = IntVar()
            pin_var.set(round(self.pin, 2))
            pass
        Label(self, text=self.pagelabel9 + " " +
              self.vName.get().upper(),
              font=("Times", 40), bg='#41B77F',
              fg='white').place(relx=.5, rely=.1, anchor="center")
        #         You Ideal Weight
        Label(self, text=self.pagelabel11,
              font=("Times", 20), bg='#41B77F',
              fg='white').place(relx=.5, rely=.2, anchor="n")
        Label(self, textvariable=pin_var,
              font=("Times", 25), bg='#009900',
              fg='white').place(relx=.5, rely=.3, anchor="n")

        # POSITIONNEMENT DE L'IMC
        imc = IntVar()
        imc.set(self.imc_var)
        Label(self, text=self.pagelabel10, font=("Times", 20),
              bg='#41B77F', fg='white').place(relx=.5, rely=.4, anchor="n")
        Label(self, textvariable=imc, font=("Times", 25),
              bg='#009900', fg='white').place(relx=.5, rely=.5, anchor="n")
        # CALCULE DE L'IMG(Indice de Masse Grasse)
        self.mg = round((1.20 * self.imc_var) +
                        (0.23 * self.vAge.get()) -
                        (10.8 * int(self.sexe_var.get())) - 5.4, 2)
        print(self.mg)
        mg = IntVar()
        mg.set(self.mg)
        Label(self, text=self.IMG,
              font=("Times", 20), bg='#41B77F',
              fg='white').place(relx=.5, rely=.6, anchor="n")
        Label(self, textvariable=mg, font=("Times", 25), bg='#009900',
              fg='white').place(relx=.5, rely=.7, anchor="n")

        # CALCULE DU Métabolisme de Base S =
        # (Size ^ 0.725) * (Weight ^ 0.425) * 0.202)
        # then MR = 24 * 37.5 * S
        self.MR = ((self.vHeight.get() / 100) ** 0.725) * \
                  ((self.weight.get() ** 0.425) * (0.202)) * 37.5 * 24
        print(self.MR)
        mr = IntVar()
        mr.set(round(self.MR, 2))
        Label(self, text=self.metabase,
              font=("Times", 20), bg='#41B77F',
              fg='white').place(relx=.5, rely=.8, anchor="n")
        Label(self, textvariable=mr, font=("Times", 25), bg='#009900',
              fg='white').place(relx=.5, rely=.9, anchor="n")
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.secondpage) \
            .place(relx=.1, rely=.9, anchor="n")
        Button(self, text=self.pagelabel321, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.fourpage) \
            .place(relx=.90, rely=.9, anchor="n")

        NomDB = self.vName.get()
        AgeDB = self.vAge.get()
        PoidsDB = self.weight.get()
        EmailDB = self.vEmail.get()
        ImcDB = self.imc_var
        WTLDB = PoidsDB - self.pin

        conn = sqlite3.connect("NutriForMQDB.db")
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Bilan (Nom TEXT , Age REAL , "
            "Poids REAL , Mail TEX T, Imc REAL , WTL REAL)")
        cursor.execute("INSERT INTO Bilan (Nom, Age, Poids , Mail , "
                       "Imc , WTL) VALUES(?,?,?,?,?,?)",
                       (NomDB, AgeDB, PoidsDB, EmailDB, ImcDB, WTLDB))
        conn.commit()
        pass

    def wpi(self):
        self.clearframe()
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.fourpage) \
            .place(relx=.1, rely=.9, anchor="n")
        Label(self, text=self.pititre,
              font=("Times", 20), bg='#006600',
              fg='white').place(relx=.5, rely=.1, anchor="center")
        Label(self, text=self.piexplain,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.5, anchor="center")
        Label(self, text=self.piexplainref,
              font=("Times", 12), bg='#41B77F',
              fg='white', ).place(relx=.5, rely=.8, anchor="center")

    def wimc(self):
        self.clearframe()
        Label(self, text=self.imc0,
              font=("Times", 20), bg='#006600', fg='white') \
            .place(relx=.5, rely=.1, anchor="center")
        Label(self, text=self.imc1,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.2, anchor="center")
        Label(self, text=self.imc2,
              font=("Times", 14), bg='#41B77F',
              fg='#00ffff').place(relx=.5, rely=.3, anchor="center")
        Label(self, text=self.imc3,
              font=("Times", 14), bg='#41B77F',
              fg='#00ff00').place(relx=.5, rely=.4, anchor="center")
        Label(self, text=self.imc4,
              font=("Times", 14), bg='#41B77F',
              fg='#ff0000').place(relx=.5, rely=.5, anchor="center")
        Label(self, text=self.imc5,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.7, anchor="center")
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.fourpage) \
            .place(relx=.1, rely=.9, anchor="n")

    def wimg(self):
        self.clearframe()
        Label(self, text=self.img00,
              font=("Times", 20), bg='#006600', fg='white') \
            .place(relx=.5, rely=.1, anchor="center")
        Label(self, text=self.img0,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.3, anchor="center")
        Label(self, text=self.img1,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.5, anchor="center")
        Label(self, text=self.img2,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.6, anchor="center")
        Label(self, text=self.img3,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.8, anchor="center")
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.fourpage) \
            .place(relx=.1, rely=.9, anchor="n")

    def wmb2(self):
        self.clearframe()
        Label(self, text=self.MB0,
              font=("Times", 20), bg='#006600', fg='white') \
            .place(relx=.5, rely=.1, anchor="center")
        Label(self, text=self.MB3,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.3, anchor="center")
        Label(self, text=self.MB3,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.5, anchor="center")

        Label(self, text=self.MB4,
              font=("Times", 14), bg='#41B77F',
              fg='#ff8000').place(relx=.5, rely=.6, anchor="center")
        image3 = PhotoImage(file='gainpoids.png')
        label = Label(self, image=image3)
        label.image = image3  # keep a reference!
        label.place(relx=.5, rely=.7, anchor="center")
        Label(self, text=self.MB5,
              font=("Times", 14), bg='#41B77F',
              fg='#00ff00').place(relx=.5, rely=.8, anchor="center")
        image4 = PhotoImage(file='pertepoids.png')
        label = Label(self, image=image4)
        label.image = image4  # keep a reference!
        label.place(relx=.5, rely=.9, anchor="center")
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.thirdpage) \
            .place(relx=.1, rely=.9, anchor="n")

    def wmb(self):
        self.clearframe()
        Label(self, text=self.MB0,
              font=("Times", 20), bg='#006600', fg='white') \
            .place(relx=.5, rely=.1, anchor="center")
        Label(self, text=self.MB1,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.2, anchor="center")
        Label(self, text=self.MB2,
              font=("Times", 14), bg='#41B77F',
              fg='white').place(relx=.5, rely=.3, anchor="center")
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.fourpage) \
            .place(relx=.1, rely=.9, anchor="n")
        Button(self, text=self.suivant, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.wmb2) \
            .place(relx=.90, rely=.9, anchor="n")
        image2 = PhotoImage(file='tableau.PNG')
        label = Label(self, image=image2)
        label.image = image2  # keep a reference!
        label.place(relx=.5, rely=.7, anchor="center")

    def fin(self):
        self.clearframe()
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.fourpage) \
            .place(relx=.1, rely=.9, anchor="n")
        Label(self, text=self.img3,
              font=("Times", 14), bg='#41B77F',
              fg='white').place()

    def fourpage(self):
        self.clearframe()
        Label(self, text=self.what, font=("Times", 40),
              bg='#006600', fg='white') \
            .place(relx=.5, rely=.1, anchor="center")
        Button(self, text=self.ideal, width=20, height=7,
               font=("Times", 10,), bg='white',
               fg='#41B77F', command=self.wpi) \
            .place(relx=.5, rely=.2, anchor="n")
        Button(self, text=self.IMC, width=20, height=7,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.wimc) \
            .place(relx=.5, rely=.4, anchor="n")
        Button(self, text=self.FMI, width=20, height=7,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.wimg) \
            .place(relx=.5, rely=.6, anchor="n")
        Button(self, text=self.BasicMeta, width=20, height=7,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.wmb) \
            .place(relx=.5, rely=.8, anchor="n")
        Button(self, text=self.retour, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.thirdpage) \
            .place(relx=.1, rely=.9, anchor="n")
        Button(self, text=self.pagelabel322, width=10, height=2,
               font=("Times", 10), bg='white',
               fg='#41B77F', command=self.fin) \
            .place(relx=.90, rely=.9, anchor="n")

    # CALCULE DE L'IMC
    def calculimc(self):
        print("Weight :" + str(self.weight.get()))
        print("Height :" + str(self.vHeight.get()))
        print("vAge :" + str(self.vAge.get()))
        print("sexe_var :" + str(self.sexe_var.get()))
        self.imc_var = round(self.weight.get()
                             / ((self.vHeight.get() / 100) ** 2), 2)
        print("imc_var :" + str(self.imc_var))
        pass


def main():
    root = Tk()
    ContactManager(root)
    root.geometry('1080x720+400+150')
    root.mainloop()


# EXECUTER LE SCRIPT
if __name__ == '__main__':
    main()
