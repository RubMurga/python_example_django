var app_control = angular.module('AppControl',[]);
app_control.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}
app_control.controller('ventas_dia_libreria_ctrl', function($scope,$http){
    var precio = 0,j=0;
    $scope.ventas_iniciales = function() {
        precio = 0; j=0;
        toastr.info("Todas las ventas de hoy");
        var url_inicial = "/Chilpancingo/control/libreria/ventas-por-dia/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0)
            {
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;

            }
            else{
                $scope.valida = 0;
                $scope.verifica = 0;
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_vendedor_func = function () {
        precio = 0;j=0;
        var url_vendedor = "/Chilpancingo/control/libreria/ventas-por-dia/vendedor/?vendedor="+$scope.vendedor_libreria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info("Todas las ventas de hoy hechas por " + $scope.libros[0]['vendido_por']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = parseFloat($scope.libros[i]['precio']) + precio;
                }
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio
                $scope.verifica = 1;
            }
            else{
                $scope.verifica = 1;
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha hecho ventas');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_libro_func = function () {
        precio = 0;j=0;
        var url_libro = "/Chilpancingo/control/libreria/ventas-por-dia/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas del libro ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio']) * (parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;
            }
            else {
                $scope.verifica = 0;
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning("Algo pasó :S");
        });
    };
    $scope.ventas_iniciales();
});

app_control.controller('ventas_mes_libreria_ctrl', function($scope,$http){
    var precio = 0,j=0;
    $scope.ventas_iniciales = function() {
        $scope.loading = true
        precio = 0; costo= 0; inversion=0;j=0;
        toastr.info("Todas las ventas de este mes");
        var url_inicial = "/Chilpancingo/control/libreria/ventas-por-mes/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = []
            for(let articulo of data.articulos){
                let precios = [] 
                for (let producto of data.productos){
                    if (articulo.id === producto.nombre_libro_id){
                        precios.push(producto.precio)
                    }
                }
                let precios_unique = precios.filter(onlyUnique)
                
                for (let precio of precios_unique){
                    let temp_prod = {
                        nombre: articulo.nombre,
                        precio: precio,
                        vendidos: 0,
                        no_vendidos: 0
                    }
                    for (let producto of data.productos){
                        if (articulo.id === producto.nombre_libro_id && precio === producto.precio){
                            if (producto.vendido == 1) temp_prod.vendidos++
                            else temp_prod.no_vendidos++
                            temp_prod.costo = producto.costo
                        }
                    }
                    $scope.libros.push(temp_prod)
                }
            }

            if($scope.libros.length != 0)
            {
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;
                $scope.loading = false
            }
            else{
                $scope.valida = 0;
                $scope.verifica = 0;
            }

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_libro_func = function () {
        precio = 0;j=0;
        $scope.loading = true
        var url_libro = "/Chilpancingo/control/libreria/ventas-por-mes/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0 || $scope.libros[0]['vendidos'] != 0) {
                toastr.info('Mostrando las ventas del libro ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio']) * (parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;
                $scope.loading = false
            }
            else {
                $scope.verifica = 0;
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning("Algo pasó :S");
        });
    };
    $scope.ventas_iniciales();
});

