define(function(){

	"use strict";
	/**
	 * @constructor CrsfSafeMixin
	 */
	var CrsfSafeMixin = function () {};

	CrsfSafeMixin.prototype = {

		csrfSafeMethod: function (method) {
			// these HTTP methods do not require CSRF protection
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		},

		sameOrigin: function (url) {
			// url could be relative or scheme relative or absolute
			var location = document.location,
				host = location.host, // host + port
				protocol = location.protocol,
				sr_origin = '//' + host,
				origin = protocol + sr_origin;
			// Allow absolute or scheme relative URLs to same origin
			return (url === origin || url.slice(0, origin.length + 1) === origin + '/') ||
				(url === sr_origin || url.slice(0, sr_origin.length + 1) === sr_origin + '/') ||
				// or any other URL that isn't scheme relative or absolute i.e relative.
				!(/^(\/\/|http:|https:).*/.test(url));
		}

	};

	return CrsfSafeMixin;
});