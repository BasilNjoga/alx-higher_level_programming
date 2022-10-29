#!/usr/bin/node

$(document).ready(function(){
    $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data, status){
        $("DIV#hello").text(hello);
    });
});