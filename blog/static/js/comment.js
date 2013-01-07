define(["jquery", "crsfsafemixin", "handlebars", "utils"], function ($, CrsfSafeMixin) {

	"use strict";

	var Comment = function () {
		var that = this;
		that.init();
	};

	Comment.prototype = {

		init: function () {
			this.cacheElements();
			this.bindEvents();
		},

		cacheElements: function () {
			this.$form = $('form');
			this.commentTemplate = Handlebars.compile($('#comment-template').html());
			this.$commentsList = $('.comments-list');
		},

		bindEvents: function () {
			var that = this,
				$textarea = that.$form.find('textarea'),
				$form = that.$form;
			$form.on('submit', that.submit.bind(this));
			$textarea.on('keyup', that.enableSubmit.bind(this));
		},

		enableSubmit: function (e) {
			var that = this,
				textarea = e.target || e.srcElement,
				$button = that.$form.find('button');

			$button.prop('disabled',
				!(textarea.value.trim().length > 10));
		},

		render: function () {
			var that = this,
				commetListHtml = that.$commentsList,
				commentTpl = that.commentTemplate,
				commentObject = that.commentObject;

			if (Object.keys(commentObject)) {
				if (!commetListHtml.html().trim()) {
					commetListHtml.html(commentTpl(commentObject));
					return;
				}
				commetListHtml.append(commentTpl(commentObject));
			}
		},

		submit: function (e) {
			e.preventDefault();
			var that = this,
				form = e.target || e.srcElement,
				csrftoken = Utils.getCookie('csrftoken');
			$.ajax({
				data: $(form).serialize(),
				url: form.action,
				type: form.method,
				dataType: 'json',
				beforeSend: function (xhr, params) {
					if (!that.csrfSafeMethod(params.type) && that.sameOrigin(params.url)) {
						xhr.setRequestHeader("X-CSRFToken", csrftoken);
					}
				},
				success: function (resp, status, xhr) {
					console.log(status);
					// console.log(JSON.parse(resp.data).fields);
					that.commentObject = resp.data || {};
					if (resp.error) {

					} else {
						that.render();
					}
				},
				error: function (response, status, errorThrown) {
					// console.log(response, status);
				}
			});

		}

	};

	Utils.augment(Comment, CrsfSafeMixin);
	Utils.registerComponent("Comment", Comment);
	return Comment;

});