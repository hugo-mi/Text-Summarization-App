<script>
    import InputFileArea from "../components/inputFileArea.svelte";
    import { element } from "svelte/internal";
    import { cr } from "../components/store.js";
    import InputFileText from '../components/inputFileText.svelte'
    import { pendingRecords } from "../components/store.js";
    import {afterUpdate } from 'svelte';

    //import
    import { Form, FormGroup, Input, Label, Button, Icon, InputGroup, InputGroupText, Col, Row, Alert, Modal, ModalBody, ModalFooter, ModalHeader  } from 'sveltestrap';
 
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
    
    let audioYNRadio = "0";   
    let members = [
		{ number: 1 , name: '' }
		
	];

    let verificationBoolean = false
    let verificationAlert = false
    let dateIsTodayOrBefore = false
    let audioIsPresent = false
    let allIsGreen = false
    let backIssue = false
    const toggle = () => (backIssue = !backIssue);
    let backIssueMessage = ''
    let clickOnButton = 0;
    //Clear la variable $cr avant utilisation
    $cr = {
        fileInput :"",
        transcript: "",
        title: "",
        projectGroup: "",
        date: "",
        generatorName: "",
        meetingProgram: "",
        attendees: []
    }

    //Function

    /**
     * Ajoute un membre 
    */
    function add() {
        members = members.concat({ number: members.length + 1, name: "" });
        members.forEach(assignNumber);
    }

    /**
     * Assigne un numéro(index) au participant(element)
     * 
     * @param element element(participant) dans la liste members
     * @param index index dans la liste members
     */
    function assignNumber(element,index)
    {
        element.number = index+1;
    }

    /**
     *  Retire un membre(element) dans la liste des particpants(members)
     * 
     * @param element element(participant) a retirer dans la liste members
     */
    function remove(element) {
        members = members.filter(function (item) {
            return item !== element;
        });
        members.forEach(assignNumber);
	}

    /**
     * Convertit une date us--> fr ou fr-->us
     * 
     * @param dateString date a convertir
     */
    function convertDate(dateString){
        var p = dateString.split(/\D/g)
        return [p[2],p[1],p[0] ].join("-")
    }

    /**
     * Verifie que tout les inputs sont vert(valid) et qu'il y a un fichier audio si l'audio est sélectionné
    */
    function verificationInput(){

        audioIsPresent = $cr.fileInput !== "";
        ////
        var today = new Date();
        var dateEnter = new Date($cr.date)

        dateIsTodayOrBefore = today >= dateEnter;
        ////
        
        var listInput= [...document.getElementsByClassName("inputVerification")].map(
                input => {return input.className}
            );
        
        
        allIsGreen = !listInput.some(
                        element => 
                             element.includes("is-invalid")
                    )
                    
        console.log(listInput)
        console.log(allIsGreen)
        console.log(dateIsTodayOrBefore)
        
        
        if(audioYNRadio === "1")
            return  audioIsPresent &&
                    dateIsTodayOrBefore &&
                    allIsGreen
        else 
            return  dateIsTodayOrBefore &&
                    allIsGreen             
        
        
    }

    /**
     * Envoie les donnée du formulaire au back-end
     * 
     */
    async function submitFormulaire(){

        
        verificationAlert = !verificationInput()

        console.log(verificationAlert)
        if((!verificationAlert) && clickOnButton)
        {
            $cr.date = convertDate($cr.date)
            $cr.attendees = members.map(
                member => {return member.name}
            )
            console.log(3)

            console.log(JSON.stringify($cr, 0, 2))

            if (audioYNRadio == "0"){
                fetch(
                    "http://localhost:8080/api/createCR/text",
                    {
                        method : 'post',
                        headers: { "Content-Type": "application/json" },
                        body : JSON.stringify($cr, 0, 2)
                    }
                )
                .then(async resp => {
                    console.log(resp);
                    if(resp.status !== 200)
                    {
                        backIssueMessage = "Error "+ resp.status +" : "+resp.statusText
                        backIssue=true
                    }else{
                        let id = await resp.json();
                        $pendingRecords.set(Object.values(id), "in_progress");
                        console.log("Nouveau CR en attente de génératio, id :", id);
                        window.location.href = "#/HistoriqueCR/"
                    }
                        
                })
                .catch(function(error) {
                    console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
                    console.log(error)
                    backIssueMessage = error.message
                    backIssue=true
                });
                
            }
            else {
                var formData = new FormData();
                formData.append('data',  JSON.stringify($cr, 0, 2));
                formData.append("file", $cr.fileInput.file , $cr.fileInput.name);
                fetch(
                    "/api/createCR/audio",
                    {
                        method : "post",
                        body : formData,
                    }
                )
                .then(async resp => {
                    console.log(resp);
                    if(resp.status !== 200)
                    {
                        backIssueMessage = "Error "+ resp.status +" : "+resp.statusText
                        backIssue=true
                    }else{
                        let id = await resp.json();
                        $pendingRecords.set(Object.values(id), "in_progress");
                        console.log("Nouveau CR en attente de génératio, id :", id);
                        window.location.href = "#/HistoriqueCR/"
                    }
                })
                .catch(function(error) {
                    console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
                    console.log(error)
                    backIssueMessage = error.message
                    backIssue=true
                });
                
            } 
        }
        verificationBoolean
        clickOnButton=false
    }

    afterUpdate(() => {
	if (verificationBoolean === true)
    {
        submitFormulaire();
    } 
});
</script>


