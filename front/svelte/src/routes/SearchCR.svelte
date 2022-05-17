<script>
    import CardCr from "../components/cardCR.svelte";
    let data = "nothing"
    let number_data
    function onSearch(){
        fetch("http://localhost:8080/api/summaries/search", 
            {
                method : 'post',
                headers: { "Content-Type": "application/json" },
                body : JSON.stringify({
                    "research" : document.getElementById("searchbar").value,
                    "margin" : 5
                }, 0, 2)
            }
        ).then((response)=>{
            response.json().then(
                (json)=>{
                    data=json
                    number_data = data.length;
                }

            )
        })
    }

    function handleKey(event){
        if (event.code=="Enter"){
            onSearch()
        }
    }
</script>

<!--Breadcrump navigation-->
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item">
            <a href="/#"><i class="bi bi-house-door-fill" /> Accueil</a>
        </li>
        <li class="breadcrumb-item active" aria-current="page">
            Recherche CR
        </li>
    </ol>
</nav>

<div class="indent">
    <p class="display-4">Rechercher un contenu dans un CR</p>
    <hr class="line" />
</div>

<div class="generatebody">
    <div class="row">
        <div class="col-10">
            <input id="searchbar" class="form-control me-2" type="search" placeholder="Entrez une phrase à rechercher" aria-label="Search" on:keypress={handleKey}>
        </div>
        <div class="col-2 text-right">
            <button class="btn btn-primary" on:click={onSearch}>Rechercher <i class="bi bi-search" /></button>
        </div>
    </div>
    <br>
    {#if data == "nothing"}
    <div class="alert alert-secondary" style="background-color: #F2F2F2 !important;" role="alert">
        <p class="lead" style="text-align: center !important;">
            <strong style="color: #ADB5BD;">Effectuez votre recherche... <i class="bi bi-search" /></strong>
        </p>
      </div>

    {:else}
        {#if data == ""}
        <div class="alert alert-secondary" style="background-color: #F2F2F2 !important;" role="alert">
            <p class="lead" style="text-align: center !important;">
                <strong style="color: #B0B8BF;">Désolé... aucun résultat ne correspond à votre recherche</strong>                
            </p>
            <p class="lead" style="text-align: center !important;">
                <strong style="color: #B0B8BF;">Veuillez réessayer</strong>
            </p>
          </div>

        {:else}
            <div class="d-block px-3 py-2 text-left text-bold text-dark" style="background-color: #EDEDF3 !important; border-radius: 5px !important;">
                <div href="#" class="badge badge-light"> {number_data}</div> CR trouvés
            </div>
            <br>
            {#each data as cr}
                <CardCr data = {cr} />
            {/each}
        {/if}
    {/if}
</div>