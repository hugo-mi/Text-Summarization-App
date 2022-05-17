<script>
	import { onMount, tick } from "svelte";
	import { jsPDF } from "jspdf";
	import { crJSON } from '../components/store.js';
	import ResetButton from '../components/resetButton.svelte';
	import Notification from "../components/notificationHandler.svelte";

	export let params = {};
	console.log(params);
	let idCR = "";
	idCR = params.id;	

	let cr = [];
	let attendees = [];
	let cr_extractive_raw = "";
	let cr_abstractive_raw = "";
	let cr_extractive_edited = "";
	let cr_abstractive_edited = "";
	let cr_last_update_extractive = "";
	let cr_last_update_abstractive = "";

	async function load(){
		console.log("Load");
		const res = await fetch(`http://localhost:8080/api/summary/${idCR}`);
		cr = await res.json();
		tick();
		attendees = cr.attendees;
		cr_last_update_extractive = cr.summary.extractive.lastUpdate;
		cr_last_update_abstractive = cr.summary.abstractive.lastUpdate;
		cr_extractive_raw = cr.summary.extractive.raw;
		cr_abstractive_raw = cr.summary.abstractive.raw;
		console.log("Edited ? " + cr.summary.extractive.edited);
		if (typeof cr.summary.extractive.edited != "undefined") {
			cr_extractive_edited = cr.summary.extractive.html;
		}
		else{
			cr_extractive_edited = ""
		}
		if (typeof cr.summary.abstractive.edited != "undefined") {
			cr_abstractive_edited = cr.summary.abstractive.html;
		}
			else{
			cr_abstractive_edited = ""
		}
		$crJSON = cr;
	}

	function resetHandler(event){
		console.log("Handler");
		load().then("Resetted")
	}

	onMount(async () => {load()});

	function generatePDF_extractif() {
		var pdf = new jsPDF("l", "mm", [297, 290]);

		var title = cr.title;
		var generator = cr.generatorName;
		var date = cr.date;
		var team = cr.projectGroup;
		var attendees = cr.attendees;
		var odj = cr.meetingProgram;

		var summary_ext = cr.summary.extractive.raw;
		if (typeof cr.summary.extractive.edited != "undefined") {
			summary_ext = cr.summary.extractive.edited;
		}

		pdf.addImage(imgInnov, "PNG", 120, 5, 60, 40);

		pdf.setTextColor(236, 119, 30);
		pdf.setFontSize(28);
		pdf.text(15, 60, title);

		pdf.addImage(imgGenerator, "PNG", 240, 53, 10, 10);

		pdf.setFontSize(18);
		pdf.text(255, 60, generator);

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(1.5);
		pdf.line(15, 67, 280, 67);

		pdf.addImage(imgTeam, "PNG", 15, 80, 18, 18);
		pdf.addImage(imgCalendar, "PNG", 110, 80, 20, 20);
		pdf.addImage(imgAttendee, "PNG", 215, 80, 20, 20);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(20);
		pdf.text(40, 100, team);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(20);
		pdf.text(135, 100, date);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(18);
		pdf.text(242, 85, attendees);

		pdf.addImage(imgODJ, "PNG", 15, 115, 15, 15);

		pdf.setFontSize(20);
		pdf.text(40, 125, "ORDRE DU JOUR");

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(0.5);
		pdf.line(15, 132, 280, 132);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(14);
		pdf.text(15, 145, odj);

		pdf.addImage(imgCR, "PNG", 17, 160, 15, 15);

		pdf.setFontSize(20);
		pdf.text(40, 170, "COMPTE RENDU DE REUNION");

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(0.5);
		pdf.line(15, 177, 280, 177);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(11);
		pdf.text(15, 190, summary_ext, {
			maxWidth: 264,
			align: "justify",
		});

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(1);
		pdf.line(15, 250, 280, 250);

		pdf.addImage(imgAubay, "PNG", 146, 260, 20, 20);

		pdf.setTextColor(236, 119, 30);
		pdf.setFontSize(10);
		pdf.text(136, 287, "Document classifié C1");

		pdf.save(title + "_extractif.pdf");
	}

	function generatePDF_abstractif() {
		var pdf = new jsPDF("l", "mm", [297, 290]);

		var title = cr.title;
		var generator = cr.generatorName;
		var date = cr.date;
		var team = cr.projectGroup;
		var attendees = cr.attendees;
		var odj = cr.meetingProgram;

		var summary_abs = cr.summary.abstractive.raw;
		if (typeof cr.summary.abstractive.edited != "undefined") {
			summary_abs = cr.summary.abstractive.edited;
		}

		pdf.addImage(imgInnov, "PNG", 120, 5, 60, 40);

		pdf.setTextColor(236, 119, 30);
		pdf.setFontSize(28);
		pdf.text(15, 60, title);

		pdf.addImage(imgGenerator, "PNG", 240, 53, 10, 10);

		pdf.setFontSize(18);
		pdf.text(255, 60, generator);

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(1.5);
		pdf.line(15, 67, 280, 67);

		pdf.addImage(imgTeam, "PNG", 15, 80, 18, 18);
		pdf.addImage(imgCalendar, "PNG", 110, 80, 20, 20);
		pdf.addImage(imgAttendee, "PNG", 215, 80, 20, 20);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(20);
		pdf.text(40, 100, team);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(20);
		pdf.text(135, 100, date);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(18);
		pdf.text(242, 85, attendees);

		pdf.addImage(imgODJ, "PNG", 15, 115, 15, 15);

		pdf.setFontSize(20);
		pdf.text(40, 125, "ORDRE DU JOUR");

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(0.5);
		pdf.line(15, 132, 280, 132);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(14);
		pdf.text(15, 145, odj);

		pdf.addImage(imgCR, "PNG", 17, 160, 15, 15);

		pdf.setFontSize(20);
		pdf.text(40, 170, "COMPTE RENDU DE REUNION");

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(0.5);
		pdf.line(15, 177, 280, 177);

		pdf.setTextColor(0, 0, 0);
		pdf.setFontSize(11);
		pdf.text(15, 190, summary_abs, {
			maxWidth: 264,
			align: "justify",
		});

		pdf.setDrawColor(207, 206, 206);
		pdf.setLineWidth(1);
		pdf.line(15, 250, 280, 250);

		pdf.addImage(imgAubay, "PNG", 146, 260, 20, 20);

		pdf.setTextColor(236, 119, 30);
		pdf.setFontSize(10);
		pdf.text(140, 287, "Document classifié C1");

		pdf.save(title + "_abstractif.pdf");
	}

	// Img base 64

	var imgInnov = new Image();
	imgInnov.src = "img/innov.png";

	var imgAubay = new Image();
	imgAubay.src = "img/aubay.png";

	var imgTeam = new Image();
	imgTeam.src = "img/team.png";

	var imgAttendee = new Image();
	imgAttendee.src = "img/attendee.png";

	var imgCalendar = new Image();
	imgCalendar.src = "img/calendar.png";

	var imgGenerator = new Image();
	imgGenerator.src = "img/generator.png";

	var imgCR = new Image();
	imgCR.src = "img/cr.png";

	var imgODJ = new Image();
	imgODJ.src = "img/odj.png";
