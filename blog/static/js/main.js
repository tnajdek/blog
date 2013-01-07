require.config({
	paths: {
		"jquery": "libs/require-jquery"
	},
	shim: {
	// 'bootstrap': ['jquery']
	}
});

require(["jquery", "bootstrap"], function ($) {
	"use strict";
});