# seed.py
from app import create_app, db
from app.models import Usuario, Libro, Cliente
from werkzeug.security import generate_password_hash

def seed_database():
    app = create_app()
    with app.app_context():
        
        # Limpiar datos existentes (opcional)
        # db.drop_all()
        # db.create_all()
        
        # Verificar si ya hay datos
        #if Usuario.query.first():
        #    print("La base de datos ya tiene datos. Usa --force para forzar la reinserción.")
        #    return
        
        # Insertar usuarios
        usuarios = [
            Usuario(
                usuario='admin2',
                password=generate_password_hash('admin123'),
                email='admin@empresa.com',
                nombre_completo='Administrador Sistema',
                rol='admin'
            ),
            Usuario(
                usuario='gerente1',
                password=generate_password_hash('gerente123'),
                email='gerente@empresa.com',
                nombre_completo='Gerente General',
                rol='gerente'
            ),
            Usuario(
                usuario='vendedor1',
                password=generate_password_hash('vendedor123'),
                email='vendedor@empresa.com',
                nombre_completo='Vendedor Principal',
                rol='vendedor'
            )
        ]
        # ==================== LIBROS (50 registros) ====================
        libros = [
            # Clásicos de la literatura
            Libro(
                isbn='978-0307476463',
                titulo='Cien Años de Soledad',
                autor='Gabriel García Márquez',
                editorial='Sudamericana',
                anio_publicacion=1967,
                genero='Realismo mágico',
                precio=45000.00,
                stock=25,
                descripcion='La obra maestra del premio Nobel colombiano. La historia de la familia Buendía en Macondo.',
                paginas=471,
                idioma='Español'
            ),
            Libro(
                isbn='978-0061120084',
                titulo='1984',
                autor='George Orwell',
                editorial='Debolsillo',
                anio_publicacion=1949,
                genero='Ciencia ficción/Distopía',
                precio=35000.00,
                stock=30,
                descripcion='La clásica novela distópica sobre un futuro totalitario y la vigilancia masiva.',
                paginas=368,
                idioma='Español'
            ),
            Libro(
                isbn='978-8497592208',
                titulo='El Principito',
                autor='Antoine de Saint-Exupéry',
                editorial='Salamandra',
                anio_publicacion=1943,
                genero='Infantil/Fábula',
                precio=28000.00,
                stock=45,
                descripcion='Un piloto perdido en el desierto conoce a un pequeño príncipe de otro planeta.',
                paginas=96,
                idioma='Español'
            ),
            Libro(
                isbn='978-8497592451',
                titulo='Don Quijote de la Mancha',
                autor='Miguel de Cervantes',
                editorial='Real Academia Española',
                anio_publicacion=1605,
                genero='Novela',
                precio=65000.00,
                stock=15,
                descripcion='La obra cumbre de la literatura española. Las aventuras del ingenioso hidalgo.',
                paginas=1345,
                idioma='Español'
            ),
            Libro(
                isbn='978-8491052807',
                titulo='La Divina Comedia',
                autor='Dante Alighieri',
                editorial='Penguin Clásicos',
                anio_publicacion=1320,
                genero='Poesía épica',
                precio=55000.00,
                stock=12,
                descripcion='El viaje de Dante a través del Infierno, el Purgatorio y el Paraíso.',
                paginas=672,
                idioma='Español'
            ),
            
            # Novelas contemporáneas
            Libro(
                isbn='978-8498387087',
                titulo='El Alquimista',
                autor='Paulo Coelho',
                editorial='Planeta',
                anio_publicacion=1988,
                genero='Novela/Filosofía',
                precio=42000.00,
                stock=38,
                descripcion='Un joven pastor andaluz viaja a Egipto en busca de un tesoro y descubre su leyenda personal.',
                paginas=192,
                idioma='Español'
            ),
            Libro(
                isbn='978-9875663172',
                titulo='La Sombra del Viento',
                autor='Carlos Ruiz Zafón',
                editorial='Planeta',
                anio_publicacion=2001,
                genero='Misterio/Drama',
                precio=48000.00,
                stock=22,
                descripcion='Un joven encuentra un libro maldito que cambiará su vida y lo llevará a desentrañar un secreto.',
                paginas=576,
                idioma='Español'
            ),
            Libro(
                isbn='978-8490622359',
                titulo='El Código Da Vinci',
                autor='Dan Brown',
                editorial='Planeta',
                anio_publicacion=2003,
                genero='Suspenso/Misterio',
                precio=46000.00,
                stock=28,
                descripcion='Robert Langdon descubre una conspiración que podría cambiar la historia del cristianismo.',
                paginas=656,
                idioma='Español'
            ),
            Libro(
                isbn='978-8490321498',
                titulo='Los Pilares de la Tierra',
                autor='Ken Follett',
                editorial='Plaza & Janés',
                anio_publicacion=1989,
                genero='Novela histórica',
                precio=75000.00,
                stock=18,
                descripcion='La construcción de una catedral gótica en la Inglaterra medieval del siglo XII.',
                paginas=1200,
                idioma='Español'
            ),
            Libro(
                isbn='978-8401337208',
                titulo='La Chica del Tren',
                autor='Paula Hawkins',
                editorial='Planeta',
                anio_publicacion=2015,
                genero='Thriller psicológico',
                precio=44000.00,
                stock=32,
                descripcion='Una mujer observa desde el tren una escena que desencadena una investigación policial.',
                paginas=496,
                idioma='Español'
            ),
            
            # Ciencia ficción y fantasía
            Libro(
                isbn='978-8445071409',
                titulo='El Señor de los Anillos: La Comunidad del Anillo',
                autor='J.R.R. Tolkien',
                editorial='Minotauro',
                anio_publicacion=1954,
                genero='Fantasía épica',
                precio=68000.00,
                stock=20,
                descripcion='Frodo Bolsón emprende la misión de destruir el Anillo Único en las tierras de Mordor.',
                paginas=576,
                idioma='Español'
            ),
            Libro(
                isbn='978-8498382679',
                titulo='Harry Potter y la Piedra Filosofal',
                autor='J.K. Rowling',
                editorial='Salamandra',
                anio_publicacion=1997,
                genero='Fantasía',
                precio=49000.00,
                stock=50,
                descripcion='El niño que vivió descubre que es un mago y entra al Colegio Hogwarts.',
                paginas=256,
                idioma='Español'
            ),
            Libro(
                isbn='978-8448036097',
                titulo='Fundación',
                autor='Isaac Asimov',
                editorial='Debolsillo',
                anio_publicacion=1951,
                genero='Ciencia ficción',
                precio=42000.00,
                stock=17,
                descripcion='Hari Seldon predice la caída del Imperio Galáctico y crea la Fundación para preservar el conocimiento.',
                paginas=320,
                idioma='Español'
            ),
            Libro(
                isbn='978-8445071768',
                titulo='Dune',
                autor='Frank Herbert',
                editorial='Ediciones B',
                anio_publicacion=1965,
                genero='Ciencia ficción',
                precio=65000.00,
                stock=14,
                descripcion='Paul Atreides lucha por el control del planeta desértico Arrakis, la única fuente de la especia melange.',
                paginas=896,
                idioma='Español'
            ),
            Libro(
                isbn='978-8417347007',
                titulo='Saga Ender: El Juego de Ender',
                autor='Orson Scott Card',
                editorial='Ediciones B',
                anio_publicacion=1985,
                genero='Ciencia ficción',
                precio=48000.00,
                stock=12,
                descripcion='Niños prodigio son entrenados en la Escuela de Batalla para enfrentar una invasión alienígena.',
                paginas=384,
                idioma='Español'
            ),
            
            # Libros de desarrollo personal
            Libro(
                isbn='978-8499082622',
                titulo='El Poder del Ahora',
                autor='Eckhart Tolle',
                editorial='Gaia',
                anio_publicacion=1997,
                genero='Espiritualidad/Autoayuda',
                precio=52000.00,
                stock=23,
                descripcion='Guía para la iluminación espiritual y vivir en el momento presente.',
                paginas=224,
                idioma='Español'
            ),
            Libro(
                isbn='978-0307463746',
                titulo='Padre Rico, Padre Pobre',
                autor='Robert Kiyosaki',
                editorial='Aguilar',
                anio_publicacion=1997,
                genero='Finanzas personales',
                precio=55000.00,
                stock=35,
                descripcion='Lo que los ricos enseñan a sus hijos sobre el dinero que los pobres y la clase media no.',
                paginas=336,
                idioma='Español'
            ),
            Libro(
                isbn='978-6073118480',
                titulo='Los 7 Hábitos de la Gente Altamente Efectiva',
                autor='Stephen Covey',
                editorial='Paidós',
                anio_publicacion=1989,
                genero='Autoayuda/Liderazgo',
                precio=58000.00,
                stock=27,
                descripcion='Un enfoque holístico para resolver problemas personales y profesionales.',
                paginas=432,
                idioma='Español'
            ),
            Libro(
                isbn='978-8497347585',
                titulo='El Monje que Vendió su Ferrari',
                autor='Robin Sharma',
                editorial='Debolsillo',
                anio_publicacion=1997,
                genero='Autoayuda/Espiritualidad',
                precio=46000.00,
                stock=29,
                descripcion='Una fábula espiritual sobre el autodescubrimiento y la realización personal.',
                paginas=240,
                idioma='Español'
            ),
            Libro(
                isbn='978-9588789725',
                titulo='La Guerra del Arte',
                autor='Steven Pressfield',
                editorial='Página Seis',
                anio_publicacion=2002,
                genero='Creatividad',
                precio=42000.00,
                stock=16,
                descripcion='Cómo vencer las resistencias internas que impiden alcanzar nuestro potencial creativo.',
                paginas=192,
                idioma='Español'
            ),
            
            # Literatura latinoamericana
            Libro(
                isbn='978-8497592482',
                titulo='Rayuela',
                autor='Julio Cortázar',
                editorial='Punto de Lectura',
                anio_publicacion=1963,
                genero='Novela experimental',
                precio=53000.00,
                stock=14,
                descripcion='Una novela que puede leerse de múltiples formas, historia de amor en París y Buenos Aires.',
                paginas=736,
                idioma='Español'
            ),
            Libro(
                isbn='978-8437601164',
                titulo='Pedro Páramo',
                autor='Juan Rulfo',
                editorial='Cátedra',
                anio_publicacion=1955,
                genero='Realismo mágico',
                precio=38000.00,
                stock=19,
                descripcion='Un hombre viaja a Comala en busca de su padre y encuentra un pueblo de fantasmas.',
                paginas=160,
                idioma='Español'
            ),
            Libro(
                isbn='978-8497592406',
                titulo='La Casa de los Espíritus',
                autor='Isabel Allende',
                editorial='Plaza & Janés',
                anio_publicacion=1982,
                genero='Realismo mágico',
                precio=54000.00,
                stock=21,
                descripcion='La saga de la familia Trueba a través de cuatro generaciones en un país latinoamericano.',
                paginas=560,
                idioma='Español'
            ),
            Libro(
                isbn='978-9580460123',
                titulo='Del Amor y Otros Demonios',
                autor='Gabriel García Márquez',
                editorial='Norma',
                anio_publicacion=1994,
                genero='Novela',
                precio=48000.00,
                stock=18,
                descripcion='Una niña de doce años mordida por un perro rabioso es recluida en un convento.',
                paginas=208,
                idioma='Español'
            ),
            
            # Poesía
            Libro(
                isbn='978-8499087573',
                titulo='Veinte Poemas de Amor y una Canción Desesperada',
                autor='Pablo Neruda',
                editorial='Debolsillo',
                anio_publicacion=1924,
                genero='Poesía',
                precio=32000.00,
                stock=31,
                descripcion='La obra más famosa del poeta chileno, premio Nobel de Literatura.',
                paginas=120,
                idioma='Español'
            ),
            Libro(
                isbn='978-8437600884',
                titulo='Poeta en Nueva York',
                autor='Federico García Lorca',
                editorial='Cátedra',
                anio_publicacion=1940,
                genero='Poesía',
                precio=40000.00,
                stock=15,
                descripcion='La visión surrealista de Lorca sobre la ciudad moderna y la alienación.',
                paginas=320,
                idioma='Español'
            ),
            
            # Filosofía y ensayo
            Libro(
                isbn='978-8430608424',
                titulo='Así Habló Zaratustra',
                autor='Friedrich Nietzsche',
                editorial='Taurus',
                anio_publicacion=1883,
                genero='Filosofía',
                precio=62000.00,
                stock=11,
                descripcion='La obra cumbre de Nietzsche donde expone su concepto del superhombre.',
                paginas=576,
                idioma='Español'
            ),
            Libro(
                isbn='978-8420678827',
                titulo='La República',
                autor='Platón',
                editorial='Alianza Editorial',
                anio_publicacion=-380,
                genero='Filosofía política',
                precio=58000.00,
                stock=13,
                descripcion='Diálogo sobre la justicia y el Estado ideal en la Grecia clásica.',
                paginas=704,
                idioma='Español'
            ),
            
            # Terror y misterio
            Libro(
                isbn='978-8483467860',
                titulo='It (Eso)',
                autor='Stephen King',
                editorial='Debolsillo',
                anio_publicacion=1986,
                genero='Terror',
                precio=75000.00,
                stock=20,
                descripcion='Un grupo de niños se enfrenta a una entidad maligna que toma la forma de sus peores miedos.',
                paginas=1504,
                idioma='Español'
            ),
            Libro(
                isbn='978-8497593328',
                titulo='El Resplandor',
                autor='Stephen King',
                editorial='Debolsillo',
                anio_publicacion=1977,
                genero='Terror',
                precio=55000.00,
                stock=22,
                descripcion='Una familia cuida un hotel aislado durante el invierno y despierta fuerzas sobrenaturales.',
                paginas=688,
                idioma='Español'
            ),
            Libro(
                isbn='978-8497593779',
                titulo='Drácula',
                autor='Bram Stoker',
                editorial='Debolsillo',
                anio_publicacion=1897,
                genero='Terror gótico',
                precio=46000.00,
                stock=17,
                descripcion='El conde Drácula viaja de Transilvania a Inglaterra en busca de nuevas víctimas.',
                paginas=576,
                idioma='Español'
            ),
            
            # Continuación de libros...
            Libro(
                isbn='978-8420648745',
                titulo='Ensayo sobre la Ceguera',
                autor='José Saramago',
                editorial='Alfaguara',
                anio_publicacion=1995,
                genero='Novela/Distopía',
                precio=52000.00,
                stock=16,
                descripcion='Una epidemia de ceguera blanca se extiende por una ciudad y la civilización colapsa.',
                paginas=400,
                idioma='Español'
            ),
            Libro(
                isbn='978-9877383283',
                titulo='El Túnel',
                autor='Ernesto Sábato',
                editorial='Booket',
                anio_publicacion=1948,
                genero='Novela psicológica',
                precio=38000.00,
                stock=14,
                descripcion='Un pintor obsesionado con una mujer confiesa haberla asesinado.',
                paginas=160,
                idioma='Español'
            ),
            Libro(
                isbn='978-8433972895',
                titulo='2666',
                autor='Roberto Bolaño',
                editorial='Anagrama',
                anio_publicacion=2004,
                genero='Novela',
                precio=95000.00,
                stock=8,
                descripcion='Cinco partes interconectadas que exploran la violencia y el mal en el siglo XX.',
                paginas=1152,
                idioma='Español'
            ),
            Libro(
                isbn='978-8420425487',
                titulo='La Ciudad y los Perros',
                autor='Mario Vargas Llosa',
                editorial='Alfaguara',
                anio_publicacion=1963,
                genero='Novela',
                precio=52000.00,
                stock=15,
                descripcion='La vida en un colegio militar limeño y sus códigos de violencia y honor.',
                paginas=488,
                idioma='Español'
            ),
        ]
        
        # ==================== CLIENTES (50 registros) ====================
        clientes = [
            # Clientes de Bogotá
            Cliente(
                nombre='Juan',
                apellido='Pérez',
                email='juan.perez@gmail.com',
                telefono='3001234567',
                direccion='Calle 45 #23-12, Chapinero, Bogotá'
            ),
            Cliente(
                nombre='María',
                apellido='González',
                email='maria.gonzalez@hotmail.com',
                telefono='3107654321',
                direccion='Carrera 15 #85-64, Usaquén, Bogotá'
            ),
            Cliente(
                nombre='Carlos',
                apellido='Rodríguez',
                email='carlos.rodriguez@yahoo.com',
                telefono='3205551234',
                direccion='Av. Chile #68B-32, Teusaquillo, Bogotá'
            ),
            Cliente(
                nombre='Ana',
                apellido='Martínez',
                email='ana.martinez@gmail.com',
                telefono='3017894561',
                direccion='Calle 100 #15-80, Usaquén, Bogotá'
            ),
            Cliente(
                nombre='Luis',
                apellido='Sánchez',
                email='luis.sanchez@empresa.com',
                telefono='3159876543',
                direccion='Diagonal 23 #37-09, Chapinero, Bogotá'
            ),
            
            # Clientes de Medellín
            Cliente(
                nombre='Laura',
                apellido='Herrera',
                email='laura.herrera@gmail.com',
                telefono='3045678901',
                direccion='Carrera 43 #30-20, El Poblado, Medellín'
            ),
            Cliente(
                nombre='Andrés',
                apellido='López',
                email='andres.lopez@hotmail.com',
                telefono='3182345678',
                direccion='Calle 10 #42-15, Laureles, Medellín'
            ),
            Cliente(
                nombre='Carolina',
                apellido='Ramírez',
                email='carolina.ramirez@yahoo.com',
                telefono='3128765432',
                direccion='Av. Las Vegas #54-12, Envigado, Medellín'
            ),
            Cliente(
                nombre='Felipe',
                apellido='Torres',
                email='felipe.torres@gmail.com',
                telefono='3165432109',
                direccion='Calle 7 #65-40, Belén, Medellín'
            ),
            Cliente(
                nombre='Daniela',
                apellido='Ospina',
                email='daniela.ospina@empresa.com',
                telefono='3209876543',
                direccion='Carrera 70 #44-30, Laureles, Medellín'
            ),
            
            # Clientes de Cali
            Cliente(
                nombre='Javier',
                apellido='Molina',
                email='javier.molina@gmail.com',
                telefono='3024567890',
                direccion='Av. 6 Norte #23-45, Granada, Cali'
            ),
            Cliente(
                nombre='Patricia',
                apellido='Castro',
                email='patricia.castro@hotmail.com',
                telefono='3177891234',
                direccion='Carrera 100 #5-80, Ciudad Jardín, Cali'
            ),
            Cliente(
                nombre='Diego',
                apellido='Muñoz',
                email='diego.munoz@yahoo.com',
                telefono='3103456789',
                direccion='Calle 14 #95-32, San Fernando, Cali'
            ),
            Cliente(
                nombre='Valentina',
                apellido='Restrepo',
                email='valentina.restrepo@gmail.com',
                telefono='3134567890',
                direccion='Av. Pasoancho #56-78, Tequendama, Cali'
            ),
            Cliente(
                nombre='Santiago',
                apellido='Giraldo',
                email='santiago.giraldo@empresa.com',
                telefono='3198765432',
                direccion='Carrera 38 #29-15, El Ingenio, Cali'
            ),
            
            # Clientes de Barranquilla
            Cliente(
                nombre='Camila',
                apellido='Fernández',
                email='camila.fernandez@gmail.com',
                telefono='3056789012',
                direccion='Calle 79 #45-23, El Prado, Barranquilla'
            ),
            Cliente(
                nombre='Ricardo',
                apellido='Jiménez',
                email='ricardo.jimenez@hotmail.com',
                telefono='3012345678',
                direccion='Carrera 51 #80-90, Alto Prado, Barranquilla'
            ),
            Cliente(
                nombre='Alejandra',
                apellido='Mendoza',
                email='alejandra.mendoza@yahoo.com',
                telefono='3167890123',
                direccion='Calle 82 #48-67, Riomar, Barranquilla'
            ),
            Cliente(
                nombre='Oscar',
                apellido='Peña',
                email='oscar.pena@gmail.com',
                telefono='3123456789',
                direccion='Av. Circunvalar #15-34, Buenavista, Barranquilla'
            ),
            
            # Clientes de Cartagena
            Cliente(
                nombre='Tatiana',
                apellido='Blanco',
                email='tatiana.blanco@gmail.com',
                telefono='3181234567',
                direccion='Calle del Curato #34-12, Centro Histórico, Cartagena'
            ),
            Cliente(
                nombre='Roberto',
                apellido='Navarro',
                email='roberto.navarro@hotmail.com',
                telefono='3145678901',
                direccion='Av. San Martín #7-89, Bocagrande, Cartagena'
            ),
            Cliente(
                nombre='Marcela',
                apellido='Díaz',
                email='marcela.diaz@yahoo.com',
                telefono='3192345678',
                direccion='Carrera 2 #15-67, Castillo Grande, Cartagena'
            ),
            
            # Más clientes diversos
            Cliente(
                nombre='Gustavo',
                apellido='Álvarez',
                email='gustavo.alvarez@gmail.com',
                telefono='3101122334',
                direccion='Calle 30 #20-15, Bucaramanga'
            ),
            Cliente(
                nombre='Diana',
                apellido='Suárez',
                email='diana.suarez@hotmail.com',
                telefono='3172233445',
                direccion='Carrera 25 #45-78, Pereira'
            ),
            Cliente(
                nombre='Héctor',
                apellido='Rojas',
                email='hector.rojas@yahoo.com',
                telefono='3153344556',
                direccion='Av. Bolívar #12-34, Cúcuta'
            ),
            Cliente(
                nombre='Adriana',
                apellido='Mejía',
                email='adriana.mejia@gmail.com',
                telefono='3024455667',
                direccion='Calle 50 #24-90, Manizales'
            ),
            Cliente(
                nombre='Mauricio',
                apellido='Vargas',
                email='mauricio.vargas@empresa.com',
                telefono='3045566778',
                direccion='Carrera 19 #36-45, Ibagué'
            ),
            Cliente(
                nombre='Liliana',
                apellido='Cárdenas',
                email='liliana.cardenas@gmail.com',
                telefono='3126677889',
                direccion='Diagonal 15 #22-33, Pasto'
            ),
            Cliente(
                nombre='Raúl',
                apellido='Romero',
                email='raul.romero@hotmail.com',
                telefono='3197788990',
                direccion='Calle 70 #35-22, Santa Marta'
            ),
            Cliente(
                nombre='Catalina',
                apellido='Espinosa',
                email='catalina.espinosa@yahoo.com',
                telefono='3118899001',
                direccion='Carrera 40 #28-56, Villavicencio'
            ),
            Cliente(
                nombre='Alberto',
                apellido='Pineda',
                email='alberto.pineda@gmail.com',
                telefono='3139900112',
                direccion='Av. 68 #43-21, Neiva'
            ),
            Cliente(
                nombre='Paola',
                apellido='Rincón',
                email='paola.rincon@empresa.com',
                telefono='3160011223',
                direccion='Calle 25 #14-78, Armenia'
            ),
            Cliente(
                nombre='Gabriel',
                apellido='Mora',
                email='gabriel.mora@gmail.com',
                telefono='3201122334',
                direccion='Carrera 12 #56-89, Popayán'
            ),
            Cliente(
                nombre='Mónica',
                apellido='Chávez',
                email='monica.chavez@hotmail.com',
                telefono='3052233445',
                direccion='Calle 80 #30-67, Montería'
            ),
            Cliente(
                nombre='Leonardo',
                apellido='Gil',
                email='leonardo.gil@yahoo.com',
                telefono='3093344556',
                direccion='Av. Circunvalar #45-23, Sincelejo'
            ),
            Cliente(
                nombre='Natalia',
                apellido='Ortiz',
                email='natalia.ortiz@gmail.com',
                telefono='3184455667',
                direccion='Carrera 50 #12-90, Valledupar'
            ),
            Cliente(
                nombre='Francisco',
                apellido='Arias',
                email='francisco.arias@empresa.com',
                telefono='3145566778',
                direccion='Calle 90 #33-45, Riohacha'
            ),
            Cliente(
                nombre='Sofía',
                apellido='Velásquez',
                email='sofia.velasquez@gmail.com',
                telefono='3126677889',
                direccion='Diagonal 10 #55-66, Quibdó'
            ),
            Cliente(
                nombre='Jorge',
                apellido='Parra',
                email='jorge.parra@hotmail.com',
                telefono='3177788990',
                direccion='Calle 42 #28-34, Tunja'
            ),
            Cliente(
                nombre='Beatriz',
                apellido='Delgado',
                email='beatriz.delgado@yahoo.com',
                telefono='3218899001',
                direccion='Carrera 22 #70-15, Florencia'
            ),
            Cliente(
                nombre='Guillermo',
                apellido='Castaño',
                email='guillermo.castano@gmail.com',
                telefono='3039900112',
                direccion='Av. Santander #56-78, Leticia'
            ),
            Cliente(
                nombre='Carmen',
                apellido='Londoño',
                email='carmen.londono@empresa.com',
                telefono='3060011223',
                direccion='Calle 5 #34-21, San Andrés'
            ),
        ]
        
        # Guardar todos los registros
        try:
            db.session.add_all(usuarios + libros + clientes)
            db.session.commit()
            print(f"✅ Datos insertados exitosamente!")
            print(f"   - {len(usuarios)} usuarios")
            print(f"   - {len(libros)} libros")
            print(f"   - {len(clientes)} clientes")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error al insertar datos: {e}")
            
if __name__ == '__main__':
    seed_database()