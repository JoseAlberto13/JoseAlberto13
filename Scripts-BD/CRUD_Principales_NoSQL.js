use analista2025;

show dbs;

show collections;

// ***** CREATE ******
// Insertar un elemento
db.estudiantes.insertOne({Id:"1001", Nombre_Estudiante:"José", Apellido_Estudiante:"Figueroa", Email:"elqueso@gmail.com", Direccion:"Las Violetas 537", Telefono:null});
db.estudiantes.insertOne({Id:"1002", Nombre_Estudiante:"Mario", Apellido_Estudiante:"Figueroa", Email:"elqueso@gmail.com", Direccion:"Las Violetas 537", Telefono:null});

// Insertar varios elementos
db.estudiantes.insertMany([
{Id:"1003", Nombre_Estudiante:"Carlos", Apellido_Estudiante:"Figueroa", Email:"elqueso@gmail.com", Direccion:"Las Violetas 537", Telefono:null},
{Id:"1004", Nombre_Estudiante:"Alberto", Apellido_Estudiante:"Figueroa", Email:"elqueso@gmail.com", Direccion:"Las Violetas 537", Telefono:null}
]);

// ***** READ ******
// Leer todos los elementos
db.estudiantes.find();

// Buscar elementos con cierta caracteristica (Filtro)
db.estudiantes.find({ Apellido_Estudiante: "Figueroa" });

// Buscar un solo elemento
db.estudiantes.findOne({ Apellido_Estudiante: "Sharpin" });

// Buscar elementeos en orden ascendente
db.estudiantes.find().sort({Id: 1});
db.estudiantes.find().sort({Apellido_Estudiante: 1});

// Buscar elementeos en orden descendente
db.estudiantes.find().sort({Id: -1});
db.estudiantes.find().sort({Apellido_Estudiante: -1});

// Buscar una cantidad limitada de elementos
db.estudiantes.find().limit(5);

// ***** UPDATE ******
// Actualizar/Modificar un valor de un documento
db.estudiantes.updateOne({Id:1}, { $set:{Nombre_Estudiante:"Antonio"}});

// Actualizar/Modificar todo el documento
db.estudiantes.replaceOne({Id:2},
    {Id:2,
    Nombre_Estudiante: "Elvira",
    Apellido_Estudiante: "Lucena",
    Email: [
        "sbasdfh1@wikia.com",
        "sbaasdf1@unc.edu",
        "sbartadsf@webeden.co.uk"
    ],
    Direccion: [
        {
            Calle : "Las Violetas",
            Numero : "537"
        }
    ],
    Telefono : {
        Contact_Mama : "+5 963 644 8639",
        Contact_Papa : "+56 684 490 3999"
    }});
    
// Actualizar/Modificar el valor de un campo en toda la colección
db.estudiantes.updateMany({Apellido_Estudiante:"Figueroa"}, {$set: {Apellido_Estudiante:"Lucena"}});
db.estudiantes.find({Apellido_Estudiante:"Lucena"});

// ***** DELETE ******
// Eliminar un documento
db.estudiantes.deleteOne({Id:3});

// Eliminar varios documentos   >>> creamos varios documentos "datos" para eliminarlos y ver el cambio
db.estudiantes.insertMany([
{Id:"1005", Nombre_Estudiante:"asdf", Apellido_Estudiante:"asdff", Email:"elqueso@gmail.com", Direccion:"Las Violetas 537", Telefono:null},
{Id:"1006", Nombre_Estudiante:"asdf", Apellido_Estudiante:"asdff", Email:"elqueso@gmail.com", Direccion:"Las Violetas 537", Telefono:null},
{Id:"1007", Nombre_Estudiante:"asdf", Apellido_Estudiante:"asdff", Email:"elqueso@gmail.com", Direccion:"Las Violetas 537", Telefono:null}
]);

db.estudiantes.find({Nombre_Estudiante:"asdf"});

db.estudiantes.deleteMany({Nombre_Estudiante:"asdf"});