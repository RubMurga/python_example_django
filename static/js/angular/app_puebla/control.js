var app_control = angular.module('AppControl',[]);
app_control.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});



app_control.controller('vendedoresCtrl', function($scope, $http){
$scope.ventas_vendedores_fun = function() {
        var urlVendedores = "/Puebla/control/obtener/vendedores/";
        $http.get(urlVendedores).success(function (data) {
            $scope.ventas_vendedores = data;
        }).error(function (data) {
            toastr.warning('algo paso');
        });
    };
    $scope.ventas_vendedores_fun();
});



app_control.controller('ventas_dia_libreria_ctrl', function($scope,$http){
    var precio = 0,j=0;
    $scope.ventas_iniciales = function() {
        precio = 0; j=0;
        toastr.info("Todas las ventas de hoy");
        var url_inicial = "/Puebla/control/libreria/ventas-por-dia/inicial/";
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
        var url_vendedor = "/Puebla/control/libreria/ventas-por-dia/vendedor/?vendedor="+$scope.vendedor_libreria ;
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
        var url_libro = "/Puebla/control/libreria/ventas-por-dia/libro/?libro="+ $scope.libro_input;
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
        precio = 0; costo= 0; inversion=0;j=0;
        toastr.info("Todas las ventas de este mes");
        var url_inicial = "/Puebla/control/libreria/ventas-por-mes/inicial/";
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
        var url_vendedor = "/Puebla/control/libreria/ventas-por-mes/vendedor/?vendedor="+$scope.vendedor_libreria ;
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
        var url_libro = "/Puebla/control/libreria/ventas-por-mes/libro/?libro="+ $scope.libro_input;
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

app_control.controller('ventas_dia_cafeteria_ctrl', function($scope,$http){
    var precio = 0,costo = 0,inversion = 0,j=0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;j=0;
        toastr.info("Todas las ventas de hoy");
        var url_inicial = "/Puebla/control/cafeteria/ventas-por-dia/inicial/";
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
        var url_vendedor = "/Puebla/control/cafeteria/ventas-por-dia/vendedor/?vendedor="+$scope.vendedor_cafeteria ;
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
        var url_libro = "/Puebla/control/cafeteria/ventas-por-dia/producto/?producto=" + $scope.producto_input;
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
        precio = 0; costo= 0; inversion=0;j=0;k=0;
        toastr.info("Todas las ventas de este mes");
        var url_inicial = "/Puebla/control/cafeteria/ventas-por-mes/inicial/";
        $http.get(url_inicial).success(function (data) {
            $scope.productos = data;
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
        var url_vendedor = "/Puebla/control/cafeteria/ventas-por-mes/vendedor/?vendedor="+$scope.vendedor_cafeteria ;
        $http.get(url_vendedor).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0) {
                toastr.info("Todas las ventas de hoy hechas por " + $scope.productos[0]['vendido_por']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = parseFloat($scope.productos[i]['precio']) + precio;
                }
                $scope.verifica = 1;
                $scope.valida = $scope.productos.length;

            }
            else{
                $scope.verifica = 1;
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
        precio = 0;
        var url_libro = "/Puebla/control/cafeteria/ventas-por-mes/producto/?producto="+ $scope.producto_input;
        $http.get(url_libro).success(function (data) {
            $scope.productos = data;
            if($scope.productos.length != 0) {
                toastr.info('Mostrando las ventas del producto ' + $scope.productos[0]['nombre']);
                for (var i = 0; i < $scope.productos.length; i++) {
                    precio = (parseFloat($scope.productos[i]['precio'])*(parseInt($scope.productos[i]['vendidos']))) + precio;
                    j = j + parseInt($scope.productos[i]['vendidos']);
                }
                $scope.vendidos = j;
                $scope.valida = $scope.productos.length;
                $scope.ganancias = precio;
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

app_control.controller('ventas_semana_libreria_ctrl', function($scope,$http){
    var precio = 0,costo = 0,inversion = 0,j=0;
    var ventas_l= 0,ventas_m = 0, ventas_mi = 0, ventas_ju = 0, ventas_vi = 0, ventas_sa= 0,ventas_dom = 0;
    var num_l =0,num_m=0, num_mi = 0, num_ju = 0, num_vi = 0, num_sa = 0, num_dom = 0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;
        ventas_l= 0;ventas_m = 0; ventas_mi = 0; ventas_ju = 0; ventas_vi = 0; ventas_sa= 0;ventas_dom = 0;
        num_l =0;num_m=0; num_mi = 0; num_ju = 0; num_vi = 0; num_sa = 0; num_dom = 0;
        toastr.info("Todas las ventas de esta semana");
        var url_inicial = "/Puebla/control/libreria/ventas-por-semana/inicial/";
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
        var url_vendedor = "/Puebla/control/libreria/ventas-por-semana/vendedor/?vendedor="+$scope.vendedor_libreria ;
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
        var url_libro = "/Puebla/control/libreria/ventas-por-semana/libro/?libro="+ $scope.libro_input;
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
        var url_inicial = "/Puebla/control/cafeteria/ventas-por-semana/inicial/";
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
        var url_vendedor = "/Puebla/control/cafeteria/ventas-por-semana/vendedor/?vendedor="+$scope.vendedor_cafeteria ;
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
        var url_libro = "/Puebla/control/cafeteria/ventas-por-semana/producto/?producto="+ $scope.producto_input;
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
        precio = 0; costo= 0; inversion=0;j=0;k=0;
        toastr.info("mostrando todos los libros registrados");
        var url_inicial = "/Puebla/control/libreria/libros/";
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
        var url_libro = "/Puebla/control/libreria/libros/libro/?libro="+ $scope.libro_input;
        $http.get(url_libro).success(function (data) {
                $scope.libros = data;
            if($scope.libros.length != 0) {
                toastr.info('Mostrando las ventas del libro ' + $scope.libros[0]['nombre']);
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
            toastr.warning('Algo paso :s');
        });
    };
});

app_control.controller('productos_registrados_ctrl', function ($scope,$http) {
   var precio = 0,costo = 0,inversion = 0,j= 0,k=0;
    $scope.ventas_iniciales = function() {
        precio = 0; costo= 0; inversion=0;
        j = 0;k=0;
        toastr.info("Mostrando todos los productos registrados");
        var url_inicial = "/Puebla/control/cafeteria/productos/";
        $http.get(url_inicial).success(function (data) {
            $scope.productos = data;
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
        var url_libro = "/Puebla/control/cafeteria/productos/producto/?producto="+ $scope.producto_input;
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
        var url_inicial = "/Puebla/control/comercializadora/ventas-por-dia/inicial/";
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
        var url_vendedor = "/Puebla/control/comercializadora/ventas-por-dia/vendedor/?vendedor="+$scope.vendedor_libreria ;
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
        var url_libro = "/Puebla/control/comercializadora/ventas-por-dia/libro/?libro="+ $scope.libro_input;
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
        var url_inicial = "/Puebla/control/comercializadora/ventas-por-semana/inicial/";
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
        var url_vendedor = "/Puebla/control/comercializadora/ventas-por-semana/vendedor/?vendedor="+$scope.vendedor_libreria ;
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
        var url_libro = "/Puebla/control/comercializadora/ventas-por-semana/libro/?libro="+ $scope.libro_input;
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
        var url_inicial = "/Puebla/control/comercializadora/ventas-por-mes/inicial/";
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
        var url_vendedor = "/Puebla/control/comercializadora/ventas-por-mes/vendedor/?vendedor="+$scope.vendedor_libreria ;
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
        var url_libro = "/Puebla/control/comercializadora/ventas-por-mes/libro/?libro="+ $scope.libro_input;
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
        var url_inicial = "/Puebla/control/comercializadora/articulos/";
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
        var url_libro = "/Puebla/control/comercializadora/articulos/articulo/?libro="+ $scope.libro_input;
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
            toastr.warning('Algo paso :s');
        });
    };
});