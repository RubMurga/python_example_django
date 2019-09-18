/**
 * Created by RubenMurga on 06/08/15.
 */


$(document).on("click","#botonprueba",function(evt){
    var cod;
    cod = $('#id_codigo_barras').val();
    $.get('/Chilpancingo/cafeteria/busqueda/', {codigo: cod}, function(data){
        if(data==1) {
            toastr.success('Se ha agregado el producto');
        }
    });
});

$(document).ready(function(evt){
    var validador;
    if($('#divvalidador').text() == 1){
        toastr.success('Se ha agregado el correctamente.');
    }
    else if($('#divvalidador').text()==2){
        toastr.success('Se ha cambiado el precio del producto correctamente.');
    }
    else if($('#divvalidador').text()==3){
        toastr.success('Se han borrado los libros del inventario.');
    }
    else if($('#divvalidador').text()==4){
        toastr.success('Se han borrado los productos del inventario.');
    }});

/* busquedas ajax */

$('#buscarLibro').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/libreria/buscando/libro', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                $('#resultbusqueda').html("");

                toastr.warning('No se ha encontrado un resultado a la busqueda');

            }
        });
    }
});
$('#buscarLibrocb').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/libreria/buscando/libro/codigo-barras', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                $('#resultbusqueda').html("");

                toastr.warning('No se ha encontrado un resultado a la busqueda');

            }
        }).fail(function(){
           toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
        });
    }
});

$('#buscarCategoria').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/libreria/buscando/categoria', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
            }
        });
    }
});


$('#inputProducto').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/cafeteria/buscando/producto', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
            }
        });
    }
});


$('#inputProductocb').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/cafeteria/buscando/producto/codigo-barras', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
            }
        }).fail(function(){
           toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
        });
    }
});



$('#buscarProducto').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/comercializadora/buscando/producto', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
            }
        });
    }
});


$('#buscarProductocb').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/comercializadora/buscando/producto/codigo-barras', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
            }

        }).fail(function(){
           toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
        });
    }
});

$('#buscarCategoriaC').keyup(function(){
    var query;
    query = $(this).val();
    if(query != "") {
        $.get('/Chilpancingo/comercializadora/buscando/categoria', {sugerencia: query}, function (data) {
            if (data != "") {
                $('#resultbusqueda').html(data);
                    toastr.success('Se han encontrado coincidencias a la busqueda');
            }
            else {
                toastr.warning('No se ha encontrado un resultado a la busqueda');
                $('#resultbusqueda').html("");
            }
        });
    }
});


