$("document").ready(function(){
  function darken(){
    $('span').css({'opacity':.75});
  }
  $('span').mouseenter(darken);
  $('a').mouseenter(darken);

  function lighten(){
    $('span').css({'opacity':.6});
  }
  $('span').mouseleave(lighten);
  $('a').mouseleave(lighten);

});
