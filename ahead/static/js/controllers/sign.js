(function($){
  // Register Page
  //----------------------------------------//
  $(document).ready(function(){
    var url = window.location.href;
    if (url.match('welcome')) {
      $('.reg-button').click();
    }
  });


  // Register Form
  //----------------------------------------//
  $('.register').submit(function(){
    alert('aa');
    return false;
  });
})(this.jQuery);