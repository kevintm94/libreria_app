from app import create_app, db
from app.models import Usuario, Libro, Cliente, Venta, DetalleVenta
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random
from decimal import Decimal

def seed_database():
    app = create_app()
    with app.app_context():
        
        # Limpiar datos existentes
        db.drop_all()
        db.create_all()
        
        # Insertar usuarios (4 usuarios)
        usuarios = [
            Usuario(
                usuario='admin',
                password=generate_password_hash('1234'),
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
            ),
            Usuario(
                usuario='vendedor2',
                password=generate_password_hash('vendedor456'),
                email='vendedor2@empresa.com',
                nombre_completo='Vendedor Secundario',
                rol='vendedor'
            )
        ]
        
        # ==================== LIBROS (sin cambios, manteniendo los 50) ====================
        libros = [
            # Solo incluyo algunos como ejemplo, mantén todos tus 50 libros aquí
            Libro(
                isbn='978-0307476463',
                titulo='Cien Años de Soledad',
                autor='Gabriel García Márquez',
                editorial='Sudamericana',
                anio_publicacion=1967,
                genero='Realismo mágico',
                precio=Decimal('189.00'),
                stock=25,
                descripcion='La obra maestra del premio Nobel colombiano.',
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
                precio=Decimal('145.00'),
                stock=30,
                descripcion='La clásica novela distópica.',
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
                precio=95.00,  # Bs
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
                precio=245.00,  # Bs
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
                precio=195.00,  # Bs
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
                precio=125.00,  # Bs
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
                precio=175.00,  # Bs
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
                precio=155.00,  # Bs
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
                precio=295.00,  # Bs
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
                precio=135.00,  # Bs
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
                precio=245.00,  # Bs
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
                precio=165.00,  # Bs
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
                precio=135.00,  # Bs
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
                precio=245.00,  # Bs
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
                precio=165.00,  # Bs
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
                precio=175.00,  # Bs
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
                precio=185.00,  # Bs
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
                precio=195.00,  # Bs
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
                precio=155.00,  # Bs
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
                precio=135.00,  # Bs
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
                precio=185.00,  # Bs
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
                precio=125.00,  # Bs
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
                precio=175.00,  # Bs
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
                precio=155.00,  # Bs
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
                precio=95.00,  # Bs
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
                precio=125.00,  # Bs
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
                precio=215.00,  # Bs
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
                precio=185.00,  # Bs
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
                precio=295.00,  # Bs
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
                precio=195.00,  # Bs
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
                precio=155.00,  # Bs
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
                precio=165.00,  # Bs
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
                precio=115.00,  # Bs
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
                precio=295.00,  # Bs
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
                precio=165.00,  # Bs
                stock=15,
                descripcion='La vida en un colegio militar limeño y sus códigos de violencia y honor.',
                paginas=488,
                idioma='Español'
            ),
        ]
        
        # ==================== CLIENTES (REDUCIDO A 25) ====================
        clientes = [
            # La Paz (5 clientes)
            Cliente(
                nombre='Juan',
                apellido='Pérez',
                email='juan.perez@gmail.com',
                telefono='+591 71543210',
                direccion='Calle 45 #23-12, Sopocachi, La Paz'
            ),
            Cliente(
                nombre='María',
                apellido='González',
                email='maria.gonzalez@hotmail.com',
                telefono='+591 72567890',
                direccion='Av. 20 de Octubre #1234, San Jorge, La Paz'
            ),
            Cliente(
                nombre='Carlos',
                apellido='Rodríguez',
                email='carlos.rodriguez@yahoo.com',
                telefono='+591 71234567',
                direccion='Calle 8 #456, Calacoto, La Paz'
            ),
            Cliente(
                nombre='Ana',
                apellido='Martínez',
                email='ana.martinez@gmail.com',
                telefono='+591 73456789',
                direccion='Av. Ballivián #789, San Miguel, La Paz'
            ),
            Cliente(
                nombre='Luis',
                apellido='Sánchez',
                email='luis.sanchez@empresa.com',
                telefono='+591 74567890',
                direccion='Calle 21 #456, Equipetrol, Santa Cruz'  # Mezclado, ok
            ),
            
            # Santa Cruz (5 clientes)
            Cliente(
                nombre='Laura',
                apellido='Herrera',
                email='laura.herrera@gmail.com',
                telefono='+591 75678901',
                direccion='Av. San Martín #1234, El Prado, Santa Cruz'
            ),
            Cliente(
                nombre='Andrés',
                apellido='López',
                email='andres.lopez@hotmail.com',
                telefono='+591 76789012',
                direccion='Calle 7 #890, Las Palmas, Santa Cruz'
            ),
            Cliente(
                nombre='Carolina',
                apellido='Ramírez',
                email='carolina.ramirez@yahoo.com',
                telefono='+591 77890123',
                direccion='Av. Cristo Redentor #234, Urbari, Santa Cruz'
            ),
            Cliente(
                nombre='Felipe',
                apellido='Torres',
                email='felipe.torres@gmail.com',
                telefono='+591 78901234',
                direccion='Calle Ecuador #567, Queru Queru, Cochabamba'  # Mezclado
            ),
            Cliente(
                nombre='Daniela',
                apellido='Ospina',
                email='daniela.ospina@empresa.com',
                telefono='+591 79012345',
                direccion='Av. América #890, Recoleta, Cochabamba'
            ),
            
            # Cochabamba (5 clientes)
            Cliente(
                nombre='Javier',
                apellido='Molina',
                email='javier.molina@gmail.com',
                telefono='+591 70123456',
                direccion='Calle Bolívar #345, El Mirador, Cochabamba'
            ),
            Cliente(
                nombre='Patricia',
                apellido='Castro',
                email='patricia.castro@hotmail.com',
                telefono='+591 71234568',
                direccion='Av. Pando #456, Tarija'
            ),
            Cliente(
                nombre='Diego',
                apellido='Muñoz',
                email='diego.munoz@yahoo.com',
                telefono='+591 72345679',
                direccion='Calle Potosí #789, Sucre'
            ),
            Cliente(
                nombre='Valentina',
                apellido='Restrepo',
                email='valentina.restrepo@gmail.com',
                telefono='+591 73456780',
                direccion='Av. Blanco Galindo #123, Sacaba, Cochabamba'
            ),
            Cliente(
                nombre='Santiago',
                apellido='Giraldo',
                email='santiago.giraldo@empresa.com',
                telefono='+591 74567891',
                direccion='Calle Libertad #456, Oruro'
            ),
            
            # Otras ciudades (5 clientes)
            Cliente(
                nombre='Camila',
                apellido='Fernández',
                email='camila.fernandez@gmail.com',
                telefono='+591 75678902',
                direccion='Av. Costanera #789, Trinidad'
            ),
            Cliente(
                nombre='Ricardo',
                apellido='Jiménez',
                email='ricardo.jimenez@hotmail.com',
                telefono='+591 76789013',
                direccion='Calle Sucre #234, Potosí'
            ),
            Cliente(
                nombre='Alejandra',
                apellido='Mendoza',
                email='alejandra.mendoza@yahoo.com',
                telefono='+591 77890124',
                direccion='Av. 6 de Agosto #567, Tupiza'
            ),
            Cliente(
                nombre='Oscar',
                apellido='Peña',
                email='oscar.pena@gmail.com',
                telefono='+591 78901235',
                direccion='Calle Linares #890, La Paz'
            ),
            Cliente(
                nombre='Tatiana',
                apellido='Blanco',
                email='tatiana.blanco@gmail.com',
                telefono='+591 79012346',
                direccion='Av. Santa Cruz #123, Montero, Santa Cruz'
            ),
            
            # Últimos 5 para completar 25
            Cliente(
                nombre='Roberto',
                apellido='Navarro',
                email='roberto.navarro@hotmail.com',
                telefono='+591 70123457',
                direccion='Calle 16 de Julio #456, El Alto, La Paz'
            ),
            Cliente(
                nombre='Marcela',
                apellido='Díaz',
                email='marcela.diaz@yahoo.com',
                telefono='+591 71234569',
                direccion='Av. Villazón #789, Cochabamba'
            ),
            Cliente(
                nombre='Gustavo',
                apellido='Álvarez',
                email='gustavo.alvarez@gmail.com',
                telefono='+591 72345680',
                direccion='Calle Camacho #234, La Paz'
            ),
            Cliente(
                nombre='Diana',
                apellido='Suárez',
                email='diana.suarez@hotmail.com',
                telefono='+591 73456781',
                direccion='Av. Busch #567, Santa Cruz'
            ),
            Cliente(
                nombre='Héctor',
                apellido='Rojas',
                email='hector.rojas@yahoo.com',
                telefono='+591 74567892',
                direccion='Calle Murillo #890, Cochabamba'
            ),
        ]

        # Guardar usuarios, libros y clientes
        try:
            db.session.add_all(usuarios + libros + clientes)
            db.session.commit()
            print(f"✅ Datos básicos insertados exitosamente!")
            print(f"   - {len(usuarios)} usuarios")
            print(f"   - {len(libros)} libros")
            print(f"   - {len(clientes)} clientes")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error al insertar datos básicos: {e}")
            return

        # ==================== VENTAS (50 registros desde 01-01-2026 hasta hoy) ====================
        print("Generando 50 ventas desde el 01-01-2026 hasta hoy...")
        
        # Obtener IDs de clientes y usuarios
        clientes_ids = [c.id_cliente for c in clientes]
        usuarios_ids = [u.id_usuario for u in usuarios]
        libros_ids = [l.id_libro for l in libros]
        
        # ✅ MÉTODOS DE PAGO CORREGIDOS - SOLO LOS QUE ESTÁN EN EL ENUM
        metodos_pago = ['efectivo', 'tarjeta', 'transferencia', 'otros']
        
        # Fecha de inicio (1 de enero de 2026)
        fecha_inicio = datetime(2026, 1, 1)
        fecha_fin = datetime.now()  # Fecha actual
        
        # Calcular el rango de días disponibles
        dias_totales = (fecha_fin - fecha_inicio).days
        
        ventas_creadas = []
        
        for i in range(50):
            # Generar fecha aleatoria entre fecha_inicio y fecha_fin
            dias_aleatorios = random.randint(0, max(0, dias_totales))
            fecha_venta = fecha_inicio + timedelta(
                days=dias_aleatorios,
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            )
            
            # Seleccionar cliente y usuario aleatorio
            cliente_id = random.choice(clientes_ids)
            usuario_id = random.choice(usuarios_ids)
            
            # Determinar cantidad de libros en esta venta (1 a 5 libros)
            cantidad_libros = random.randint(1, 5)
            
            # Seleccionar libros únicos para esta venta
            libros_seleccionados = random.sample(libros_ids, min(cantidad_libros, len(libros_ids)))
            
            total_venta = Decimal('0')
            detalles_temp = []
            
            for libro_id in libros_seleccionados:
                libro = next(l for l in libros if l.id_libro == libro_id)
                cantidad = random.randint(1, 3)  # 1 a 3 copias del mismo libro
                precio_unitario = libro.precio  # Ya es Decimal
                
                # Aplicar descuento aleatorio (0-15%) en algunas ventas
                if random.random() < 0.3:  # 30% de probabilidad de descuento
                    descuento = Decimal(str(random.uniform(0.05, 0.15)))
                    precio_unitario = precio_unitario * (Decimal('1') - descuento)
                
                subtotal = precio_unitario * cantidad
                total_venta += subtotal
                
                detalles_temp.append({
                    'id_libro': libro_id,
                    'cantidad': cantidad,
                    'precio_unitario': round(precio_unitario, 2),
                    'subtotal': round(subtotal, 2)
                })
            
            # ✅ CREAR LA VENTA CON MÉTODO DE PAGO VÁLIDO
            venta = Venta(
                id_cliente=cliente_id,
                id_usuario=usuario_id,
                fecha_venta=fecha_venta,
                total=round(total_venta, 2),
                metodo_pago=random.choice(metodos_pago)  # SOLO valores del ENUM
            )
            
            db.session.add(venta)
            db.session.flush()  # Para obtener el ID de la venta
            
            # Crear los detalles de venta
            for detalle in detalles_temp:
                detalle_venta = DetalleVenta(
                    id_venta=venta.id_venta,
                    id_libro=detalle['id_libro'],
                    cantidad=detalle['cantidad'],
                    precio_unitario=detalle['precio_unitario'],
                    subtotal=detalle['subtotal']
                )
                db.session.add(detalle_venta)
                
                # Actualizar stock del libro
                libro = Libro.query.get(detalle['id_libro'])
                if libro:
                    libro.stock -= detalle['cantidad']
            
            ventas_creadas.append(venta)
        
        # Guardar todas las ventas y detalles
        try:
            db.session.commit()
            print(f"✅ Ventas insertadas exitosamente!")
            print(f"   - {len(ventas_creadas)} ventas creadas")
            
            # Mostrar resumen de ventas por mes
            ventas_por_mes = {}
            fechas_ventas = []
            
            for venta in ventas_creadas:
                mes = venta.fecha_venta.strftime('%B')
                ventas_por_mes[mes] = ventas_por_mes.get(mes, 0) + 1
                fechas_ventas.append(venta.fecha_venta.strftime('%d/%m/%Y'))
            
            print("\n📊 Resumen de ventas por mes:")
            for mes, cantidad in ventas_por_mes.items():
                print(f"   - {mes}: {cantidad} ventas")
            
            # Mostrar primeras y últimas fechas
            if fechas_ventas:
                print(f"\n📅 Rango de fechas:")
                print(f"   - Primera venta: {min(fechas_ventas)}")
                print(f"   - Última venta: {max(fechas_ventas)}")
            
            # Total de ingresos
            total_ingresos = sum(v.total for v in ventas_creadas)
            print(f"\n💰 Total de ingresos: Bs {total_ingresos:,.2f}")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error al insertar ventas: {e}")
            
if __name__ == '__main__':
    seed_database()