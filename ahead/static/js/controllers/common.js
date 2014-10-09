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
  ((expiredays==null) ? "" : "; expires="+exdate.toGMTString())
}

function CartsViewModel() {
  this.items = [];
  this.sign = '￥';
  this.money = ko.observable(0);
  this.getPrice = function() {
    if (this.itemsLength() < 1) {
      return 0;
    }
  }
  this.itemsLength = function() {
    return this.items.length;
  }
  this.addCart = function(id, img, price, num) {
  }
}

ko.applyBindings(CartsViewModel());