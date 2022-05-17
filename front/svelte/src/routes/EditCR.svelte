<script>
    import { onMount } from "svelte";
    import { bind, element } from "svelte/internal";
    import { cr } from "../components/store.js";
    import Quill from "quill";
    import { crJSON } from '../components/store.js';
    //import
    import {
        Form,
        FormGroup,
        Input,
        Label,
        Button,
        Icon,
        InputGroup,
        InputGroupText,
        Col,
        Row,
    } from "sveltestrap";

    export let params = {};
    console.log(params);
    let idCR = "";
    let typeCR = "";
    idCR = params.id;
    typeCR = params.type;

    let cr_json = [];
    let attendees = [];
    let cr_extractive_raw = "";
    let cr_abstractive_raw = "";
    let cr_extractive_edited = "";
    let cr_abstractive_edited = "";
    $crJSON.date = convertDate($crJSON.date);

    onMount(async () => {
        const res = await fetch(`http://localhost:8080/api/summary/${idCR}`);
        cr_json = await res.json();
        attendees = cr_json.attendees;
        cr_extractive_raw = cr_json.summary.extractive.raw;
        cr_abstractive_raw = cr_json.summary.abstractive.raw;
        if (typeof cr_json.summary.extractive.edited != "undefined") {
            cr_extractive_edited = cr_json.summary.extractive.edited;
        }
        if (typeof cr_json.summary.abstractive.edited != "undefined") {
            cr_abstractive_edited = cr_json.summary.abstractive.edited;
        }
    });

    console.log($crJSON);

    function chooseSummary() {
        if (typeCR == "ext" && $crJSON.summary.extractive.edited != undefined) {
            cr_extractive_edited = $crJSON.summary.extractive.html;
            content.text = cr_extractive_edited;
            return cr_extractive_edited;
        } else if (
            typeCR == "ext" &&
            $crJSON.summary.extractive.edited == undefined
        ) {
            cr_extractive_raw = $crJSON.summary.extractive.raw;
            content.text = cr_extractive_raw;
            return cr_extractive_raw;
        } else if (
            typeCR == "abs" &&
            $crJSON.summary.abstractive.edited != undefined
        ) {
            cr_abstractive_edited = $crJSON.summary.abstractive.html;
            content.text = cr_abstractive_edited;
            return cr_abstractive_edited;
        } else {
            cr_abstractive_raw = $crJSON.summary.abstractive.raw;
            content.text = cr_abstractive_raw;
            return cr_abstractive_raw;
        }
    }

    //variable
    let groupeProjetDB = [//Liste des Projets
        "AMC",
        "AMP",
        "DEP",
        "DWYH",
        "EBOUARD",
        "EPCL",
        "GAO",
        "GOCHAIN",
        "HOLOVIEW",
        "ISCAN",
        "KSKILL",
        "KYP",
        "LCDP",
        "NLP",
        "ODR",
        "SERIOUS",
        "SERVERLESS",
        "UI",
        "VRCLOUD",
        "WMF"
    ]


    //variable formulaire
    let members = [];
    members = $crJSON.attendees.map((obj) => {
        var memberTemp = { number: 0, name: "" };
        memberTemp.number = $crJSON.attendees.indexOf(obj) + 1;
        memberTemp.name = obj;
        console.log(attendees.indexOf(obj));
        console.log(memberTemp.name);
        return memberTemp;
    });

    var today = new Date();
    var date = today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var dateTime = date+' à '+time;  

    // Text Editor

    let content = { html: "", text: "" };
    let quill = null;

    onMount(() => {
        let container = document.getElementById("editor");
        quill = new Quill(container, {
            modules: {
                toolbar: [
                    [
                        { font: [] },
                        { size: ["small", false, "large", "huge"] }, // custom dropdown
                        { header: 1 },
                        { header: 2 },
                        "",
                    ], // custom button values

                    ["bold", "italic", "underline", "strike", ""], // toggled buttons

                    [{ list: "ordered" }, { list: "bullet" }],
                    [{ indent: "-1" }, { indent: "+1" }], // outdent/indent

                    [{ color: [] }, { background: [] }], // dropdown with defaults from theme

                    ["clean"], // remove formatting button
                ],
            },
            placeholder: "Type something...",
            theme: "snow", // or 'bubble'
        });
        var delta = quill.clipboard.convert(chooseSummary());
        quill.setContents(delta, "silent");
    });

    //Function
    function add() {
        members = members.concat({ number: members.length + 1, name: "" });
        members.forEach(assignNumber);
    }

    function assignNumber(element, index, array) {
        element.number = index + 1;
    }

    function remove(element) {
        members = members.filter(function (item) {
            return item !== element;
        });
        members.forEach(assignNumber);
    }

    function getAllValue() {
        var editor_content = quill.container.firstChild.innerHTML;
        console.log(editor_content);

        if (typeCR == "ext") {
            $crJSON.summary.extractive.html = editor_content;
            $crJSON.summary.extractive.edited = quill.getText();
            $crJSON.summary.extractive.lastUpdate = dateTime;
        } else {
            $crJSON.summary.abstractive.html = editor_content;
            $crJSON.summary.abstractive.edited = quill.getText();
            $crJSON.summary.abstractive.lastUpdate = dateTime;
        }
        $crJSON.date = convertDate($crJSON.date); //remise en fr
        $crJSON.attendees = members.map((member) => {
            return member.name;
        });
        console.log($crJSON);

        fetch("http://localhost:8080/api/summary/" + $crJSON.id + "/update", {
            method: "post",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify($crJSON, 0, 2),
            redirect: "follow",
        }).then((response) => {
            console.log("CR updated");
            window.location.href = "#/VoirCR/" + $crJSON.id + "/isEdited";
        });
    }

    function convertDate(dateString) {
        var p = dateString.split(/\D/g);
        return [p[2], p[1], p[0]].join("-");
    }
