var Utils = {

	getCookie: function(name) {
		var cookieValue = null,
			cookies,
			cookie,
			i;
		if (document.cookie && document.cookie != '') {
			cookies = document.cookie.split(';');
			for (i = 0; i < cookies.length; i++) {
				cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	},

	extend: function (destination, source) {
		for (var k in source) {
			if (source.hasOwnProperty(k)) {
					destination[k] = source[k];
				}
			}
		return destination; 
	},

	registerComponent: function (name, constr) {
		// var componentName = 'd' + name;
		// window[name] = constr;	
		console.log(typeof constr);
		if (typeof constr !== 'undefined' && typeof constr === "function") {
			window[name] = constr;
		}
	},

	// Extend an existing object with a method from another
	augment: function ( receivingClass, givingClass ) {
 
		// only provide certain methods
		if ( arguments[2] ) {
			for ( var i = 2, len = arguments.length; i < len; i++ ) {
				receivingClass.prototype[arguments[i]] = givingClass.prototype[arguments[i]];
			}
		} else { // provide all methods
			for ( var methodName in givingClass.prototype ) {
	 
			// check to make sure the receiving class doesn't
			// have a method of the same name as the one currently
			// being processed
				if ( !Object.hasOwnProperty(receivingClass.prototype, methodName) ) {
					receivingClass.prototype[methodName] = givingClass.prototype[methodName];
				}

			// Alternatively:
			// if ( !receivingClass.prototype[methodName] ) {
			//  receivingClass.prototype[methodName] = givingClass.prototype[methodName];
			// }
			}
		}
	}

}