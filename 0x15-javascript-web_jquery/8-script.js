#!/usr/bin/node

$(document).ready(function(){
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data, status) {
        $.each(data, function(n) {
          $("UL#list_movies").text(n + ': ' + data.title);
        });
        alert(status);
      }, "json");
    });