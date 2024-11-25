import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "#61A707"
    page.window_width = 650
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    img_height = 100
    img_width = 100
    border_radius = 25 # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)
    
    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
    
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()
        
    
    # Botones Padres de la informática con imágenes y etiquetas semánticas
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14= ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)
    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
    
    # Vista de portada
    if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]
                                    ),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
    # Vista de los padres de la informática
    elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                    alignment="center",
                                    controls=[
                                        btn5, btn6, btn7,btn8
                                    ]  
                                    ),
                                    ft.Row(
                                    alignment="center",
                                        controls=[
                                        btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                        btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                        btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                    ElevatedButton(
                                        'Padres de la informatica y sus lenguajes',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )




    #Audios Ramas de la informatica 
    intro_ramas = ft.Audio(src="Intro_ramas.mp3", volume=1, balance=0)
    page.overlay.append(intro_ramas) 
    
    Ramas_Informatica = ft.Audio(src="Ramas_Informatica.mp3", volume=1, balance=0)
    page.overlay.append(Ramas_Informatica)
    
    Inteligencia_artificial = ft.Audio(src="Inteligencia_Artificial.mp3", volume=1, balance=0)
    page.overlay.append(Inteligencia_artificial)
    
    Realidad_virtual = ft.Audio(src="Realidad_virtual.mp3", volume=1, balance=0)
    page.overlay.append(Realidad_virtual)
    
    Robotica = ft.Audio(src="Robotica.mp3", volume=1, balance=0)
    page.overlay.append(Robotica)
    
    Cibernetica = ft.Audio(src="cibernetica.mp3", volume=1, balance=0)
    page.overlay.append(Cibernetica)
    
    Telematica = ft.Audio(src="Telematica.mp3", volume=1, balance=0)
    page.overlay.append(Telematica)
    
    Ofimatica = ft.Audio(src="Ofimatica.mp3", volume=1, balance=0)
    page.overlay.append(Ofimatica)
    
    def StopAll():
        intro_ramas.pause()
        Ramas_Informatica.pause()
        Inteligencia_artificial.pause()
        Realidad_virtual.pause()
        Robotica.pause()
        Cibernetica.pause()
        Telematica.pause()
        Ofimatica.pause()
        
    def play_Intro_ramas(e):
        StopAll()
        intro_ramas.play()
        
    def play_Ramas_Informatica(e):
        StopAll()
        Ramas_Informatica.play()
        
    def play_Inteligencia_artificial(e):
        StopAll()
        Inteligencia_artificial.play()
        
    def play_Realidad_virtual(e):
        StopAll()
        Realidad_virtual.play()
        
    def play_Robotica(e):
        StopAll()
        Robotica.play()
        
    def play_Cibernetica(e):
        StopAll()
        Cibernetica.play()
    
    def play_Telematica(e):
        StopAll()
        Telematica.play()

    def play_Ofimatica(e):
        StopAll()
        Ofimatica.play()

    #Botones Ramas de la Informatica
    btn1 = ElevatedButton(content=ft.Image(src="Inteligencia_artificial.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Inteligencia Artificial"), on_click=play_Inteligencia_artificial)
    btn2 = ElevatedButton(content=ft.Image(src="realidad_virtual.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Realidad Virtual"), on_click=play_Realidad_virtual)
    btn3 = ElevatedButton(content=ft.Image(src="robotica.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Robotica"), on_click=play_Robotica)
    btn4 = ElevatedButton(content=ft.Image(src="cibernetica.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Cibernetica"), on_click=play_Cibernetica)
    btn5 = ElevatedButton(content=ft.Image(src="telematica.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Telematica"), on_click=play_Telematica)
    btn6 = ElevatedButton(content=ft.Image(src="ofimatica.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ofimatica"), on_click=play_Ofimatica)

     # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
     # Vista de las Ramas de la Informatica
    if page.route == '/ramas':
            page.views.append(
                View(
                    "/ramas",
                    controls=[
                        AppBar(
                            title=ft.Text("Ramas de la informatica"),
                            bgcolor="green"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn4, btn5, btn6
                                      ]  
                                    ),
                                     ElevatedButton(
                                        'Ramas de la informatica',
                                        on_click=lambda _: page.go('/ramas')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )

        

 # Audios Historia de las computadoras
    Intro_compu = ft.Audio(src="Intro_compu.mp3", volume=1, balance=0)
    page.overlay.append(Intro_compu)
    
    Quinientosac = ft.Audio(src="500_a.C.mp3", volume=1, balance=0)
    page.overlay.append(Quinientosac)
    
    Mil614 = ft.Audio(src="1614.mp3", volume=1, balance=0)
    page.overlay.append(Mil614)
    
    Mil620 = ft.Audio(src="1620.mp3", volume=1, balance=0)
    page.overlay.append(Mil620)
    
    Mil623 = ft.Audio(src="1623.mp3", volume=1, balance=0) 
    page.overlay.append(Mil623)
    
    Mil642 = ft.Audio(src="1642.mp3", volume=1, balance=0)
    page.overlay.append(Mil642 )
    
    Mil671 = ft.Audio(src="1671.mp3", volume=1, balance=0)
    page.overlay.append(Mil671)
    
    Mil801 = ft.Audio(src="1801.mp3", volume=1, balance=0)
    page.overlay.append(Mil801)
     
    Mil833 = ft.Audio(src="1833.mp3", volume=1, balance=0)
    page.overlay.append(Mil833)
    
    Mil841 = ft.Audio(src="1841.mp3", volume=1, balance=0)
    page.overlay.append(Mil841)
    
    Mil893 = ft.Audio(src="1893.mp3", volume=1, balance=0)
    page.overlay.append(Mil893)
    
    Mil938 = ft.Audio(src="1938.mp3", volume=1, balance=0)
    page.overlay.append(Mil938)
    
    Mil944 = ft.Audio(src="Mil944.mp3", volume=1, balance=0)
    page.overlay.append(Mil944)
    
    Mil949 = ft.Audio(src="1949.mp3", volume=1, balance=0)
    page.overlay.append(Mil949)
    
    Mil950 = ft.Audio(src="1950.mp3", volume=1, balance=0)
    page.overlay.append(Mil950)

    Mil951 = ft.Audio(src="1951.mp3", volume=1, balance=0)
    page.overlay.append(Mil951)

    Mil953 = ft.Audio(src="1953.mp3", volume=1, balance=0)
    page.overlay.append(Mil953)

    Mil961 = ft.Audio(src="1961.mp3", volume=1, balance=0)
    page.overlay.append(Mil961)

    Mil964 = ft.Audio(src="1964.mp3", volume=1, balance=0)
    page.overlay.append(Mil964)

    Mil971 = ft.Audio(src="1971.mp3", volume=1, balance=0)
    page.overlay.append(Mil971)

    Mil975 = ft.Audio(src="1975.mp3", volume=1, balance=0)
    page.overlay.append(Mil975)

    Mil976 = ft.Audio(src="1976.mp3", volume=1, balance=0)
    page.overlay.append(Mil976)
    
    Mil977 = ft.Audio(src="1977.mp3", volume=1, balance=0)
    page.overlay.append(Mil977)
    
    Mil981 = ft.Audio(src="1981.mp3", volume=1, balance=0)
    page.overlay.append(Mil981)
    
    Mil982 = ft.Audio(src="1982.mp3", volume=1, balance=0)
    page.overlay.append(Mil982)
    
    Mil983 = ft.Audio(src="1983.mp3", volume=1, balance=0)
    page.overlay.append(Mil983)
    
    Mil990 = ft.Audio(src="1990.mp3", volume=1, balance=0)
    page.overlay.append(Mil990)
    
    DosMil = ft.Audio(src="2000.mp3", volume=1, balance=0)
    page.overlay.append(DosMil)
    
    DosMil7 = ft.Audio(src="2007.mp3", volume=1, balance=0)
    page.overlay.append(DosMil7)

    def StopAll():
        Intro_compu.pause()
        Quinientosac.pause()
        Mil614.pause()
        Mil620.pause()
        Mil623.pause()
        Mil642.pause()
        Mil671.pause()
        Mil801.pause()
        Mil833.pause()
        Mil841.pause()
        Mil893.pause()
        Mil938.pause()
        Mil944.pause()
        Mil949.pause()
        Mil950.pause()
        Mil951.pause()
        Mil953.pause()
        Mil961.pause()
        Mil964.pause()
        Mil971.pause()
        Mil975.pause()
        Mil976.pause()
        Mil977.pause()
        Mil981.pause()
        Mil982.pause()
        Mil983.pause()
        Mil990.pause()
        DosMil.pause()
        DosMil7.pause()
    
    def play_Intro_compu(e):
        StopAll()
        Intro_compu.play()
        
    def play_Quinientosac(e):
        StopAll()
        Quinientosac.play()
        
    def play_Mil614(e):
        StopAll()
        Mil614.play()
        
    def play_Mil620(e):
        StopAll()
        Mil620.play()
        
    def play_Mil623(e):    
        StopAll()
        Mil623.play()
        
    def play_Mil642(e):
        StopAll()
        Mil642.play()
        
    def play_Mil671(e):
        StopAll()
        Mil671.play()
    
    def play_Mil801(e):
        StopAll()
        Mil801.play()
        
    def play_Mil833(e):
        StopAll()
        Mil833.play()
    
    def play_Mil841(e):
        StopAll()
        Mil841.play()
    
    def play_Mil893(e):
        StopAll()
        Mil893.play()
    
    def play_Mil938(e):
        StopAll()
        Mil938.play()
    
    def play_Mil944(e):
        StopAll()
        Mil944.play()
        
    def play_Mil949(e):
        StopAll()
        Mil949.play()
        
    def play_Mil950(e):
        StopAll()
        Mil950.play()
        
    def play_Mil951(e):
        StopAll()
        Mil951.play()
        
    def play_Mil953(e):
        StopAll()
        Mil953.play()
        
    def play_Mil961(e):
        StopAll()
        Mil961.play()
    
    def play_Mil964(e):
        StopAll()
        Mil964.play()
    
    def play_Mil971(e):
        StopAll()
        Mil971.play()
    
    def play_Mil975(e):
        StopAll()
        Mil975.play()

    def play_Mil975(e):
        StopAll()
        Mil975.play()
    
    def play_Mil976(e):
        StopAll()
        Mil976.play()

    def play_Mil977(e):
        StopAll()
        Mil977.play()
    
    def play_Mil981(e):
        StopAll()
        Mil981.play()

    def play_Mil982(e):
        StopAll()
        Mil982.play()
    
    def play_Mil983(e):
        StopAll()
        Mil983.play()

    def play_Mil990(e):
        StopAll()
        Mil990.play()
    
    def play_DosMil(e):
        StopAll()
        DosMil.play()

    def play_DosMil17(e):
        StopAll()
        DosMil7.play()

    
    # Botones Historia de la informatica
    btn1 = ElevatedButton(content=ft.Image(src="500a.C.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="500a.C"), on_click=play_Quinientosac)
    btn2 = ElevatedButton(content=ft.Image(src="1614.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1614"), on_click=play_Mil614)
    btn3 = ElevatedButton(content=ft.Image(src="1620.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1620"), on_click=play_Mil620)
    btn4 = ElevatedButton(content=ft.Image(src="1623.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1623"), on_click=play_Mil623)
    btn5 = ElevatedButton(content=ft.Image(src="1642.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1642"), on_click=play_Mil642)
    btn6 = ElevatedButton(content=ft.Image(src="1671.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1671"), on_click=play_Mil671)
    btn7 = ElevatedButton(content=ft.Image(src="1801.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1801"), on_click=play_Mil801)
    btn8 = ElevatedButton(content=ft.Image(src="1833.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1833"), on_click=play_Mil833)
    btn9 = ElevatedButton(content=ft.Image(src="1841.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1841"), on_click=play_Mil841)
    btn10 = ElevatedButton(content=ft.Image(src="1893.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1893"), on_click=play_Mil893)
    btn11 = ElevatedButton(content=ft.Image(src="1938.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1938"), on_click=play_Mil938)
    btn12 = ElevatedButton(content=ft.Image(src="1944.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1944"), on_click=play_Mil944)
    btn13 = ElevatedButton(content=ft.Image(src="1949.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1949"), on_click=play_Mil949)
    btn14 = ElevatedButton(content=ft.Image(src="1950.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1950"), on_click=play_Mil950)
    btn15 = ElevatedButton(content=ft.Image(src="1951.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1951"), on_click=play_Mil951)
    btn16 = ElevatedButton(content=ft.Image(src="1953.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1953"), on_click=play_Mil953)
    btn17 = ElevatedButton(content=ft.Image(src="1961.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1961"), on_click=play_Mil961)
    btn18 = ElevatedButton(content=ft.Image(src="1964.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1964"), on_click=play_Mil964)
    btn19 = ElevatedButton(content=ft.Image(src="1971.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1971"), on_click=play_Mil971)
    btn20 = ElevatedButton(content=ft.Image(src="1975.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1975"), on_click=play_Mil975)
    btn21 = ElevatedButton(content=ft.Image(src="1976.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1976"), on_click=play_Mil976)
    btn22 = ElevatedButton(content=ft.Image(src="1977.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1977"), on_click=play_Mil977)
    btn23 = ElevatedButton(content=ft.Image(src="1981.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1981"), on_click=play_Mil981)
    btn24 = ElevatedButton(content=ft.Image(src="1982.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1982"), on_click=play_Mil982)
    btn25 = ElevatedButton(content=ft.Image(src="1983.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1983"), on_click=play_Mil983)
    btn26 = ElevatedButton(content=ft.Image(src="1990.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="1990"), on_click=play_Mil990)
    btn27 = ElevatedButton(content=ft.Image(src="2000.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="2000"), on_click=play_DosMil)
    btn28 = ElevatedButton(content=ft.Image(src="2007.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="2007"), on_click=play_DosMil17)
    
# Vista de la historia de la informatica
    if page.route == '/historia':
            page.views.append(
                View(
                    "/historia",
                    controls=[
                        AppBar(
                            title=ft.Text("Historia de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                    alignment="center",
                                    controls=[
                                        btn5, btn6, btn7,btn8
                                    ]  
                                    ),
                                    ft.Row(
                                    alignment="center",
                                        controls=[
                                        btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                        btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                        btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn21, btn22, btn23, btn24
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn25, btn26, btn27, btn28
                                        ]
                                    ),
                                    ElevatedButton(
                                        'La historia de las computadoras',
                                        on_click=lambda _: page.go('/computadoras')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )



    #Audios de las redes sociales 

    Introducción= ft.Audio(src="Introducción.mp3", volume=1, balance=0)
    page.overlay.append(Introducción)

    Calculadora= ft.Audio(src="Calculadora.mp3", volume=1, balance=0)
    page.overlay.append(Calculadora)

    Canva= ft.Audio(src="Canva.mp3", volume=1, balance=0)
    page.overlay.append(Canva)    

    Configuración = ft.Audio(src="Configuración.mp3", volume=1, balance=0)
    page.overlay.append(Configuración)

    Facebook = ft.Audio(src="Facebook.mp3", volume=1, balance=0)
    page.overlay.append(Facebook)

    Gmail = ft.Audio(src="Gmail.mp3", volume=1, balance=0)
    page.overlay.append(Gmail)

    GooglePlay = ft.Audio(src="GooglePlay.mp3", volume=1, balance=0)
    page.overlay.append(GooglePlay)

    Google = ft.Audio(src="Google.mp3", volume=1, balance=0)
    page.overlay.append(Google)

    Instagram = ft.Audio(src="Instagram.mp3", volume=1, balance=0)
    page.overlay.append(Instagram)

    Netflix = ft.Audio(src="Netflix.mp3", volume=1, balance=0)
    page.overlay.append(Netflix)

    Notas = ft.Audio(src="Notas.mp3", volume=1, balance=0)
    page.overlay.append(Notas)

    Visual = ft.Audio(src="Visual.mp3", volume=1, balance=0)
    page.overlay.append(Visual)

    Whatsapp = ft.Audio(src="Whatsapp.mp3", volume=1, balance=0)
    page.overlay.append(Whatsapp)

    Pinterest = ft.Audio(src="Pinterest.mp3", volume=1, balance=0)
    page.overlay.append(Pinterest)

    Tiktok = ft.Audio(src="Tiktok.mp3", volume=1, balance=0)
    page.overlay.append(Tiktok)

    Twitter = ft.Audio(src="Twitter.mp3", volume=1, balance=0)
    page.overlay.append(Twitter)

    Uber = ft.Audio(src="Uber.mp3", volume=1, balance=0)
    page.overlay.append(Uber)

    def StopAll():
        Introducción.pause()
        Calculadora.pause()
        Canva.pause()
        Configuración.pause()
        Facebook.pause()
        Gmail.pause()
        GooglePlay.pause()
        Google.pause()
        Instagram.pause()
        Netflix.pause()
        Notas.pause()
        Pinterest.pause()
        Tiktok.pause()
        Twitter.pause()
        Uber.pause()
        Visual.pause()
        Whatsapp.pause()

    def play_Introducción(e):
        StopAll()
        Introducción.play()
    
        
    def play_Calculadora(e):
        StopAll()
        Calculadora.play()

    def play_Canva(e):
        StopAll()
        Canva.play()

    def play_Configuración(e):
        StopAll()
        Configuración.play()

    def play_Facebook(e):
        StopAll()
        Facebook.play()

    def play_Gmail(e):
        StopAll()
        Gmail.play()

    def play_GooglePlay(e):
        StopAll()
        GooglePlay.play()

    def play_Google(e):
        StopAll()
        Google.play()

    def play_Instagram(e):
        StopAll()
        Instagram.play()

    def play_Netflix(e):
        StopAll()
        Netflix.play()

    def play_Notas(e):
        StopAll()
        Notas.play()

    def play_Pinterest(e):
        StopAll()
        Pinterest.play()

    def play_Tiktok(e):
        StopAll()
        Tiktok.play()

    def play_Twitter(e):
        StopAll()
        Twitter.play()

    def play_Uber(e):
        StopAll()
        Uber.play()

    def play_Visual(e):
        StopAll()
        Visual.play()

    def play_Whatsapp(e):
        StopAll()
        Whatsapp.play()

 # Botones Aplicaciones 
    btn1 = ElevatedButton(content=ft.Image(src="Calculadora.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Calculadora"), on_click=play_Calculadora)
    btn2 = ElevatedButton(content=ft.Image(src="Canva.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Canva"), on_click=play_Canva)
    btn3 = ElevatedButton(content=ft.Image(src="Configuración.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Configuración"), on_click=play_Configuración)
    btn4 = ElevatedButton(content=ft.Image(src="Facebook.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Facebook"), on_click=play_Facebook)
    btn5 = ElevatedButton(content=ft.Image(src="Gmail.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gmail"), on_click=play_Gmail)
    btn6= ElevatedButton(content=ft.Image(src="GooglePlay.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="GooglePlay"), on_click=play_GooglePlay)
    btn7 = ElevatedButton(content=ft.Image(src="Google.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Google"), on_click=play_Google)
    btn8 = ElevatedButton(content=ft.Image(src="Instagram.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Instagram"), on_click=play_Instagram)
    btn9 = ElevatedButton(content=ft.Image(src="Netflix.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Netflix"), on_click=play_Netflix)
    btn10 = ElevatedButton(content=ft.Image(src="Notas.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Notas"), on_click=play_Notas)
    btn11 = ElevatedButton(content=ft.Image(src="Pinterest.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Pinterest"), on_click=play_Pinterest)
    btn12 = ElevatedButton(content=ft.Image(src="Tiktok.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tiktok"), on_click=play_Tiktok)
    btn13 = ElevatedButton(content=ft.Image(src="Twitter.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Twitter"), on_click=play_Twitter)
    btn14 = ElevatedButton(content=ft.Image(src="Uber.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Uber"), on_click=play_Uber)
    btn15 = ElevatedButton(content=ft.Image(src="Visual.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Visual"), on_click=play_Visual)
    btn16 = ElevatedButton(content=ft.Image(src="Whatsapp.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Whatsapp"), on_click=play_Whatsapp)
    
    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
            
    # Vista de las aplicaciones
    if page.route == '/aplicaciones':
            page.views.append(
                View(
                    "/aplicaciones",
                    controls=[
                        AppBar(
                            title=ft.Text("Las aplicaciones"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="asset
