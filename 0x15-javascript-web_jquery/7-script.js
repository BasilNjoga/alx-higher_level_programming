#!/usr/bin/node

$(document).ready(function(){
    $.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function(name, status){
        $("DIV#character").text(name);
    });
});