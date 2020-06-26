$(document).ready(function() {
  for (i = 0; i < 11; i++) {
    var owl = $(".owl-col-"+String(i));

    owl.owlCarousel({
        items : i, //10 items above 1000px browser width
        itemsDesktop : [1000,Math.min(1,parseInt(i/2))], //5 items between 1000px and 901px
        itemsDesktopSmall : [900,Math.min(1,parseInt(i/3))], // betweem 900px and 601px
        itemsTablet: [600,Math.min(1,parseInt(i/5))], //2 items between 600 and 0
        itemsMobile : false // itemsMobile disabled - inherit from itemsTablet option
    });
  }


});