app_control.controller('ventas_dia_cafeteria_ctrl', function($scope,$http){
    var precio = 0,costo = 0,inversion = 0,j=0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;j=0;
        toastr.info("Todas las ventas de hoy");
        var url_inicial = "/Chilpancingo/control/cafeteria/ventas-por-dia/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0){
                for (var i = 0; i < $scope.productos.length; i++) {
                        precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                        j = j + parseInt($scope.productos[i]['vendidos']);
                }
                $scope.verifica = 0;
                $scope.vendidos = j;
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio;
            }
            else{
                $scope.valida = 0;
                $scope.verifica = 0;
            }

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_vendedor_func = function () {
        precio = 0; costo= 0; inversion= 0;
        var url_vendedor = "/Chilpancingo/control/cafeteria/ventas-por-dia/vendedor/?vendedor="+$scope.vendedor_cafeteria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0) {
                toastr.info("Todas las ventas de hoy hechas por " + $scope.productos[0]['vendido_por']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = parseFloat($scope.productos[i]['precio']) + precio;

                }
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio - costo;
                $scope.verifica = 1;

            }
            else{
                $scope.verifica = 1;
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha hecho ventas');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_producto_func = function () {
        precio = 0;
        costo = 0;
        inversion = 0;
        j=0;
        var url_libro = "/Chilpancingo/control/cafeteria/ventas-por-dia/producto/?producto=" + $scope.producto_input;
        $http.get(url_libro).success(function (data) {
            $scope.productos = data;
            if ($scope.productos.length != 0) {
                toastr.info('Mostrando las ventas del producto ' + $scope.productos[0]['nombre']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio']) * (parseInt($scope.productos[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.productos[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;
            }
            else {
                $scope.verifica = 0;
                $scope.valida = 0;
                $scope.productos = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning("Algo pasó :S");
        });
    };
    $scope.ventas_iniciales();
});

app_control.controller('ventas_mes_cafeteria_ctrl', function($scope,$http){
    var precio = 0,j= 0;
    $scope.ventas_iniciales = function() {
        $scope.loading = true
        precio = 0; costo= 0; inversion=0;j=0;k=0;
        toastr.info("Todas las ventas de este mes");
        var url_inicial = "/Chilpancingo/control/cafeteria/ventas-por-mes/inicial/";
        $http.get(url_inicial).success(function (data) {
            
            $scope.productos = []
            for(let articulo of data.articulos){
                let precios = [] 
                for (let producto of data.productos){
                    if (articulo.id === producto.nombre_producto_id){
                        precios.push(producto.precio)
                    }
                }
                let precios_unique = precios.filter(onlyUnique)
                
                for (let precio of precios_unique){
                    let temp_prod = {
                        nombre: articulo.nombre,
                        precio: precio,
                        vendidos: 0,
                        no_vendidos: 0
                    }
                    for (let producto of data.productos){
                        if (articulo.id === producto.nombre_producto_id && precio === producto.precio){
                            if (producto.vendido == 1) temp_prod.vendidos++
                            else temp_prod.no_vendidos++
                            temp_prod.costo = producto.costo
                        }
                    }
                    $scope.productos.push(temp_prod)
                }
            }
            if($scope.productos.length != 0)
            {
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.productos[i]['vendidos']);
                }
                $scope.verifica = 0;
                $scope.vendidos = j;
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio;
                $scope.loading = false
            }
            else{
                $scope.valida = 0;
                $scope.verifica = 0;
            }

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_producto_func = function () {
        precio = 0;
        $scope.loading = true
        var url_libro = "/Chilpancingo/control/cafeteria/ventas-por-mes/producto/?producto="+ $scope.producto_input;
        $http.get(url_libro).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0)  {
                toastr.info('Mostrando las ventas del producto ' + $scope.productos[0]['nombre']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.productos[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio;
                $scope.loading = false
            }
            else{
                $scope.valida = 0;
                $scope.productos = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }

            if ($scope.productos[0]['vendidos'] == "0"){
                $scope.valida = 0;
                $scope.productos = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.ventas_iniciales();
});

app_control.controller('ventas_semana_libreria_ctrl', function($scope,$http){
    var precio = 0,costo = 0,inversion = 0,j=0;
    var ventas_l= 0,ventas_m = 0, ventas_mi = 0, ventas_ju = 0, ventas_vi = 0, ventas_sa= 0,ventas_dom = 0;
    var num_l =0,num_m=0, num_mi = 0, num_ju = 0, num_vi = 0, num_sa = 0, num_dom = 0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        toastr.info("Todas las ventas de esta semana");
        var url_inicial = "/Chilpancingo/control/libreria/ventas-por-semana/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = data;
            for (var i = 0; i < $scope.libros.length; i++) {
                precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                j = j + parseInt($scope.libros[i]['vendidos']);
                if($scope.libros[i]['dia'] == 'lunes'){
                    num_l = num_l + parseInt($scope.libros[i]['vendidos']);
                    ventas_l = ventas_l + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'martes'){
                    num_m = num_m + parseInt($scope.libros[i]['vendidos']);
                    ventas_m = ventas_m + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'miercoles'){
                    num_mi = num_mi + parseInt($scope.libros[i]['vendidos']);
                    ventas_mi = ventas_mi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'jueves'){
                    num_ju = num_ju + parseInt($scope.libros[i]['vendidos']);
                    ventas_ju = ventas_ju + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'viernes'){
                    num_vi = num_vi + parseInt($scope.libros[i]['vendidos']);
                    ventas_vi = ventas_vi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'sabado'){
                    num_sa = num_sa + parseInt($scope.libros[i]['vendidos']);
                    ventas_sa = ventas_sa + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'domingo'){
                    num_dom = num_dom + parseInt($scope.libros[i]['vendidos']);
                    ventas_dom = ventas_dom + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }
            }
            $scope.valida = j;
            $scope.ganancias = precio;
            $scope.inversion = inversion;
            $scope.resta = precio - inversion;

            $scope.num_l = num_l; $scope.ventas_l = ventas_l;
            $scope.num_m = num_m; $scope.ventas_m = ventas_m;
            $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
            $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
            $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
            $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
            $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.ventas_iniciales();


        $scope.busca_vendedor_func = function () {
        precio = 0; costo= 0; inversion= 0;j=0;
            ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        var url_vendedor = "/Chilpancingo/control/libreria/ventas-por-semana/vendedor/?vendedor="+$scope.vendedor_libreria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info("Todas las ventas de esta semana hechas por " + $scope.libros[0]['vendido_por']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    if($scope.libros[i]['dia'] == 'lunes'){
                        num_l = num_l + parseInt($scope.libros[i]['vendidos']);
                        ventas_l = ventas_l + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'martes'){
                        num_m = num_m + parseInt($scope.libros[i]['vendidos']);
                        ventas_m = ventas_m + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'miercoles'){
                        num_mi = num_mi + parseInt($scope.libros[i]['vendidos']);
                        ventas_mi = ventas_mi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'jueves'){
                        num_ju = num_ju + parseInt($scope.libros[i]['vendidos']);
                        ventas_ju = ventas_ju + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'viernes'){
                        num_vi = num_vi + parseInt($scope.libros[i]['vendidos']);
                        ventas_vi = ventas_vi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'sabado'){
                        num_sa = num_sa + parseInt($scope.libros[i]['vendidos']);
                        ventas_sa = ventas_sa + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'domingo'){
                        num_dom = num_dom + parseInt($scope.libros[i]['vendidos']);
                        ventas_dom = ventas_dom + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }
                }
                $scope.valida = j;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;

                $scope.num_l = num_l; $scope.ventas_l = ventas_l;
                $scope.num_m = num_m; $scope.ventas_m = ventas_m;
                $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
                $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
                $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
                $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
                $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;


            }
            else{
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha hecho ventas');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_libro_func = function () {
        precio = 0; costo= 0; inversion= 0;j=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        var url_libro = "/Chilpancingo/control/libreria/ventas-por-semana/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
                $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas en la semana del libro ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    if($scope.libros[i]['dia'] == 'lunes'){
                        num_l = num_l + parseInt($scope.libros[i]['vendidos']);
                        ventas_l = ventas_l + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'martes'){
                        num_m = num_m + parseInt($scope.libros[i]['vendidos']);
                        ventas_m = ventas_m + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'miercoles'){
                        num_mi = num_mi + parseInt($scope.libros[i]['vendidos']);
                        ventas_mi = ventas_mi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'jueves'){
                        num_ju = num_ju + parseInt($scope.libros[i]['vendidos']);
                        ventas_ju = ventas_ju + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'viernes'){
                        num_vi = num_vi + parseInt($scope.libros[i]['vendidos']);
                        ventas_vi = ventas_vi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'sabado'){
                        num_sa = num_sa + parseInt($scope.libros[i]['vendidos']);
                        ventas_sa = ventas_sa + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'domingo'){
                        num_dom = num_dom + parseInt($scope.libros[i]['vendidos']);
                        ventas_dom = ventas_dom + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }
                }
                $scope.valida = j;
                $scope.ganancias = precio ;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;

                $scope.num_l = num_l; $scope.ventas_l = ventas_l;
                $scope.num_m = num_m; $scope.ventas_m = ventas_m;
                $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
                $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
                $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
                $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
                $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;
            }
            else{
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.lunes = false;
    $scope.martes = false;
    $scope.miercoles = false;
    $scope.jueves = false;
    $scope.viernes = false;
    $scope.sabado = false;
    $scope.domingo = false;
    $scope.muestra_lunes = function(){
        if($scope.lunes == false) {
            $scope.lunes = true;
        }
        else if($scope.lunes == true){
            $scope.lunes = false;
        }
    };
        $scope.muestra_martes = function(){
        if($scope.martes == false) {
            $scope.martes = true;
        }
        else if($scope.martes == true){
            $scope.martes = false;
        }
    };
        $scope.muestra_miercoles = function(){
        if($scope.miercoles == false) {
            $scope.miercoles = true;
        }
        else if($scope.miercoles == true){
            $scope.miercoles = false;
        }
    };
        $scope.muestra_jueves = function(){
        if($scope.jueves == false) {
            $scope.jueves = true;
        }
        else if($scope.jueves == true){
            $scope.jueves = false;
        }
    };
        $scope.muestra_viernes = function(){
        if($scope.viernes == false) {
            $scope.viernes = true;
        }
        else if($scope.viernes == true){
            $scope.viernes = false;
        }
    };
        $scope.muestra_sabado = function(){
        if($scope.sabado == false) {
            $scope.sabado = true;
        }
        else if($scope.sabado == true){
            $scope.sabado = false;
        }
    };
        $scope.muestra_domingo = function(){
        if($scope.domingo == false) {
            $scope.domingo = true;
        }
        else if($scope.domingo == true){
            $scope.domingo = false;
        }
    };
});

app_control.controller('ventas_semana_cafeteria_ctrl', function($scope,$http){
    var precio = 0,costo = 0,inversion = 0,j=0;
    var ventas_l= 0,ventas_m = 0, ventas_mi = 0, ventas_ju = 0, ventas_vi = 0, ventas_sa= 0,ventas_dom = 0;
    var num_l =0,num_m=0, num_mi = 0, num_ju = 0, num_vi = 0, num_sa = 0, num_dom = 0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;j=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        toastr.info("Todas las ventas de esta semana");
        var url_inicial = "/Chilpancingo/control/cafeteria/ventas-por-semana/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.productos = data;
            for (var i = 0; i < $scope.productos.length; i++) {
                precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                inversion = (parseFloat($scope.productos[i]['costo'])*(parseInt($scope.productos[i]['vendidos']) + parseInt($scope.productos[i]['no_vendidos']))) + inversion;
                j = j + parseInt($scope.productos[i]['vendidos']);
                if($scope.productos[i]['dia'] == 'lunes'){
                    num_l = num_l + parseInt($scope.productos[i]['vendidos']);
                    ventas_l = ventas_l + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                }else if($scope.productos[i]['dia'] == 'martes'){
                    num_m = num_m + parseInt($scope.productos[i]['vendidos']);
                    ventas_m = ventas_m + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                }else if($scope.productos[i]['dia'] == 'miercoles'){
                    num_mi = num_mi + parseInt($scope.productos[i]['vendidos']);
                    ventas_mi = ventas_mi + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                }else if($scope.productos[i]['dia'] == 'jueves'){
                    num_ju = num_ju + parseInt($scope.productos[i]['vendidos']);
                    ventas_ju = ventas_ju + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                }else if($scope.productos[i]['dia'] == 'viernes'){
                    num_vi = num_vi + parseInt($scope.productos[i]['vendidos']);
                    ventas_vi = ventas_vi + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                }else if($scope.productos[i]['dia'] == 'sabado'){
                    num_sa = num_sa + parseInt($scope.productos[i]['vendidos']);
                    ventas_sa = ventas_sa + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                }else if($scope.productos[i]['dia'] == 'domingo'){
                    num_dom = num_dom + parseInt($scope.productos[i]['vendidos']);
                    ventas_dom = ventas_dom + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                }
            }
            $scope.num_l = num_l; $scope.ventas_l = ventas_l;
            $scope.num_m = num_m; $scope.ventas_m = ventas_m;
            $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
            $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
            $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
            $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
            $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;

            $scope.valida = j;
            $scope.ganancias = precio;
            $scope.inversion = inversion;
            $scope.resta = precio - inversion;

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_vendedor_func = function () {
        precio = 0; costo= 0; inversion= 0;j=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        var url_vendedor = "/Chilpancingo/control/cafeteria/ventas-por-semana/vendedor/?vendedor="+$scope.vendedor_cafeteria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0) {
                toastr.info("Todas las ventas de esta semana hechas por " + $scope.productos[0]['vendido_por']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.productos[i]['costo'])*(parseInt($scope.productos[i]['vendidos']) + parseInt($scope.productos[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.productos[i]['vendidos']);
                    if($scope.productos[i]['dia'] == 'lunes'){
                        num_l = num_l + parseInt($scope.productos[i]['vendidos']);
                        ventas_l = ventas_l + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'martes'){
                        num_m = num_m + parseInt($scope.productos[i]['vendidos']);
                        ventas_m = ventas_m + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'miercoles'){
                        num_mi = num_mi + parseInt($scope.productos[i]['vendidos']);
                        ventas_mi = ventas_mi + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'jueves'){
                        num_ju = num_ju + parseInt($scope.productos[i]['vendidos']);
                        ventas_ju = ventas_ju + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'viernes'){
                        num_vi = num_vi + parseInt($scope.productos[i]['vendidos']);
                        ventas_vi = ventas_vi + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'sabado'){
                        num_sa = num_sa + parseInt($scope.productos[i]['vendidos']);
                        ventas_sa = ventas_sa + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'domingo'){
                        num_dom = num_dom + parseInt($scope.productos[i]['vendidos']);
                        ventas_dom = ventas_dom + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }
                }
                $scope.valida = j;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;

                $scope.num_l = num_l; $scope.ventas_l = ventas_l;
                $scope.num_m = num_m; $scope.ventas_m = ventas_m;
                $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
                $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
                $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
                $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
                $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;

            }
            else{
                $scope.valida = 0;
                $scope.productos = [];
                $scope.ganancias = 0;
                toastr.warning('No ha hecho ventas');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_producto_func = function () {
        precio = 0; costo= 0; inversion= 0;j=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        var url_libro = "/Chilpancingo/control/cafeteria/ventas-por-semana/producto/?producto="+ $scope.producto_input;
        $http.get(url_libro).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0) {
                toastr.info('Mostrando las ventas de esta semana del producto ' + $scope.productos[0]['nombre']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.productos[i]['costo'])*(parseInt($scope.productos[i]['vendidos']) + parseInt($scope.productos[i]['no_vendidos']))) + inversion;
                     j = j + parseInt($scope.productos[i]['vendidos']);

                    if($scope.productos[i]['dia'] == 'lunes'){
                        num_l = num_l + parseInt($scope.productos[i]['vendidos']);
                        ventas_l = ventas_l + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'martes'){
                        num_m = num_m + parseInt($scope.productos[i]['vendidos']);
                        ventas_m = ventas_m + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'miercoles'){
                        num_mi = num_mi + parseInt($scope.productos[i]['vendidos']);
                        ventas_mi = ventas_mi + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'jueves'){
                        num_ju = num_ju + parseInt($scope.productos[i]['vendidos']);
                        ventas_ju = ventas_ju + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'viernes'){
                        num_vi = num_vi + parseInt($scope.productos[i]['vendidos']);
                        ventas_vi = ventas_vi + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'sabado'){
                        num_sa = num_sa + parseInt($scope.productos[i]['vendidos']);
                        ventas_sa = ventas_sa + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }else if($scope.productos[i]['dia'] == 'domingo'){
                        num_dom = num_dom + parseInt($scope.productos[i]['vendidos']);
                        ventas_dom = ventas_dom + (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos'])));
                    }

                }
                $scope.valida = j;
                $scope.ganancias = precio - costo;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;

                $scope.num_l = num_l; $scope.ventas_l = ventas_l;
                $scope.num_m = num_m; $scope.ventas_m = ventas_m;
                $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
                $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
                $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
                $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
                $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;
            }
            else{
                $scope.valida = 0;
                $scope.productos = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.ventas_iniciales();
    $scope.lunes = false;
    $scope.martes = false;
    $scope.miercoles = false;
    $scope.jueves = false;
    $scope.viernes = false;
    $scope.sabado = false;
    $scope.domingo = false;
    $scope.muestra_lunes = function(){
        if($scope.lunes == false) {
            $scope.lunes = true;
        }
        else if($scope.lunes == true){
            $scope.lunes = false;
        }
    };
        $scope.muestra_martes = function(){
        if($scope.martes == false) {
            $scope.martes = true;
        }
        else if($scope.martes == true){
            $scope.martes = false;
        }
    };
        $scope.muestra_miercoles = function(){
        if($scope.miercoles == false) {
            $scope.miercoles = true;
        }
        else if($scope.miercoles == true){
            $scope.miercoles = false;
        }
    };
        $scope.muestra_jueves = function(){
        if($scope.jueves == false) {
            $scope.jueves = true;
        }
        else if($scope.jueves == true){
            $scope.jueves = false;
        }
    };
        $scope.muestra_viernes = function(){
        if($scope.viernes == false) {
            $scope.viernes = true;
        }
        else if($scope.viernes == true){
            $scope.viernes = false;
        }
    };
        $scope.muestra_sabado = function(){
        if($scope.sabado == false) {
            $scope.sabado = true;
        }
        else if($scope.sabado == true){
            $scope.sabado = false;
        }
    };
        $scope.muestra_domingo = function(){
        if($scope.domingo == false) {
            $scope.domingo = true;
        }
        else if($scope.domingo == true){
            $scope.domingo = false;
        }
    };
});

app_control.controller('libros_registrados_ctrl', function ($scope,$http) {
    var precio = 0,costo = 0,inversion = 0,j= 0,k=0;
    $scope.ventas_iniciales = function() {
        $scope.loading = true
        precio = 0; costo= 0; inversion=0;j=0;k=0;
        toastr.info("mostrando todos los libros registrados");
        var url_inicial = "/Chilpancingo/control/libreria/libros/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = []
            for(let articulo of data.articulos){
                let precios = [] 
                for (let producto of data.productos){
                    if (articulo.id === producto.nombre_libro_id){
                        precios.push(producto.precio)
                    }
                }
                let precios_unique = precios.filter(onlyUnique)
                
                for (let precio of precios_unique){
                    let temp_prod = {
                        nombre: articulo.nombre,
                        precio: precio,
                        vendidos: 0,
                        no_vendidos: 0
                    }
                    for (let producto of data.productos){
                        if (articulo.id === producto.nombre_libro_id && precio === producto.precio){
                            if (producto.vendido == 1) temp_prod.vendidos++
                            else temp_prod.no_vendidos++
                            temp_prod.costo = producto.costo
                        }
                    }
                    $scope.libros.push(temp_prod)
                }
            }
            if($scope.libros.length != 0)
            {
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    k = k + parseInt($scope.libros[i]['no_vendidos']);
                }
                $scope.vendidos = j;
                $scope.restantes = k;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;
                $scope.loading = false
            }
            else{
                $scope.valida = 0;
            }

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.ventas_iniciales();

        $scope.busca_libro_func = function () {
        $scope.loading = true
        precio = 0; costo= 0; inversion= 0;j=0;
        var url_libro = "/Chilpancingo/control/libreria/libros/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
                $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas del libro ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    k = k + parseInt($scope.libros[i]['no_vendidos']);
                }
                $scope.vendidos = j;
                $scope.restantes = k;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;
                $scope.loading = false
            }
            else{
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');

            }
            $scope.loading = false
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
});


app_control.controller('productos_registrados_ctrl', function ($scope,$http) {
   var precio = 0,costo = 0,inversion = 0,j= 0,k=0;
    $scope.ventas_iniciales = function() {
        $scope.loading = true
        precio = 0; costo= 0; inversion=0;
        j = 0;k=0;
        toastr.info("Mostrando todos los productos registrados");
        var url_inicial = "/Chilpancingo/control/cafeteria/productos/";
        $http.get(url_inicial).success(function (data) {
            $scope.productos = []
            for(let articulo of data.articulos){
                let precios = [] 
                for (let producto of data.productos){
                    if (articulo.id === producto.nombre_producto_id){
                        precios.push(producto.precio)
                    }
                }
                let precios_unique = precios.filter(onlyUnique)
                
                for (let precio of precios_unique){
                    let temp_prod = {
                        nombre: articulo.nombre,
                        precio: precio,
                        vendidos: 0,
                        no_vendidos: 0
                    }
                    for (let producto of data.productos){
                        if (articulo.id === producto.nombre_producto_id && precio === producto.precio){
                            if (producto.vendido == 1) temp_prod.vendidos++
                            else temp_prod.no_vendidos++
                            temp_prod.costo = producto.costo
                        }
                    }
                    $scope.productos.push(temp_prod)
                }
            }
            if($scope.productos.length != 0)
            {
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.productos[i]['costo'])*(parseInt($scope.productos[i]['vendidos']) + parseInt($scope.productos[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.productos[i]['vendidos']);
                    k = k + parseInt($scope.productos[i]['no_vendidos']);
                }
                $scope.vendidos = j;
                $scope.restantes = k;
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;
                $scope.loading = false
            }
            else{
                $scope.valida = 0;
            }

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_producto_func = function () {
        precio = 0; costo= 0; inversion= 0;j= 0;k=0;
        $scope.loading = true
        var url_libro = "/Chilpancingo/control/cafeteria/productos/producto/?producto="+ $scope.producto_input;
        $http.get(url_libro).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0) {
                toastr.info('Mostrando las ventas del producto ' + $scope.productos[0]['nombre']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.productos[i]['costo'])*(parseInt($scope.productos[i]['vendidos']) + parseInt($scope.productos[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.productos[i]['vendidos']);
                    k = k + parseInt($scope.productos[i]['no_vendidos']);
                }
                $scope.vendidos = j;
                $scope.restantes = k;
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio ;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;
                $scope.loading = false
            }
            else{
                $scope.valida = 0;
                $scope.productos = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.ventas_iniciales();
});







app_control.controller('ventas_dia_comercializadora_ctrl', function($scope,$http){
    var precio = 0,j=0;
    $scope.ventas_iniciales = function() {
        precio = 0; j=0;
        toastr.info("Todas las ventas de hoy");
        var url_inicial = "/Chilpancingo/control/comercializadora/ventas-por-dia/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0)
            {
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;

            }
            else{
                $scope.valida = 0;
                $scope.verifica = 0;
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_vendedor_func = function () {
        precio = 0;j=0;
        var url_vendedor = "/Chilpancingo/control/comercializadora/ventas-por-dia/vendedor/?vendedor="+$scope.vendedor_libreria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info("Todas las ventas de hoy hechas por " + $scope.libros[0]['vendido_por']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = parseFloat($scope.libros[i]['precio']) + precio;
                }
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio
                $scope.verifica = 1;
            }
            else{
                $scope.verifica = 1;
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha hecho ventas');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_libro_func = function () {
        precio = 0;j=0;
        var url_libro = "/Chilpancingo/control/comercializadora/ventas-por-dia/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas del producto ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio']) * (parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;
            }
            else {
                $scope.verifica = 0;
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning("Algo pasó :S");
        });
    };
    $scope.ventas_iniciales();
});



app_control.controller('ventas_semana_comercializadora_ctrl', function($scope,$http){
    var precio = 0,costo = 0,inversion = 0,j=0;
    var ventas_l= 0,ventas_m = 0, ventas_mi = 0, ventas_ju = 0, ventas_vi = 0, ventas_sa= 0,ventas_dom = 0;
    var num_l =0,num_m=0, num_mi = 0, num_ju = 0, num_vi = 0, num_sa = 0, num_dom = 0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        toastr.info("Todas las ventas de esta semana");
        var url_inicial = "/Chilpancingo/control/comercializadora/ventas-por-semana/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = data;
            for (var i = 0; i < $scope.libros.length; i++) {
                precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                j = j + parseInt($scope.libros[i]['vendidos']);
                if($scope.libros[i]['dia'] == 'lunes'){
                    num_l = num_l + parseInt($scope.libros[i]['vendidos']);
                    ventas_l = ventas_l + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'martes'){
                    num_m = num_m + parseInt($scope.libros[i]['vendidos']);
                    ventas_m = ventas_m + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'miercoles'){
                    num_mi = num_mi + parseInt($scope.libros[i]['vendidos']);
                    ventas_mi = ventas_mi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'jueves'){
                    num_ju = num_ju + parseInt($scope.libros[i]['vendidos']);
                    ventas_ju = ventas_ju + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'viernes'){
                    num_vi = num_vi + parseInt($scope.libros[i]['vendidos']);
                    ventas_vi = ventas_vi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'sabado'){
                    num_sa = num_sa + parseInt($scope.libros[i]['vendidos']);
                    ventas_sa = ventas_sa + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }else if($scope.libros[i]['dia'] == 'domingo'){
                    num_dom = num_dom + parseInt($scope.libros[i]['vendidos']);
                    ventas_dom = ventas_dom + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                }
            }
            $scope.valida = j;
            $scope.ganancias = precio;
            $scope.inversion = inversion;
            $scope.resta = precio - inversion;

            $scope.num_l = num_l; $scope.ventas_l = ventas_l;
            $scope.num_m = num_m; $scope.ventas_m = ventas_m;
            $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
            $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
            $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
            $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
            $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.ventas_iniciales();


        $scope.busca_vendedor_func = function () {
        precio = 0; costo= 0; inversion= 0;j=0;
            ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        var url_vendedor = "/Chilpancingo/control/comercializadora/ventas-por-semana/vendedor/?vendedor="+$scope.vendedor_libreria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info("Todas las ventas de esta semana hechas por " + $scope.libros[0]['vendido_por']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    if($scope.libros[i]['dia'] == 'lunes'){
                        num_l = num_l + parseInt($scope.libros[i]['vendidos']);
                        ventas_l = ventas_l + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'martes'){
                        num_m = num_m + parseInt($scope.libros[i]['vendidos']);
                        ventas_m = ventas_m + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'miercoles'){
                        num_mi = num_mi + parseInt($scope.libros[i]['vendidos']);
                        ventas_mi = ventas_mi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'jueves'){
                        num_ju = num_ju + parseInt($scope.libros[i]['vendidos']);
                        ventas_ju = ventas_ju + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'viernes'){
                        num_vi = num_vi + parseInt($scope.libros[i]['vendidos']);
                        ventas_vi = ventas_vi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'sabado'){
                        num_sa = num_sa + parseInt($scope.libros[i]['vendidos']);
                        ventas_sa = ventas_sa + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'domingo'){
                        num_dom = num_dom + parseInt($scope.libros[i]['vendidos']);
                        ventas_dom = ventas_dom + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }
                }
                $scope.valida = j;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;

                $scope.num_l = num_l; $scope.ventas_l = ventas_l;
                $scope.num_m = num_m; $scope.ventas_m = ventas_m;
                $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
                $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
                $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
                $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
                $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;


            }
            else{
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha hecho ventas');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_libro_func = function () {
        precio = 0; costo= 0; inversion= 0;j=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        var url_libro = "/Chilpancingo/control/comercializadora/ventas-por-semana/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
                $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas en la semana del producto ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    if($scope.libros[i]['dia'] == 'lunes'){
                        num_l = num_l + parseInt($scope.libros[i]['vendidos']);
                        ventas_l = ventas_l + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'martes'){
                        num_m = num_m + parseInt($scope.libros[i]['vendidos']);
                        ventas_m = ventas_m + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'miercoles'){
                        num_mi = num_mi + parseInt($scope.libros[i]['vendidos']);
                        ventas_mi = ventas_mi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'jueves'){
                        num_ju = num_ju + parseInt($scope.libros[i]['vendidos']);
                        ventas_ju = ventas_ju + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'viernes'){
                        num_vi = num_vi + parseInt($scope.libros[i]['vendidos']);
                        ventas_vi = ventas_vi + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'sabado'){
                        num_sa = num_sa + parseInt($scope.libros[i]['vendidos']);
                        ventas_sa = ventas_sa + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }else if($scope.libros[i]['dia'] == 'domingo'){
                        num_dom = num_dom + parseInt($scope.libros[i]['vendidos']);
                        ventas_dom = ventas_dom + (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos'])));
                    }
                }
                $scope.valida = j;
                $scope.ganancias = precio ;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;

                $scope.num_l = num_l; $scope.ventas_l = ventas_l;
                $scope.num_m = num_m; $scope.ventas_m = ventas_m;
                $scope.num_mi = num_mi; $scope.ventas_mi = ventas_mi;
                $scope.num_ju = num_ju; $scope.ventas_ju = ventas_ju;
                $scope.num_vi = num_vi; $scope.ventas_vi = ventas_vi;
                $scope.num_sa = num_sa; $scope.ventas_sa = ventas_sa;
                $scope.num_dom = num_dom; $scope.ventas_dom = ventas_dom;
            }
            else{
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.lunes = false;
    $scope.martes = false;
    $scope.miercoles = false;
    $scope.jueves = false;
    $scope.viernes = false;
    $scope.sabado = false;
    $scope.domingo = false;
    $scope.muestra_lunes = function(){
        if($scope.lunes == false) {
            $scope.lunes = true;
        }
        else if($scope.lunes == true){
            $scope.lunes = false;
        }
    };
        $scope.muestra_martes = function(){
        if($scope.martes == false) {
            $scope.martes = true;
        }
        else if($scope.martes == true){
            $scope.martes = false;
        }
    };
        $scope.muestra_miercoles = function(){
        if($scope.miercoles == false) {
            $scope.miercoles = true;
        }
        else if($scope.miercoles == true){
            $scope.miercoles = false;
        }
    };
        $scope.muestra_jueves = function(){
        if($scope.jueves == false) {
            $scope.jueves = true;
        }
        else if($scope.jueves == true){
            $scope.jueves = false;
        }
    };
        $scope.muestra_viernes = function(){
        if($scope.viernes == false) {
            $scope.viernes = true;
        }
        else if($scope.viernes == true){
            $scope.viernes = false;
        }
    };
        $scope.muestra_sabado = function(){
        if($scope.sabado == false) {
            $scope.sabado = true;
        }
        else if($scope.sabado == true){
            $scope.sabado = false;
        }
    };
        $scope.muestra_domingo = function(){
        if($scope.domingo == false) {
            $scope.domingo = true;
        }
        else if($scope.domingo == true){
            $scope.domingo = false;
        }
    };
});

app_control.controller('ventas_mes_comercializadora_ctrl', function($scope,$http){
    var precio = 0,j=0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;j=0;
        toastr.info("Todas las ventas de este mes");
        var url_inicial = "/Chilpancingo/control/comercializadora/ventas-por-mes/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0)
            {
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;

            }
            else{
                $scope.valida = 0;
                $scope.verifica = 0;
            }

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_vendedor_func = function () {
        precio = 0;
        var url_vendedor = "/Chilpancingo/control/comercializadora/ventas-por-mes/vendedor/?vendedor="+$scope.vendedor_libreria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info("Todas las ventas de hoy hechas por " + $scope.libros[0]['vendido_por']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = parseFloat($scope.libros[i]['precio']) + precio;
                }
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 1;
            }
            else{
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha hecho ventas');
                $scope.verifica = 1;
            }
        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.busca_libro_func = function () {
        precio = 0;j=0;
        var url_libro = "/Chilpancingo/control/comercializadora/ventas-por-mes/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
                $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas del producto ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio']) * (parseInt($scope.libros[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.verifica = 0;
            }
            else {
                $scope.verifica = 0;
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning("Algo pasó :S");
        });
    };
    $scope.ventas_iniciales();
});

app_control.controller('articulos_registrados_ctrl', function ($scope,$http) {
    var precio = 0,costo = 0,inversion = 0,j= 0,k=0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;j=0;k=0;
        toastr.info("mostrando todos los productos registrados");
        var url_inicial = "/Chilpancingo/control/comercializadora/articulos/";
        $http.get(url_inicial).success(function (data) {
            $scope.libros = data;
            if($scope.libros.length != 0)
            {
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.libros[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    k = k + parseInt($scope.libros[i]['no_vendidos']);
                }
                $scope.vendidos = j;
                $scope.restantes = k;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;
            }
            else{
                $scope.valida = 0;
            }

        }).error(function (data) {
            toastr.warning('Algo paso :s');
        });
    };
    $scope.ventas_iniciales();
        $scope.busca_libro_func = function () {
        precio = 0; costo= 0; inversion= 0;j=0;
        var url_libro = "/Chilpancingo/control/comercializadora/articulos/articulo/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
                $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas del producto ' + $scope.libros[0]['nombre']);
                for (var i = 0; i < $scope.libros.length; i++) {
                    precio = (parseFloat($scope.libros[i]['precio'])*(parseInt($scope.libros[i]['vendidos']))) + precio;
                    inversion = (parseFloat($scope.libros[i]['costo'])*(parseInt($scope.libros[i]['vendidos']) + parseInt($scope.productos[i]['no_vendidos']))) + inversion;
                    j = j + parseInt($scope.libros[i]['vendidos']);
                    k = k + parseInt($scope.libros[i]['no_vendidos']);
                }
                $scope.vendidos = j;
                $scope.restantes = k;
                $scope.valida = $scope.libros.length;
                $scope.ganancias = precio;
                $scope.inversion = inversion;
                $scope.resta = precio - inversion;

            }
            else{
                $scope.valida = 0;
                $scope.libros = [];
                $scope.ganancias = 0;
                toastr.warning('No ha ventas de este producto');
            }
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });
    };
});

app_control.controller('actualizar_inventario_ctrl',function($scope,$http){
    $scope.libros;
    $scope.mostrar = false;
    $scope.busqueda = function(){
        var url_libro = "/Chilpancingo/control/libreria/buscar/?libro="+ $scope.busquedaAngular;
        $http.get(url_libro).success(function (data) {
            $scope.libros = data;
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });
        $scope.mostrar = false;
    };

    $scope.buscar_especifico = function(id, $nombre){
        $scope.id = id;
        $scope.nombre_seleccionado = $nombre;
        $scope.mostrar = true;
        var url_libro = "/Chilpancingo/control/libreria/buscar_id/?id_libro="+id[0][0];
        $http.get(url_libro).success(function (data) {
            $scope.contador = data;
            $scope.numero = data.numero;
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });


    };

    $scope.actualizar_existencias = function(){
        console.log($scope.id[0][0]);
        console.log($scope.contador.numero);
        var existencias_a_borrar = $scope.numero - $scope.contador.numero;
        var url_libro = "/Chilpancingo/control/libreria/actualizar_existencias/?id_libro="+$scope.id[0][0]+"&numero="+existencias_a_borrar;
        $http.get(url_libro).success(function (data) {
            toastr.success("Se ha actualizado las existencias del articulo.");
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });
    }
});


app_control.controller('actualizar_inventario_ctrl_cafeteria',function($scope,$http){
    $scope.libros;
    $scope.mostrar = false;
    $scope.busqueda = function(){
        var url_libro = "/Chilpancingo/control/cafeteria/buscar/?libro="+ $scope.busquedaAngular;
        $http.get(url_libro)
            .success(function (data) {
                $scope.libros = data;
            }).error(function (data) {
                toastr.warning('Algo pasó.');
            });
        $scope.mostrar = false;
    };

    $scope.buscar_especifico = function(id, $nombre){
        $scope.id = id;
        $scope.nombre_seleccionado = $nombre;
        $scope.mostrar = true;
        var url_libro = "/Chilpancingo/control/cafeteria/buscar_id/?id_libro="+id[0][0];
        $http.get(url_libro).success(function (data) {
            $scope.contador = data;
            $scope.numero = data.numero;
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });


    };

    $scope.actualizar_existencias = function(){
        console.log($scope.id[0][0]);
        console.log($scope.contador.numero);
        var existencias_a_borrar = $scope.numero - $scope.contador.numero;
        var url_libro = "/Chilpancingo/control/cafeteria/actualizar_existencias/?id_libro="+$scope.id[0][0]+"&numero="+existencias_a_borrar;
        $http.get(url_libro).success(function (data) {
            toastr.success("Se ha actualizado las existencias del articulo.");
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });
    }
});
app_control.controller('actualizar_inventario_ctrl_comercializadora',function($scope,$http){
    $scope.libros;
    $scope.mostrar = false;
    $scope.busqueda = function(){
        var url_libro = "/Chilpancingo/control/comercializadora/buscar/?libro="+ $scope.busquedaAngular;
        $http.get(url_libro).success(function (data) {
            $scope.libros = data;
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });
        $scope.mostrar = false;
    };

    $scope.buscar_especifico = function(id, $nombre){
        $scope.id = id;
        $scope.nombre_seleccionado = $nombre;
        $scope.mostrar = true;
        var url_libro = "/Chilpancingo/control/comercializadora/buscar_id/?id_libro="+id[0][0];
        $http.get(url_libro).success(function (data) {
            $scope.contador = data;
            $scope.numero = data.numero;
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });


    };

    $scope.actualizar_existencias = function(){
        console.log($scope.id[0][0]);
        console.log($scope.contador.numero);
        var existencias_a_borrar = $scope.numero - $scope.contador.numero;
        var url_libro = "/Chilpancingo/control/comercializadora/actualizar_existencias/?id_libro="+$scope.id[0][0]+"&numero="+existencias_a_borrar;
        $http.get(url_libro).success(function (data) {
            toastr.success("Se ha actualizado las existencias del articulo.");
        }).error(function (data) {
            toastr.warning('Algo pasó.');
        });
    }
});

app_control.controller('bitacora_ctrl', function($scope,$http){

    var url = "/Chilpancingo/control/bitacora/get_data/";
    $http.get(url).success(function(data){
        $scope.libros = data;
    }).error(function(){
        toastr.warning('Algo pasó.');
    });
});

app_control.controller('ventas_mes_spec_comercializadora_ctrl', function ($scope, $http){
    $scope.buscar = function(){
        var url = '/Chilpancingo/control/comercializadora/busqueda-anio-mes/?anio=' + $scope.anio_busqueda + '&mes=' + $scope.mes_busqueda
        $http.get(url).success(function (data){
            $scope.libros = data
        }).error(function(){
            toastr.warning('Algo pasó.');
        })
    };
});