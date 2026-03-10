from flask import Blueprint, render_template, request, redirect, url_for
from .models import Libro
from .extensions import db

from flask import send_file
from fpdf import FPDF
import io

libros_bp = Blueprint("libros", __name__)

# LISTAR LIBROS
@libros_bp.route("/libros")
def listar_libros():
    # Tomamos el parámetro de búsqueda desde la URL
    busqueda = request.args.get("busqueda", "")

    if busqueda:
        # Filtramos por título, autor o ISBN
        libros = Libro.query.filter(
            (Libro.titulo.ilike(f"%{busqueda}%")) |
            (Libro.autor.ilike(f"%{busqueda}%")) |
            (Libro.isbn.ilike(f"%{busqueda}%"))
        ).all()
    else:
        libros = Libro.query.all()

    return render_template("libro.html", libros=libros, busqueda=busqueda)


# CREAR LIBRO
@libros_bp.route("/libros/crear", methods=["GET","POST"])
def crear_libro():

    error = None

    if request.method == "POST":

        isbn = request.form["isbn"]
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        precio = request.form["precio"]

        if not titulo:
            error = "El título es obligatorio"

        elif not autor:
            error = "El autor es obligatorio"

        elif float(precio) <= 0:
            error = "El precio debe ser mayor a 0"

        libro_existente = Libro.query.filter_by(isbn=isbn).first()

        if libro_existente:
            error = "El ISBN ya existe"

        if error:
            return render_template("crear_libro.html", error=error)

        nuevo_libro = Libro(
            isbn=isbn,
            titulo=titulo,
            autor=autor,
            editorial=request.form["editorial"],
            anio_publicacion=request.form["anio_publicacion"],
            genero=request.form["genero"],
            precio=precio,
            stock=request.form["stock"],
            descripcion=request.form["descripcion"],
            paginas=request.form["paginas"],
            idioma=request.form["idioma"]
        )

        db.session.add(nuevo_libro)
        db.session.commit()

        return redirect(url_for("libros.listar_libros"))

    return render_template("crear_libro.html", error=error)

# EDITAR LIBRO
@libros_bp.route("/libros/editar/<int:id>", methods=["GET", "POST"])
def editar_libro(id):
    libro = Libro.query.get_or_404(id)
    error = None

    if request.method == "POST":

        isbn = request.form["isbn"]
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        precio = request.form["precio"]

        # VALIDACIONES
        if not titulo:
            error = "El título es obligatorio"
        elif not autor:
            error = "El autor es obligatorio"
        elif float(precio) <= 0:
            error = "El precio debe ser mayor a 0"

        # Validar ISBN duplicado (excepto el libro actual)
        libro_existente = Libro.query.filter(Libro.isbn==isbn, Libro.id_libro!=id).first()
        if libro_existente:
            error = "El ISBN ya existe"

        if error:
            return render_template("editar_libro.html", libro=libro, error=error)

        # Actualizar datos
        libro.isbn = isbn
        libro.titulo = titulo
        libro.autor = autor
        libro.editorial = request.form["editorial"]
        libro.anio_publicacion = request.form["anio_publicacion"]
        libro.genero = request.form["genero"]
        libro.precio = precio
        libro.stock = request.form["stock"]
        libro.descripcion = request.form["descripcion"]
        libro.paginas = request.form["paginas"]
        libro.idioma = request.form["idioma"]

        db.session.commit()

        return redirect(url_for("libros.listar_libros"))

    return render_template("editar_libro.html", libro=libro, error=error)

# ELIMINAR LIBRO
@libros_bp.route("/libros/eliminar/<int:id>")
def eliminar_libro(id):

    libro = Libro.query.get_or_404(id)

    db.session.delete(libro)
    db.session.commit()

    return redirect(url_for("libros.listar_libros"))

# REPORTE PDF DE LIBROS
@libros_bp.route("/libros/reporte/pdf")
def reporte_libros_pdf():

    from datetime import datetime
    from fpdf import FPDF
    from flask import send_file
    import io

    libros = Libro.query.all()

    pdf = FPDF()
    pdf.add_page()

    # TITULO
    pdf.set_font("Arial","B",16)
    pdf.cell(190,10,"SISTEMA DE LIBRERIA",0,1,"C")

    pdf.set_font("Arial","B",14)
    pdf.cell(190,10,"REPORTE DE LIBROS",0,1,"C")

    # FECHA
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    pdf.set_font("Arial","",10)
    pdf.cell(190,8,f"Fecha del reporte: {fecha}",0,1)

    pdf.ln(5)

    # ENCABEZADO TABLA
    pdf.set_font("Arial","B",10)

    pdf.cell(25,8,"ISBN",1,0,"C")
    pdf.cell(45,8,"Titulo",1,0,"C")
    pdf.cell(40,8,"Autor",1,0,"C")
    pdf.cell(25,8,"Precio",1,0,"C")
    pdf.cell(20,8,"Stock",1,0,"C")
    pdf.cell(35,8,"Genero",1,1,"C")

    pdf.set_font("Arial","",9)

    for libro in libros:

        isbn = str(libro.isbn)[:12]
        titulo = libro.titulo[:28]
        autor = libro.autor[:25]
        precio = str(libro.precio)
        stock = str(libro.stock)
        genero = libro.genero[:20]

        pdf.cell(25,8,isbn,1)
        pdf.cell(45,8,titulo,1)
        pdf.cell(40,8,autor,1)
        pdf.cell(25,8,precio,1,0,"C")
        pdf.cell(20,8,stock,1,0,"C")
        pdf.cell(35,8,genero,1)

        pdf.ln()

    pdf.ln(5)

    # TOTAL LIBROS
    pdf.set_font("Arial","B",11)
    pdf.cell(190,10,f"Total de libros registrados: {len(libros)}",0,1)

    # GENERAR PDF
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    buffer = io.BytesIO(pdf_bytes)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="reporte_libros.pdf",
        mimetype="application/pdf"
    )