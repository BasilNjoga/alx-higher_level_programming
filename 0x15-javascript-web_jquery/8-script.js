#!/usr/bin/node

$(document).ready(function(){
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data, status){
        $("UL#list_movies").text(data);
    });
});