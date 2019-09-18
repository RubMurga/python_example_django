/**
 * Created by RubenMurga on 12/08/15.
 */
var registro = angular.module('RegistroAngular', []);
  registro.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });

registro.controller('TodoCtrl', function($scope,$http){
    $scope.buscar_usuario = function(){
        var url = "/usuario/buscar-usuario/?usuario="+$scope.user_input;
        $http.get(url).success(function(data){
            toastr.error("Ese nombre de usuario ya existe");
        }).error(function(data){
           toastr.success("Ese nombre de usuario está disponible");
        });
    };

    $scope.verificar_pass = function () {
        if($scope.pass2 === $scope.pass1){
            toastr.success("Las contraseñas coinciden");
        }
        else{
            toastr.error("Favor de introducir contraseñas iguales");
        }
    };

});

