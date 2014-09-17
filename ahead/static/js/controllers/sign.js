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
    var username = $('#reg_username').val();
    var email = $('#reg_email').val();
    var password = $('reg_password').val();
    var password2 = $('reg_password2').val();

    if (username === "")
    return false;
  });
})(this.jQuery);