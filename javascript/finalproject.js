$("document").ready(function() {

				$('#info2').click(function(){

					$('html, body').animate({
						scrollTop: $("#info").offset().top
					}, 1000);

				 });

				$('#experience2').click(function(){

					$('html, body').animate({
						scrollTop: $("#experience").offset().top
					}, 1000);

				 });

					$('#drop').click(function(){

					$('html, body').animate({
						scrollTop: $("#top").offset().top
					}, 1000);

				 });

         $('#droppic').click(function(){

         $('html, body').animate({
           scrollTop: $("#top").offset().top
         }, 1000);

        });

});
