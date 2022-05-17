<!-- 
    Le fichier texte .txt sera récupéré
Si l'utilisateur tente de rentrer un fichier qui n'est pas de type "text/plain" 
ou tente d'envoyer plusieurs fihcier alors la zone de du fichier deviendra rouge 
et indiquera l'erreur
Sinon le texte original sera affiché en dessous et l'uilisateur pourra modifier, 
s'il le désire, son contenu dans la zone input juste en dessous      
-->

<script>
    //Import
    import { Icon, Button, Label, Spinner, Card, CardBody, CardText,Collapse} from 'sveltestrap';

    //Variable
    export let transcript;//Variable contenant le texte
    let fileInput ='';//Variable contenant les informations relatif au fichier    
	let fileIDK;
    let isOpen = false;
    /*
    error = 0 ==> pas d'erreur
    error = 1 ==> il y a plus d'un fichier
    error = 2 ==> c'est pas un type "text/plain"
    */
    let error = 0;    

 	const onFileSelected =(e)=>{
        // reintialisation des variables
        fileInput='';
        error = 0;
        transcript = ""

        //verification qu'on rentre bien un seul fichier
        if (e.target.files.length > 1)
            error = 1
        //verification que c'est bien un type "text/plain"    
        else if(e.target.files[0].type !== "text/plain" )
            error = 2    
        else {
            var path = e.target.value
            var startIndex = (path.indexOf('\\') >= 0 ? path.lastIndexOf('\\') : path.lastIndexOf('/'));
            var filename = path.substring(startIndex);
            if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
                filename = filename.substring(1);
            }
            fileInput = {
                "file" : e.target.files[0],
                'name' : filename
            }
        }
    }
    
    //Fonction
    /**
     * Fonction permettant la lecture d'un fichier entré dans la variable fileInput.file
     * 
     * parametre : rien
     * 
     * returns: le texte d'une fichier .txt
     */
    async function readText() {
        fileInput.file.text()
        .then(
            (text) => transcript = text
        )
        
        return fileInput.file.text();
    }
	
</script>

<style>

    .upFile{
        background-color: #e3e3e3 !important;
        border: solid  #ec771e !important;
        color: #ec771e !important;
        padding: 1em;
        align-items: stretch;
        align-content: center;
        text-align: center;
        border-radius: 3px;
        
    }
    .upFile:hover{
        background-color: #ec771e !important;
        border: solid  #ec771e !important;
        color: #e3e3e3 !important;
        padding: 1em;
        align-items: stretch;
        align-content: center;
        text-align: center;
        
    }

    .upFile:focus{
	    border-color:#ec771e !important;
	    outline:0 !important;
	    box-shadow:0 0 0 .25rem #ec771e !important;
    }

    .upFile:hover{
	    border-color:#ec771e !important;
	    outline:0 !important;
	    box-shadow:0 0 0 .25rem #ec771e !important;
    }
    .deletebtn{
        margin-bottom: 0.5%;
        margin-right: 0;
    }

    .upFileError{
        background-color: #e3e3e3 !important;
        border: solid  #eb2823 !important;
        color: #eb2823 !important;
        padding: 1em;
        align-items: stretch;
        align-content: center;
        text-align: center;
        border-radius: 3px;
        
    }
    .upFileError:hover{
        background-color: #eb2823 !important;
        border: solid  #eb2823 !important;
        color: #e3e3e3 !important;
        padding: 1em;
        align-items: stretch;
        align-content: center;
        text-align: center;
        
    }

    .upFileError:focus{
	    border-color:#eb2823 !important;
	    outline:0 !important;
	    box-shadow:0 0 0 .25rem #eb2823 !important;
    }

    .upFileError:hover{
	    border-color:#eb2823 !important;
	    outline:0 !important;
	    box-shadow:0 0 0 .25rem #eb2823 !important;
    }


	
</style>

 

<!-- HTML -->
<Label for="exampleFile">Fichier Text</Label>


{#if fileInput!=='' && error===0} <!--S'il y a un fichier et qu'il n'y a pas d'erreur-->

<div class="row">
    <div class="col-12 text-right">
    <div class="deletebtn">
    
        <Button class="btnFileUp" outline danger on:click={()=>{fileInput=''; transcript=''}} >
        Supprimer le fichier 
        <Icon name="trash" />
    </Button>
</div>
  </div> 
</div>

<div class="upFile" on:click={()=>{fileIDK.click();}}>
    <h1>
        <Icon name="file-text" />
    </h1>
        <p>
            {fileInput.name}
        </p>
</div>

{:else if error===1} <!-- S'il l'erreur 1 est présente -->
<div class="upFileError" on:click={()=>{fileIDK.click();}}>
    <h1>
        <Icon name="file-x" />
    </h1>
    <h1>
        Vous avez sélectionné plus d'un fichier
    </h1>
    <p>
        Veuillez sélectionner un seul fichier texte (.txt)
    </p>
</div>

{:else if error===2} <!-- S'il l'erreur 2 est présente -->
<div class="upFileError" on:click={()=>{fileIDK.click();}}> 
    <h1>
        <Icon name="file-x" />
    </h1>
    <h4>
        Vous avez sélectinné un fichier qui n'est pas de type texte
    </h4>
    <p>
        Veuillez sélectionner un fichier texte (.txt)
    </p>
</div>
{:else}  <!-- S'il y a pas de fichier -->
<div class="upFile" on:click={()=>{fileIDK.click();}}>
    <h1>
        <Icon name="file-earmark-plus" />
    </h1>
    <h4>
        Sélectionner votre fichier texte
    </h4>
    <p>
        (txt)
        
    </p>
</div>
{/if}



<input style="display:none" type="file"  on:change={(e)=>onFileSelected(e)} bind:this={fileIDK} >

{#if fileInput!=='' && error === 0}
    {#await readText()}
        <p>Chargement <Spinner primary /></p>
    {:then text}
    <br/>
        <Button block type="button" color="primary" on:click={() => {(isOpen = !isOpen); console.log(isOpen)}} class="mb-3">
            Voir le texte original <i class="bi bi-eye" />
        </Button>
        <Collapse {isOpen}>
            <Card >
                <CardBody>
                    <CardText>
                        {text}
                    </CardText>                
                </CardBody>
            </Card>
        </Collapse>
        <h5>Modifiez le texte original ci-dessous si besoin</h5>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
{/if}