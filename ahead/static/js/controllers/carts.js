var cartTools = {

  getMoney: function() {
    var carts = this.getCarts();
    var money = 0;

    if ( carts.length < 1 ) return 0;

    for (var i in this.carts) {
      money += this.carts[i]['price'] * this.carts[i]['num']
    }
    return money;
  },

  getCarts: function() {
    return getCookie('carts') == "" ? {} : JSON.parse(getCookie('carts'));
  },

  addCarts: function(id, name, pic, price, num) {
    
  },

  emptyCarts: function() {
    setCookie('carts', "")
  },
}