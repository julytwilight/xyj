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
    var password = $('#reg_password').val();
    var password2 = $('#reg_password2').val();

    if (username === "" || username.length < 4 || username.length > 30){
      $('#reg_username').addClass('error');
      return false;
    }

    if (/[\w-]+@[\w-]+.[\w]+/.test(email) === false){
      $('#reg_email').addClass('error');
      return false;
    }

    if (password.length < 6) {
      $('#reg_password').addClass('error');
      return false;
    };

    if (password != password2) {
      $('#reg_password2').addClass('error');
      return false;
    }
  });
})(this.jQuery);