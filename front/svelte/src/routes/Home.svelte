<script>
	import {fade, fly} from "svelte/transition";

	let imgGenererCR = 'img/genererCR.png';
	let imghistoriqueCR = 'img/historiqueCR.png';

	function customFade(node, {
	delay = 0,
	duration = 800
	}) {
	const o = +getComputedStyle(node).opacity;

	return {
		delay,
		duration,
		css: t => `opacity: ${t * o}`
	};
}
</script>

<!--Breadcrump navigation-->

<div class="indent">
	<p class="display-4">AubaySum App</p>
	<hr class="line" />
</div>

<div class="row">
	<div  class="col md-6 m-5">
		<h3 in:fly={{x :-5000 , duration: 1500}}>Générer automatiquement votre CR</h3>
		<br />
		<p  in:fly={{x :-5000 , duration: 1500}}  style="text-align: justify; font-size : 1.2em;">
			En quelques clics, générer votre compte-rendu de réunion à partir
			d'un fichier audio au format MP3, MP4 ou WAV ou à partir d'un texte.
			AubaySum vous proposera deux versions du compte-rendu générées par
			mBARThez et CamemBERT que vous pourrez éditer à votre guise pour
			corriger d'éventuelles erreurs.
			<br />La génération peut prendre <strong>plusieurs minutes</strong>,
			une notification vous sera envoyée lorsque celle-ci sera terminée.
		</p>
		<br />
		<p >
			<a in:customFade={{delay:1500}} class="btn btn-primary" href="#/GeneratorCR/"
				>Générer un CR <i class="bi bi-gear-fill" /></a
			>
		</p>
	</div>
	<div class="col md-6 m-5 text-right">
		<img in:customFade={{delay:500}} class="img_homepage"  src={imgGenererCR} alt="image générer CR" />
	</div>
</div>
<div class="row" style="background-color: rgba(0, 0, 0, 0.05) !important;">
	<div class="col md-6 m-5 text-left">
		<img
			in:customFade={{delay:500}}
			class="img_homepage"
			src={imghistoriqueCR}
			alt="image historique CR"
		/>
	</div>
	<div class="col md-6 m-5">
		<h3  in:fly={{x :5000 , duration: 1500}}>Consulter l’historique des CR générés</h3>
		<br />
		<p  in:fly={{x :5000 , duration: 1500}} style="text-align: justify; font-size : 1.2em;">
			Consultez les comptes-rendus précédemment générés et faites des
			recherches par projet, par participants ou par date. Vous pourrez en
			suite exporter le compte-rendu selectionné en PDF.
		</p>
		<br />
		<p>
			<a in:customFade={{delay:1500}}  class="btn btn-outline-secondary" href="#/HistoriqueCR"
				>Historique des CR <i class="bi bi-file-text" /></a
			>
		</p>
	</div>
</div>