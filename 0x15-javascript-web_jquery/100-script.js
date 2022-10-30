#!/usr/bin/node

$(function(){
document.querySelector('header').style.color = "#FF0000";
});
document.addEventListener("DOMContentLoaded",() => { 
    document.getElementById("msg1").innerHTML = document.URL.toString();
 });