</script>

<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
	<symbol id="check-circle-fill" fill="currentColor" viewBox="0 0 16 16">
		<path
			d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
		/>
	</symbol>
</svg>
<Notification />
<!--Breadcrump navigation-->
<nav aria-label="breadcrumb">
	<ol class="breadcrumb">
		<li class="breadcrumb-item">
			<a href="#"><i class="bi bi-house-door-fill" /> Accueil</a>
		</li>
		<li class="breadcrumb-item active" aria-current="page">{cr.title}</li>
	</ol>
</nav>

{#if params.isCreated && params.isCreated == "isCreated"}
	<div class="alert alert-success alert-dismissible fade show" role="alert">
		<svg
			class="bi flex-shrink-0 me-2"
			width="24"
			height="24"
			role="img"
			aria-label="Success:"><use xlink:href="#check-circle-fill" /></svg
		>
		{cr.title} crée avec succès
		<button
			type="button"
			class="btn-close"
			data-bs-dismiss="alert"
			aria-label="Close"
			style="align-items: right !important;"
		/>
	</div>
{/if}
{#if params.isCreated && params.isCreated == "isEdited"}
	<div class="alert alert-success alert-dismissible fade show" role="alert">
		<svg
			class="bi flex-shrink-0 me-2"
			width="24"
			height="24"
			role="img"
			aria-label="Success:"><use xlink:href="#check-circle-fill" /></svg
		>
		{cr.title} a été modifié avec succès
		<button
			type="button"
			class="btn-close"
			data-bs-dismiss="alert"
			aria-label="Close"
			style="align-items: right !important;"
		/>
	</div>
{/if}

<div class="indent">
	<p class="display-4" style="font-size:5vw !important;">{cr.title}</p>
	<hr class="line"/> 
</div>

<div class="generatebody">
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-8 mt-5 mb-5">
				<h5>Groupe projet</h5>
				<h6>{cr.projectGroup}</h6>
			</div>
			<div class="col-md-4 mt-5 mb-5">
				<h5>Date</h5>
				<h6>{cr.date}</h6>
			</div>
		</div>

		<div class="row">
			<div class="col-md-8 mb-5">
				<h5>Nom des participants</h5>
				<ul>
					{#each attendees as attendee}
						<li>{attendee}</li>
					{/each}
				</ul>
			</div>
			<div class="col-md-4 mb-5">
				<h5>Nom du générateur</h5>
				<h6>{cr.generatorName}</h6>
			</div>
		</div>

		<div class="row">
			<div class="col-md-8 mb-5">
				<h5>Ordre du jour</h5>
				<h6>{cr.meetingProgram}</h6>
			</div>
			<div class="col-md-4 mb-5">
				<h5>Note</h5>
				<h6 style="color: green">
					<i class="bi bi-hand-thumbs-up" /> +12
					<h6>
						<br />
						<h6 style="color: red">
							<i class="bi bi-hand-thumbs-down" /> -5
							<h6 />
						</h6>
					</h6>
				</h6>
			</div>
		</div>

		<h4 style="color: #ec771e;">
			Texte généré par la solution Speech To Text (Rev.ai)
		</h4>
		<br />
		<div class="row orange">
			<div class="col m-3">
				<div class="row">
					{cr.transcript}
				</div>
			</div>
		</div>

		<div class="row">
			<div class="col m-3 ">
				<div class="wrap">
					<img
						src="http://image.flaticon.com/icons/svg/3/3907.svg"
						id="arrow"
						class="animated bounce"
					/>
				</div>
			</div>
		</div>

		<div class="row">
			<div class="col-md-6 p-5">
				<h5
					style="color: #ec771e !important; margin-bottom: 20px !important;"
				>
					Résumé généré par CamemBERT (Extractif)
				</h5>
				<div class="row orange">
					<div class="col m-4">
						<div class="row">
							{#if cr_extractive_edited != ""}
								{@html cr_extractive_edited}
							{:else}
								{cr_extractive_raw}
							{/if}
						</div>
					</div>
					<div class="row">
						<div class="col-md-7 ml-4 mb-4 text-left">
							{#if cr_last_update_extractive != "" && cr_last_update_extractive != undefined}
								<p style="color: #A4ADB3 !important; font-size: 14px;">Dernière modification le : <strong>{cr_last_update_extractive}</strong></p>
							{/if}
						</div>
						<div class="col-3 col-md-4 ml-4 mb-4 text-right">
							{#if cr_extractive_edited != ""}
								<ResetButton idCR={idCR} crType="ext" on:reset_cr={resetHandler}/>
							{/if}
						</div>
					</div>
				</div>
			</div>
			<div class="col-md-6 p-5">
				<h5
					style="color: #ec771e !important; margin-bottom: 20px !important;"
				>
					Résumé généré par mBART'hez (Abstractif)
				</h5>
				<div class="row orange">
					<div class="col m-4">
						<div class="row">
							{#if cr_abstractive_edited != ""}
								{@html cr_abstractive_edited}
							{:else}
								{cr_abstractive_raw}
							{/if}
						</div>
					</div>
					<div class="row">
						<div class="col-md-7 ml-4 mb-4 text-left">
							{#if cr_last_update_abstractive != "" && cr_last_update_abstractive != undefined}
								<p style="color: #A4ADB3 !important; font-size: 14px;">Dernière modification le : <strong>{cr_last_update_abstractive}</strong></p>
							{/if}
						</div>
						<div class="col-3 col-md-4 ml-4 mb-4 text-right">
							{#if cr_abstractive_edited != ""}
								<ResetButton idCR={idCR} crType="abs" on:reset_cr={resetHandler}/>
							{/if}
						</div>
					</div>
				</div>
			</div>
		</div>

		<div style="margin-top: -100px;">
			<div class="row pr-3 pl-3">
				<div class="col-md-6 p-5 replacementExt">				
					<div class="row">
						<div class="col-md-8">
							<div class="row">
								<div class="col-12 mb-2">
									<a
										class="btn btn-primary"
										href="#/EditCR/ext/{idCR}"
										>Editer le CR <i
											class="bi bi-pencil-square"
										/></a
									>
								</div>
								<div class="col-12  ">
									<button
										class="btn btn-outline-secondary"
										on:click={generatePDF_extractif}
										>Exporter le CR <i
											class="bi bi-file-earmark-pdf"
										/></button
									>
								</div>
							</div>
						</div>
						
						<div class="col-md-4 text-right replacementExtThumbs">				
							<div class="row">
								<div class="col-md-6">
									<div class="row">
										<div class="col-12">
											<h6 style="color: green">
												<i
													class="bi bi-hand-thumbs-up"
												/>
												<h6 />
											</h6>
										</div>
										<div class="col-12">
											<p style="color: green;">+5</p>
										</div>
									</div>
								</div>
								<div class="col-md-6">
									<div class="row">
										<div class="col-12">
											<h6 style="color: red">
												<i
													class="bi bi-hand-thumbs-down"
												/>
												<h6 />
											</h6>
										</div>
										<div class="col-12">
											<p style="color: red;">+5</p>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="col-md-6 p-5 replacementAbs">				
					<div class="row">
						<div class="col-md-8">
							<div class="row">
								<div class="col-12 mb-2">
									<a
										class="btn btn-primary"
										href="#/EditCR/abs/{idCR}"
										>Editer le CR <i
											class="bi bi-pencil-square"
										/></a
									>
								</div>
								<div class="col-12">
									<button
										class="btn btn-outline-secondary"
										on:click={generatePDF_abstractif}
										>Exporter le CR <i
											class="bi bi-file-earmark-pdf"
										/></button
									>
								</div>
							</div>
						</div>
						<div class="col-md-4 text-right replacementAbsThumbs">				
							<div class="row">
								<div class="col-md-6">
									<div class="row">
										<div class="col-12">
											<h6 style="color: green">
												<i
													class="bi bi-hand-thumbs-up"
												/>
												<h6 />
											</h6>
										</div>
										<div class="col-12">
											<p style="color: green;">+5</p>
										</div>
									</div>
								</div>
								<div class="col-md-6">
									<div class="row">
										<div class="col-12">
											<h6 style="color: red">
												<i
													class="bi bi-hand-thumbs-down"
												/>
												<h6 />
											</h6>
										</div>
										<div class="col-12">
											<p style="color: red;">+5</p>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
<style>
	.orange {
		border-radius: 10px !important;
		border-color: #ec771e !important;
		border-width: 0.5px;
		border: solid;
		text-align: justify !important;
		margin-bottom: 100px;
		overflow-wrap: break-word !important;
		word-wrap: break-word !important;
	}
</style>