<style>
  
  .generatebody{
    color : #5D5D5D ;
    margin: 5em;
  }
  .form-check{
    display:block;
    min-height:1.5rem;
    padding-left:1.5em;
    margin-bottom:.125rem}


.form-check-input:focus{
	border-color:#ec771e;
	outline:0;
	box-shadow:0 0 0 .25rem #ec771e;
}

.form-check-input:checked
{
    background-color:#ec771e;
    border-color:#ec771e
}


.selectProjet:focus {
    border-color: #ec771e !important;
    box-shadow: 0 0 0 .25rem #ec771e !important;
}


  
</style>

<!-- HTML -->
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item">
            <a href="/#"><i class="bi bi-house-door-fill" /> Accueil</a>
        </li>
        <li class="breadcrumb-item active" aria-current="page">
            Génération CR
        </li>
    </ol>
</nav>

<div class="indent">
    <p class="display-4">Générer votre CR en quelques clics</p>
    <hr class="line" />
</div>

<div class="generatebody">
    <Form>
        <Row>
            <Col>
                <Label class="form-label" for="audioYN">Souhaitez-vous téléverser l'audio de réunion? </Label>
                <div class="row row-cols-lg-auto g-3 align-items-center">
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" bind:group={audioYNRadio} value="1" label="Oui">
                        <label class="form-check-label" for="audioY" >Oui</label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" bind:group={audioYNRadio} value="0" label="Non" checked>
                        <label class="form-check-label" for="audioN" >Non</label>
                    </div>
                </div>
            </Col>
        </Row>

        <br/>

        <Row>
            <Col>
                {#if audioYNRadio === "0"}  
                    <FormGroup>
                        <Label for="textCR">Texte du Compte Rendu</Label>
                        <InputFileText bind:transcript={$cr.transcript}/>
                        <hr class="line"/>
                        <Input type="textarea" name="text" id="textCR" class="inputVerification" bind:value={$cr.transcript} valid={$cr.transcript !== "" && verificationBoolean ? true : undefined} invalid={$cr.transcript === "" && verificationBoolean ? true : undefined} />                
                    </FormGroup>
                {:else}                
                    <InputFileArea bind:fileInput={$cr.fileInput}/>
                {/if}
            </Col>
                
        </Row>

        <br/>

        <Row>
            <Col sm="4">
                <FormGroup>
                    <Label for="title">Titre du Compte Rendu</Label>
                    <Input type="text" name="text" id="title" class="inputVerification" bind:value={$cr.title} valid={$cr.title !== "" && verificationBoolean ? true : undefined} invalid={$cr.title === "" && verificationBoolean ? true : undefined}/> 
                </FormGroup>
            </Col>
        </Row>

        <Row>
            <Col sm="4">
                <FormGroup>
                    <Label for="projectCR">Groupe Projet</Label>
                    <Input class="selectProjet inputVerification" type="select" name="select" id="projectCR"  bind:value={$cr.projectGroup} valid={$cr.projectGroup !== "" && verificationBoolean ? true : undefined} invalid={$cr.projectGroup === "" && verificationBoolean ? true : undefined}  >
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
                        class="inputVerification"
                        placeholder="date placeholder" 
                        bind:value={$cr.date}
                        valid={$cr.date !== "" && verificationBoolean && dateIsTodayOrBefore ? true : undefined} invalid={$cr.date === "" && verificationBoolean && !dateIsTodayOrBefore ? true : undefined} 
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
                        <Input type="text" name="text" id="nameGenerator" class="inputVerification" bind:value={$cr.generatorName} valid={$cr.generatorName !== "" && verificationBoolean ? true : undefined} invalid={$cr.generatorName === "" && verificationBoolean ? true : undefined} />
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
                <Label for="participant">Participant {member.number} </Label>
                <div class="input-group mb-3">
                    <Input type="text" class="inputVerification" bind:value={member.name} valid={member.name !== "" && verificationBoolean ? true : undefined} invalid={member.name === "" && verificationBoolean ? true : undefined} />
                    <button class="btn btn-outline-danger" type="button" on:click={remove(member)}><Icon name="dash-square" /></button>
                </div>
            {/each}
        </Col>
    </Row>
    <Button  class="btn-primary" on:click={add} >Ajout d'un Participant <Icon name="person-plus" /></Button>
    <br/>
    <br/>

    <Form>        
        <Row>
            <Col>
                <FormGroup> 
                    <Label for="meetingProgram">Ordre du jour</Label>
                    <Input type="textarea" name="text" id="meetingProgram" class="inputVerification" size="sm" bind:value={$cr.meetingProgram}  valid={$cr.meetingProgram !== "" && verificationBoolean ? true : undefined} invalid={$cr.meetingProgram === "" && verificationBoolean ? true : undefined}/>
                </FormGroup>
            </Col>      
        </Row>

        <Row>
            <Col>
                <Button type="button" class="btn btn-primary" on:click={() => {verificationBoolean = true; clickOnButton=true}} block>Générer CR <Icon name="gear" /></Button>
            </Col>      
        </Row>        
    </Form>
    <br>
    <Alert
        color="danger"
        isOpen={verificationAlert}
        toggle={() => (verificationAlert = false)}>
        {#if !audioIsPresent && audioYNRadio === "1"} <!-- Si l'option audio est sélection  et qu'il n'y a pas de fichier audio-->
        Veuillez sélectionner un fichier audio.
        <br>
        {/if}
        {#if !dateIsTodayOrBefore}
        Veuillez entrer une date antérieure ou égale à celle d'aujourd'hui
        <br>        
        {/if}
        {#if !allIsGreen}
        Veuillez completer tous les champs en rouge.
        {/if}
    </Alert>
    <Modal isOpen={backIssue} {toggle} color="danger">
        <ModalHeader {toggle}><h5 style="color:red !important;">Erreur</h5></ModalHeader>
        <ModalBody>
            Il y a eu un problème avec l'opération fetch:
            <br>
            {backIssueMessage}
            <br>
            Veuillez rééssayer plus tard.
        </ModalBody>
        <ModalFooter>
          <Button color="secondary" on:click={toggle}>Cancel</Button>
        </ModalFooter>
    </Modal>

</div>
