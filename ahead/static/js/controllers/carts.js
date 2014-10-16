function getCookie(c_name) {
  if (document.cookie.length>0) {
    c_start = document.cookie.indexOf(c_name + "=")
    if (c_start!=-1) { 
      c_start=c_start + c_name.length+1;
      c_end=document.cookie.indexOf(";",c_start)
      if (c_end==-1) 
        c_end = document.cookie.length;
      return unescape(document.cookie.substring(c_start,c_end))
    } 
  }
  return ""
}

function setCookie(c_name,value,expiredays) {
  var exdate=new Date()
  exdate.setDate(exdate.getDate()+expiredays)
  document.cookie=c_name+ "=" + escape(value)+
  ((expiredays==null) ? "" : "; expires="+exdate.toGMTString()) + "; path=/"
}

var cartTools = {

  getMoney: function() {
    var carts = this.getCarts();
    var money = 0;

    if ( carts.length < 1 ) return 0;

    for (var i in carts) {
      money += carts[i]['price'] * carts[i]['num']
    }
    return money;
  },

  setMoney: function() {
    $('.cart-money').html(this.getMoney());
  },

  getCarts: function() {
    return getCookie('carts') == "" ? {} : JSON.parse(getCookie('carts'));
  },

  addCarts: function(id, name, pic, price, num) {
    var carts = this.getCarts();
    if (carts[id]) {
      carts[id]['num'] += num;
    } else {
      carts[id] = {
        name: name,
        pic: pic,
        price: price,
        num: num,
      }
    }
    setCookie('carts', JSON.stringify(carts));
    this.setMoney();
  },

  emptyCarts: function() {
    setCookie('carts', "")
  },
};

(function($){
  
}(this.jQuery));