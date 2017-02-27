var myStore = angular.module("myStore", ['storeReviews','ngResource'])

myStore.config(function($resourceProvider){
    $resourceProvider.defaults.stripTrailingSlashes = false
})