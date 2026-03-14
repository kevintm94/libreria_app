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
            # ... incluye aquí todos tus 50 libros ...
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