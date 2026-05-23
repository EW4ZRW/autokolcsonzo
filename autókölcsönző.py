from abc import ABC
from datetime import datetime



class Auto(ABC):

    def __init__(self, rendszam, tipus, berleti_dij):

        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij

    def get_rendszam(self):
        return self._rendszam

    def get_tipus(self):
        return self._tipus

    def get_berleti_dij(self):
        return self._berleti_dij




class Szemelyauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, ulesek_szama):

        super().__init__(rendszam, tipus, berleti_dij)

        self._ulesek_szama = ulesek_szama




class Teherauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):

        super().__init__(rendszam, tipus, berleti_dij)

        self._teherbiras = teherbiras



class Berles:

    def __init__(self, auto, datum):

        self._auto = auto
        self._datum = datum

    def get_auto(self):
        return self._auto

    def get_datum(self):
        return self._datum




class Autokolcsonzo:

    def __init__(self, nev):

        self._nev = nev
        self._autok = []
        self._berlesek = []

  

    def auto_hozzaad(self, auto):

        self._autok.append(auto)

   

    def autok_listazasa(self):

        print("\nELÉRHETŐ AUTÓK:\n")

        for auto in self._autok:

            print(
                f"{auto.get_tipus()} | "
                f"{auto.get_rendszam()} | "
                f"{auto.get_berleti_dij()} Ft/nap"
            )

    

    def datum_ellenorzes(self, datum):

        try:

            datetime.strptime(datum, "%Y.%m.%d")

            return True

        except ValueError:

            return False

    

    def berles(self, rendszam, datum):

        if not self.datum_ellenorzes(datum):

            raise Exception(
                "Hibás dátumformátum! "
                "Használj ilyet: YYYY.MM.DD"
            )

        for auto in self._autok:

            if auto.get_rendszam() == rendszam:

                for berles in self._berlesek:

                    if berles.get_auto().get_rendszam() == rendszam and berles.get_datum() == datum:

                        raise Exception(
                            "Ez az autó már foglalt!"
                        )

                uj_berles = Berles(auto, datum)

                self._berlesek.append(uj_berles)

                return auto.get_berleti_dij()

        raise Exception("Nincs ilyen rendszámú autó!")

    

    def berles_lemondas(self, rendszam, datum):

        for berles in self._berlesek:

            if berles.get_auto().get_rendszam() == rendszam and berles.get_datum() == datum:

                self._berlesek.remove(berles)

                return True

        raise Exception("Nincs ilyen bérlés!")

    

    def berlesek_listazasa(self):

        if not self._berlesek:

            print("\nNincs aktív bérlés.")

            return

        print("\nAKTUÁLIS BÉRLÉSEK:\n")

        for berles in self._berlesek:

            print(
                f"{berles.get_auto().get_tipus()} | "
                f"{berles.get_auto().get_rendszam()} | "
                f"{berles.get_datum()}"
            )




def menu():

    print("\n AUTÓKÖLCSÖNZŐ ")
    print("1 - Autók listázása")
    print("2 - Autó bérlése")
    print("3 - Bérlés lemondása")
    print("4 - Bérlések listázása")
    print("0 - Kilépés")




kolcsonzo = Autokolcsonzo("SpeedCar")



auto1 = Szemelyauto(
    "ABC123",
    "Toyota Corolla",
    12000,
    5
)

auto2 = Szemelyauto(
    "DEF456",
    "BMW X5",
    18000,
    5
)

auto3 = Teherauto(
    "GHI789",
    "Ford Transit",
    25000,
    1200
)


kolcsonzo.auto_hozzaad(auto1)
kolcsonzo.auto_hozzaad(auto2)
kolcsonzo.auto_hozzaad(auto3)



kolcsonzo.berles("ABC123", "2026.05.10")
kolcsonzo.berles("DEF456", "2026.05.11")
kolcsonzo.berles("GHI789", "2026.05.12")
kolcsonzo.berles("ABC123", "2026.05.13")



while True:

    menu()

    valasztas = input("\nVálassz menüpontot: ")

    try:

      

        if valasztas == "1":

            kolcsonzo.autok_listazasa()

        

        elif valasztas == "2":

            rendszam = input("Rendszám: ")

            datum = input("Dátum (YYYY.MM.DD): ")

            ar = kolcsonzo.berles(rendszam, datum)

            print("\nSikeres bérlés!")

            print(f"Fizetendő: {ar} Ft")

    

        elif valasztas == "3":

            rendszam = input("Rendszám: ")

            datum = input("Dátum (YYYY.MM.DD): ")

            kolcsonzo.berles_lemondas(rendszam, datum)

            print("\nBérlés lemondva!")

       

        elif valasztas == "4":

            kolcsonzo.berlesek_listazasa()

       

        elif valasztas == "0":

            print("\nKilépés...")

            break

        else:

            print("\nÉrvénytelen menüpont!")

    except Exception as hiba:

        print("\nHIBA:", hiba)