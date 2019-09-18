function imprSelec(nombre) {
    var ficha = document.getElementById(nombre);
    var ventimp = window.open(' ', 'popimpr');

      ventimp.document.write( ficha.innerHTML );

      ventimp.document.close();

      ventimp.print( );

      ventimp.close();

}
function seleccionarInput(){
  $('#productoIn').focus();
}


var caja = angular.module('CRegistradora', []);

  caja.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });


  caja.controller('TodoCtrl', function($scope, $http){
    $scope.productos = [
    ];

    $scope.agregarProducto = function(){
          var url = "/Chilpancingo/libreria/buscando/caja-registradora/?codigo="+$scope.productoInput;
          $http.get(url).success(function(data,status,headers,config){
            $scope.productos.push({codigo:$scope.productoInput,cancelado:false, nombre:data['nombre'], precio:data['precio'], id: data['id']});
            $scope.productoInput = '';
            seleccionarInput();
          }).error(function(data,status,headers,config){
            toastr.error("No se ha podido agregar a la venta porque el producto no está registrado, favor de registrarlo.");
          });
        var tiempo = new Date();
        $scope.dia = tiempo.getDate()+1;
        $scope.mes = tiempo.getMonth()+1;
        $scope.anio = tiempo.getFullYear();
        $scope.hora = tiempo.getHours();
        $scope.minutos = tiempo.getMinutes();

    };

    $scope.getTotalProductos = function() {
      $scope.totalProductos = 0;
      for(var i = 0; i < $scope.productos.length;i++){
        if($scope.productos[i]['cancelado'] == false){
          $scope.totalProductos = $scope.totalProductos +1;
        }
      }
      return $scope.totalProductos;
    };

    $scope.getPagar = function(){
      $scope.pagar = 0.0;
        for(var i = 0; i < $scope.productos.length;i++){
          if($scope.productos[i]['cancelado'] == false){
             $scope.pagar += parseFloat($scope.productos[i]['precio']);
          }
        }
      return $scope.pagar;
    };
    $scope.getCambio = function(){
      $scope.pagar = 0.0;
        for(var i = 0; i < $scope.productos.length;i++){
          if($scope.productos[i]['cancelado'] == false){
             $scope.pagar += parseFloat($scope.productos[i]['precio']);
          }
        }
      if($scope.pagar == 0 || $scope.dineroInput == 0){
        return 0;
      }
      else {
        return ($scope.dineroInput - $scope.pagar);
      }
    };

    $scope.mandarVenta = function(){

        for (var i = 0; i < $scope.productos.length; i++) {
          if ($scope.productos[i]['cancelado'] == false) {
            var url = "/Chilpancingo/libreria/caja-registradora/venta/?codigo=" + $scope.productos[i]['id'] + "&cancelado=0";
            $http.get(url).success(function (data) {
                toastr.success("Se ha hecho la venta del producto " + data['nombre']);
            }).error(function (data) {
              toastr.error("Ha ocurrido un error :C");
            });
          }else{
             var url = "/Chilpancingo/libreria/caja-registradora/venta/?codigo=" + $scope.productos[i]['id']+"&cancelado=1";
            $http.get(url).success(function (data) {
                toastr.warning("Se ha cancelado la venta del producto "+ data['nombre']);
                j++;
            }).error(function (data) {
              toastr.error("Ha ocurrido un error :C");
            });
          }
        }
      $scope.productos = [];
        imprSelec('Imprime');

    };

  });