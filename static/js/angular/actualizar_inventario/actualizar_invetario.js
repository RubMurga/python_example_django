var app = angular.module('actualizarApp', []);

  app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });


app.controller('ActualizarCtrl', function($scope,$http){
    alert("hola");
});