/**
 * Created by RubenMurga on 13/08/15.
 */

var busqueda_libro = angular.module('BLibreria', []);

  busqueda_libro.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });

busqueda_libro.controller('LibreriaCtrl', function($scope, $http){

    $scope.buscarProducto = function(){
        var url = "/Chilpancingo/libreria/agregar-producto/busqueda-articulo/?nombre_art="+$scope.libreria_input;
        $http.get(url).success(function(data){
            if(data.nombre)
                toastr.warning("Ya existe un libro con ese nombre, mejor agrega articulos al libro en el formulario de abajo.");
        }).error(function (data) {

        });
    };

    $scope.calcular_precio = function(){
        var porcentaje = parseFloat(($scope.porcentaje_input)/100);
        $scope.precio_input = parseFloat($scope.costo_input) + parseFloat(($scope.costo_input)*porcentaje);
    }
});

var busqueda_comercializadora = angular.module('BComercializadora', []);

busqueda_comercializadora.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });

  busqueda_comercializadora.controller('ComercializadoraCtrl', function($scope, $http){

    $scope.buscarProducto = function(){
        var url = "/Chilpancingo/comercializadora/agregar-producto/busqueda-articulo/?nombre_art="+$scope.libreria_input;
        $http.get(url).success(function(data){
            if(data.nombre)
                toastr.warning("Ya existe un libro con ese nombre, mejor agrega articulos al libro en el formulario de abajo.");
        }).error(function (data) {

        });
    };

    $scope.calcular_precio = function(){
        var porcentaje = parseFloat(($scope.porcentaje_input)/100);
        $scope.precio_input = parseFloat($scope.costo_input) + parseFloat(($scope.costo_input)*porcentaje);
    }
});




var busqueda_categoria = angular.module('LCategoria',[]);
busqueda_categoria.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

busqueda_categoria.controller('CategoriaCtrl', function($scope, $http){
    $scope.buscarCategoria = function(){
        var url = "/Chilpancingo/libreria/buscar/categoria-angular/?nombre_cat="+$scope.categoria_input;
        $http.get(url).success(function(data){
            toastr.warning('Ya existe una categoria con ese nombre, ingresa otro.');
        }).error(function(data){

        });
    };
});





var busqueda_cafeteria = angular.module('ACafeteria', []);
busqueda_cafeteria.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

});
busqueda_cafeteria.controller('CafeteriaCtrl', function ($scope, $http) {
    $scope.buscar_producto = function() {
        var url = "/Chilpancingo/cafeteria/buscar/articulo/?nombre_art="+$scope.cafeteria_input;
        $http.get(url).success(function (data) {
            if(data.nombre)
                toastr.warning("Ya existe un producto con ese nombre, mejor agrega articulos al producto en el formulario de abajo :D");
        }).error(function (data) {

        });
    };
    $scope.calcular_precio_cafeteria = function(){
        var porcentaje = parseFloat(($scope.porcentaje_input_cafeteria)/100);
        $scope.precio_pro_cafeteria = parseFloat($scope.costo_input_cafe) + parseFloat(($scope.costo_input_cafe)*porcentaje);
    };
});
