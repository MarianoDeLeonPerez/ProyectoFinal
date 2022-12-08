# Entrega Intermedia - Mariano De Leon

### _Descripcion del Proyecto_ 

Proyecto simulando una web donde se puede tanto pedir(seria la creacion del objeto) como buscar ya sean libros, mangas o comics y cuenta con estos 3 modelos.

- Libros (nombre - Charfield),(autor - Charfield)
- Mangas (nombre - Charfield),(autor - Charfield)
- Comics (nombre - Charfield),(autor - Charfield)

### _Funcionamiento de la web_

La web cuenta con 7 botones funcionales, Inicio que se encuentra arriba a la izquierda y en el centro de la web los botones correspondientes para pedir y buscar cada uno de los modelos

| BOTON | URL | FUNCIONAMIENTO|
| ------ | ------ | ----- |
| Inicio | localhost/AppLibros | Te dirije al inicio de la pagina, con el se puede volver despues de las busquedas |
| Pedir Libro | localhost/AppLibros/LibroPeticion | Te lleva al formulario para poder realizar la peticion de un libro |
| Pedir Manga | localhost/AppLibros/MangaPeticion | Te lleva al formulario para poder realizar la peticion de un Manga |
| Pedir Comic | localhost/AppLibros/ComicPeticion | Te lleva al formulario para poder realizar la peticion de un Comic |
| Buscar Libro | localhost/AppLibros/busquedaLibro | Te lleva al formulario para poder realizar la busqueda de un libro |
| Buscar Manga | localhost/AppLibros/busquedaManga | Te lleva al formulario para poder realizar la busqueda de un Manga |
| Buscar Comic | localhost/AppLibros/busquedaComic | Te lleva al formulario para poder realizar la busqueda de un Comic |


## _Opciones de busqueda_

- Libros: Programacion(2 resultados), Html(1 resultado), Django(1 resultado), Visual(1 resultado)
- Mangas: Hero(1 resultado), One Piece(1 resultado)
- Comics: Superman(2 resultados), Capitan(1 resultado)

En caso de no encontrar resultados, la web lo notifica
