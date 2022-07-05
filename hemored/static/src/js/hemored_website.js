odoo.define('website.website', function (require) {
'use strict';

    console.log("Odoo javascript");

});


$(document).on('click', '#btn_registrar', function (e) {
        e.preventDefault();
        var bandera = true

		var codrenipress = "";
		var codrenipress_num = 0;
		var telefono = "";
		var email = "";
		var tipo = "";
		var medico = "";
		var anexo = "";
		var celular = "";
		var web = True;

		codrenipress = $('#txtcodrenipress').val();
		telefono = $('#txttelefono').val();
		email = $('#txtemail').val();
		tipo = $('#cmbtipo').val();
		medico = $('#txtmedico').val();
		anexo = $('#txtanexo').val();
		celular = $('#txtcelular').val();
		$('#cmbrweb').val(web);

		if(codrenipress.length != 8){
			alert('Alto! codigo Renipress solo debe tener 8 dígitos');

			return false;
		}else{
			if(isNaN(codrenipress)){

				alert('Alto! codigo Renipress solo debe tener dígitos');
				return false;
			}
		}

		if(telefono.length < 6){
			alert('Alto! Telefono debe tener mas de 6 dígitos');

			return false;
		}else{
			if(isNaN(telefono)){

				alert('Alto! Telefono solo debe tener dígitos');
				return false;
			}
		}

		if(isNaN(celular)){

			alert('Alto! Celular solo debe tener dígitos');
			return false;
		}else{
      if(celular.length < 9){
        alert('Alto! Telefono debe tener mas de 9 dígitos');

        return false;
      }
		}

		if (bandera) {
			alert('Validaciones Superadas');
		}

});
