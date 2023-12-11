$("#menu-trigger").click(function () {
  $(".menu").toggleClass("menu-visible");
});

$(".close").click(function () {
  $(".menu").toggleClass("menu-visible");
});

$(".platofuerte-trigger").click(function () {
  console.log("Hola si soy")
  $(".fuertes").toggleClass("fuertes-visible");
});

$(".cerrar2-trigger").click(function () {
  $(".fuertes").toggleClass("fuertes-visible");
});

$(".marbar-trigger").click(function () {
  $(".mar").toggleClass("mar-visible");
});

$(".cerrar-trigger").click(function () {
  $(".mar").toggleClass("mar-visible");
});

$(".ensaladas-trigger").click(function () {
  $(".sopas").toggleClass("sopas-visible");
});

$(".cerrar3-trigger").click(function () {
  $(".sopas").toggleClass("sopas-visible");
});
