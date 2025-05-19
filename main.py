          from tkinter import *




          root = Tk()
          root.geometry("1200x760")
          root.title("Map Book MK2")



          ramka_lista_obiektow=Frame(root)
          ramka_formularz=Frame(root)
          ramka_szczegoly_obiektow=Frame(root)
          ramka_mapa=Frame(root)

          ramka_lista_obiektow.grid(row=0, column=0)
          ramka_formularz.grid(row=0, column=0)
          ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
          ramka_mapa.grid(row=2, column=0,columnspan=2)

          # ramka_lista_obiektów
          label_lista_obiektow=Label(ramka_lista_obiektow, text="lista użytkowników")
          label_lista_obiektow.grid(row=0, column=0, columnspan=2)
          listbox_lista_obiektow=Listbox(ramka_lista_obiektow, width=50, height=10)
          listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
          button_pokaz_szczegoly_obiektow=Button(ramka_lista_obiektow, text="Pokaż szczegóły")
          button_pokaz_szczegoly_obiektow.grid(row=2, column=0,)
          button_usun_obiekt=Button(ramka_lista_obiektow, text="Usuń obiekt")
          button_usun_obiekt.grid(row=2, column=1)
          button_edytuj_obiekt=Button(ramka_lista_obiektow, text="Edytuj obiekt")
          button_edytuj_obiekt.grid(row=2, column=2)

          #ramka formularz
          label_formularz=Label(ramka_mapa, text="Formularz")
          label_formularz.grid(row=0, column=0, columnspan=2)
          label_name=Label(ramka_mapa, text="Name")
          label_name.grid(row=1, column=0, sticky=W)
          label_surname=Label(ramka_mapa, text="Surname")
          label_surname.grid(row=2, column=0, sticky=W)
          label_location=Label(ramka_mapa, text="Location")
          label_location.grid(row=3, column=0, sticky=W)
          label_posts=Label(ramka_mapa, text="Posts")
          label_posts.grid(row=4, column=0, sticky=W)

          entry_name=Entry(ramka_formularz)
          entry_name.grid(row=1, column=1)
          entry_surname=Entry(ramka_formularz)
          entry_surname.grid(row=2, column=1)
          entry_location=Entry(ramka_formularz)
          entry_location.grid(row=3, column=1)
          entry_posts=Entry(ramka_formularz)
          entry_posts.grid(row=4, column=1)

          button_dodaj_obiekt=Button(ramka_formularz, text="Dodaj obiekt")
          button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

          #ramka_szczegoly_obiektu
          label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="szczegoly obiektu:")
          label_szczegoly_obiektow.grid(row=0, column=0,)
          label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Imię:")
          label_szczegoly_name.grid(row=1, column=0,)
          label_szczegoly_name=Label(ramka_szczegoly_obiektow, text=".....")
          label_szczegoly_name.grid(row=1, column=0,)









