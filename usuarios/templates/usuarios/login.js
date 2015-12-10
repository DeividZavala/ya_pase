(function(){
	var formulario = document.formulario_registro,
		elementos = formulario.elements;

	// funciones

	var ValidarInputs = function(){
		for(var i = 0; i < elementos.length; i++){
			if (elementos[i].type == "text" || elementos[i].type == "email" || elementos[i].type == "password") {
				if (elementos[i].value == 0) {
					console.log("El campo " + elementos[i].name + ' esta incompleto')
					elementos[i].className = elementos[i].className + ' error'
					return false;
				}else{
					elementos[i].className = elementos[i].className.replace("error", "")
				}
			}
		}

		return true;
	};

	var validarCheckbox = function(){
		var opciones = document.getElementsByName('terminos'),
			resultado = false;
		for(var i = 0; i < elementos.length; i++){
			if (elementos[i].type == "checkbox") {
				for (var o = 0; o < opciones.length; o++){
					if (opciones[o].checked) {
						resultado = true;
						break;
					}
				}
			if (resultado == false) {
				elementos[i].parentNode.className = elementos[i].parentNode.className + " error"
				console.log('El checkbox no esta seleccionado');
				return false;
			}else {
				elementos[i].parentNode.className = elementos[i].parentNode.className.replace(" error", "");
				return true
			}

			}
		}
	}

	var enviar = function(e){
		if (!ValidarInputs()){
			console.log('Falto validar los Input');
			e.preventDefault();
		}else if(!validarCheckbox()){
			console.log('Falto validar los Checkbox');
			e.preventDefault();
		}else{
			console.log('Enviar');
			e.preventDefault();
		}
	};

	//Funciones blur y focus

	var focusInput = function(){
		this.parentElement.children[1].className = "label active";
		this.parentElement.children[0].className = this.parentElement.children[0].className.replace("error", "");
	};

	var blurInput = function(){
		if (this.value <= 0) {
			this.parentElement.children[1].className = "label";
			this.parentElement.children[0].className = this.parentElement.children[0].className + " error";
		};
	};

	// Eventos

	formulario.addEventListener("submit", enviar);

	for (var i = 0; i < elementos.length; i++){
		if(elementos[i].type == "text" || elementos[i].type == "email" || elementos[i].type == "password"){
			elementos[i].addEventListener("focus", focusInput);
			elementos[i].addEventListener("blur", blurInput);
		};
	};

}())