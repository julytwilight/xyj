(function($){

  // Navigation Current
  var url = window.location.href;
  if (url.match('yummy')) {
    $('.yummy').addClass('current');
  } else if (url.match('blog')) {
    $('.blog').addClass('current');
  } else if (url.match('about')) {
    $('.about').addClass('current');
  } else {
    $('.homepage').addClass('current');
  }
})(this.jQuery);