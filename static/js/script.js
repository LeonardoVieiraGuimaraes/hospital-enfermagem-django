// alert("funcionando")

$(document).ready(function () {
	$("#id_paciente").select2({
		theme: "bootstrap-5",
		width: $(this).data("width")
			? $(this).data("width")
			: $(this).hasClass("w-100")
			? "100%"
			: "style",
	});
	$("#id_usuario").select2({
		theme: "bootstrap-5",
		width: $(this).data("width")
			? $(this).data("width")
			: $(this).hasClass("w-100")
			? "100%"
			: "style",
	});
		$("#id_cirurgia_segura").select2({
		theme: "bootstrap-5",
		width: $(this).data("width")
			? $(this).data("width")
			: $(this).hasClass("w-100")
			? "100%"
			: "style",
	});
});


function radioOcultar(event){

	console.log(event);
	let inputName = event.name;
	// console.log(inputName);
	let inputValue = event.value;
	console.log(inputValue);

	let seSim = ["se_sim", "se_sim_01", "se_sim_02", "se_sim_03", "se_sim_04"];


	for (let i in seSim) {
		// let inputSelectdiv = document.getElementById(`div_id_${inputName}_${seSim[i]}`);

		let inputSelectinputs = document.getElementsByName(`${inputName}_${seSim[i]}`);
		// console.log(inputSelectinputs)

		for (i in inputSelectinputs) {
			if (inputSelectinputs[i] != null) {
				if (inputValue == "Sim") {
					inputSelectinputs[i].disabled = false;
					inputSelectinputs[i].required = true;

				}
				else {
					inputSelectinputs[i].disabled = true;
					inputSelectinputs[i].required = false;
					// if (inputSelectinputs[i].type == "text" || inputSelectinputs[i].type == "number") {
					// 	inputSelectinputs[i].value = "";
					// }
					// if (inputSelectinputs.type == "radio") {
					// inputSelectinputs.checked = true;
					// }
				}

			}
		}
		let seNao = ["se_nao"]
		for (let i in seNao) {
			let inputSelectinputn = document.getElementsByName(`${inputName}_${seNao[i]}`);
			for (i in inputSelectinputn) {
				if (inputSelectinputn[i] != null) {
					if (inputValue == "Não") {
						inputSelectinputn[i].disabled = false;
						inputSelectinputn[i].required = true;

					}
					else {
						inputSelectinputn[i].disabled = true;
						inputSelectinputn[i].required = false;
						// inputSelectinputn[i].value = "";
						// if (inputSelectinputn[i].type == "radio") {
						// 	inputSelectinputn[i].checked = false;
						// }

					}

				}
			}
		}
	}
}

function CheckBoxOcultar(event){


	let inputName = event.name;


	let inputValue = event.value;

	let inputchecked = event.checked;


	let inputSelectinputs = document.getElementsByName(`${inputName}_out`);
	console.log(inputchecked)

	if (inputValue == "Out" && inputchecked == true) {

				inputSelectinputs[0].disabled = false;
				inputSelectinputs[0].required = true;

			}
	else {
				inputSelectinputs[0].disabled = true;
				inputSelectinputs[0].required = false;

			}



}