</script>

<svelte:head>
    <link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet" />
</svelte:head>

<!-- HTML -->
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item">
            <a href="#"><i class="bi bi-house-door-fill" /> Accueil</a>
        </li>
        <li class="breadcrumb-item active" aria-current="page">Editer le CR</li>
    </ol>
</nav>

<div class="indent">
    <p class="display-4">Editer le CR</p>
    <hr class="line" />
</div>

<div class="generatebody">
    <Form>
        <Row>
            <Col>
                <FormGroup>
                    <Label for="textCR">Texte du Compte Rendu</Label>
                    <div id="editor" class="editor" />
                    <br />
                </FormGroup>
            </Col>
        </Row>

        <Row>
            <Col sm="4">
                <FormGroup>
                    <Label for="title">Titre du Compte Rendu</Label>
                    <Input
                        type="text"
                        name="text"
                        id="title"
                        bind:value={$crJSON.title}
                    />
                </FormGroup>
            </Col>
        </Row>

        <Row>
            <Col sm="4">
                <FormGroup>
                    <Label for="projectCR">Groupe Projet</Label>
                    <Input
                        class="selectProjet"
                        type="select"
                        name="select"
                        id="projectCR"
                        bind:value={$crJSON.projectGroup}
                    >
                        <option selected>Groupe</option>
                        {#each groupeProjetDB as groupe}
                            <option value={groupe}>
                                {groupe}
                            </option>
                        {/each}
                    </Input>
                </FormGroup>
            </Col>
        </Row>

        <Row>
            <Col sm="3">
                <FormGroup class="sm">
                    <Label for="exampleDate">Date</Label>
                    <InputGroup>
                        <Input
                            type="date"
                            name="date"
                            id="exampleDate"
                            placeholder="date placeholder"
                            format="dd-mm-yyyy"
                            bind:value={$crJSON.date}
                        />
                        <InputGroupText>
                            <Icon name="calendar3" />
                        </InputGroupText>
                    </InputGroup>
                </FormGroup>
            </Col>
        </Row>

        <Row>
            <Col sm="4">
                <FormGroup>
                    <Label for="nameGenerator">Nom du rédacteur</Label>
                    <InputGroup>
                        <Input
                            type="text"
                            name="text"
                            id="nameGenerator"
                            bind:value={$crJSON.generatorName}
                        />
                        <InputGroupText>
                            <Icon name="pen" />
                        </InputGroupText>
                    </InputGroup>
                </FormGroup>
            </Col>
        </Row>
    </Form>

    <h5 for="members">Nom des Participants</h5>
    <Row>
        <Col sm="4">
            {#each members as member}
                <Label for="participant">Participant {member.number}</Label>
                <div class="input-group mb-3">
                    <input
                        type="text"
                        class="form-control"
                        bind:value={member.name}
                    />
                    <button
                        class="btn btn-outline-danger"
                        on:click={remove(member)}
                        ><Icon name="dash-square" /></button
                    >
                </div>
            {/each}
        </Col>
    </Row>

    <Button class="btn-primary" on:click={add}
        >Ajout d'un Participant <Icon name="person-plus" /></Button
    >
    <br />
    <br />

    <Form>
        <Row>
            <Col>
                <FormGroup>
                    <Label for="meetingProgram">Ordre du jour</Label>
                    <Input
                        type="textarea"
                        name="text"
                        id="meetingProgram"
                        size="sm"
                        bind:value={$crJSON.meetingProgram}
                    />
                </FormGroup>
            </Col>
        </Row>

        <Row>
            <Col>
                <Button
                    type="button"
                    class="btn btn-primary"
                    on:click={getAllValue}
                    block>Modifier le CR <Icon name="pencil-square" /></Button
                >
            </Col>
        </Row>
    </Form>
</div>

<style>
    .generatebody {
        color: #5d5d5d !important;
        margin: 5em;
    }

    .form-check {
        display: block;
        min-height: 1.5rem;
        padding-left: 1.5em;
        margin-bottom: 0.125rem;
    }

    .form-check-input:focus {
        border-color: #ec771e;
        outline: 0;
        box-shadow: 0 0 0 0.25rem #ec771e;
    }

    .form-check-input:checked {
        background-color: #ec771e;
        border-color: #ec771e;
    }

    .selectProjet:focus {
        border-color: #ec771e !important;
        box-shadow: 0 0 0 0.25rem #ec771e !important;
    }

    .orange {
        border-radius: 10px !important;
        border-color: #ec771e !important;
        border-width: 0.5px;
        border: solid;
        text-align: justify !important;
        margin-bottom: 100px;
    }
</style>
