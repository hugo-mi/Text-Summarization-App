<script>
    import { onMount } from "svelte";
    import { poll } from "../poll.js";
    import { Circle } from "svelte-loading-spinners";
    import DeleteButton from "../components/deleteButton.svelte";
    import ResetButton from "../components/resetButton.svelte";

    let imgGenererCR = "img/genererCR.png";
    let imghistoriqueCR = "img/historiqueCR.png";

    let summaries = [];

    onMount(async () => {
        const res = await fetch(`http://localhost:8080/api/summaries/list`);
        summaries = await res.json();
    });

    function handleMessageDelete(event){
        const res = fetch(`http://localhost:8080/api/summaries/list`).then((res)=>{res.json().then(
            (json) => {summaries=json}
        )})
    }

    poll(() => {handleMessageDelete("")}, 2000)

    function searchFunction() {
        var input, filter, table, tr, td, i, j, txtValue;
        input = document.getElementById("searchInput");
        if (input != null) {
            filter = input.value.toUpperCase();
            table = document.getElementById("summ");
            tr = table.getElementsByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td");
                if (td) {
                    for (j = 0; j < td.length - 1; j++) {
                        txtValue = td[j].textContent || td[j].innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {
                            tr[i].style.display = "";
                            break;
                        } else {
                            tr[i].style.display = "none";
                        }
                    }
                }
            }
        }
    }

    function sortTable(n) {
        var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
        table = document.getElementById("summ");
        switching = true;
        dir = "asc";
        while (switching) {
            switching = false;
            rows = table.rows;
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("TD")[n];
                y = rows[i + 1].getElementsByTagName("TD")[n];
                if (dir == "asc") {
                    if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                    }
                } else if (dir == "desc") {
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
                switchcount ++;
            } else {
                if (switchcount == 0 && dir == "asc") {
                    dir = "desc";
                    switching = true;
                }
            }
        }
    }

</script>

<style lang="scss">
    .actions {
        display: flex;
        flex-direction: row;
        &-loading {
            margin-right: 1em;
        }
    }
    #summ {
        font-family: Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    #summ td,
    #summ th {
        text-align: left;
        border: 1px solid #ddd;
        padding: 12px;
    }

    #summ tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    #summ tr:hover {
        background-color: #ddd;
    }
    #summ th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #ec771e;
        color: white;
    }

    #summ th:hover {background-color:  #c9671d;}

    #searchInput {
        width: 100%; 
        font-size: 16px; 
        padding: 12px 20px 12px 40px; 
        border: 1px solid #ec771e; 
        margin-bottom: 12px; 
    }

    #searchIcon {
        position: absolute;
        margin-bottom: 12px;
        padding: 20px;
        color: #808080;
    }

</style>
<!--Breadcrump navigation-->
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item">
            <a href="/#"><i class="bi bi-house-door-fill" /> Accueil</a>
        </li>
        <li class="breadcrumb-item active" aria-current="page">
            Historique des CR
        </li>
    </ol>
</nav>

<div class="indent">
    <p class="display-4">Historique des CR</p>
    <hr class="line" />
</div>

<div class="generatebody">
    <i id="searchIcon" class="fa fa-search form-control-feedback"></i>
    <input
        type="text"
        id="searchInput"
        on:keyup={searchFunction}
        placeholder="Recherche ..."
    />

    <div style="overflow-x:auto;">
        <table id="summ">
            <thead>
                <tr>
                    <th on:click={() => sortTable(0)}>Nom du CR <i class="bi bi-sort-alpha-down"></i></th>
                    <th on:click={() => sortTable(1)}>Projet <i class="bi bi-sort-alpha-down"></i></th>
                    <th on:click={() => sortTable(2)}>Date <i class="bi bi-sort-numeric-down"></i></th>
                    <th on:click={() => sortTable(3)}>Participants <i class="bi bi-sort-alpha-down"></i></th>
                    <th on:click={() => sortTable(4)}>Créateur <i class="bi bi-sort-alpha-down"></i></th>
                    <th>Actions</th>
                </tr>
            </thead>
            {#each summaries as data, i (data.id)}
                <tr>
                    <td>{data.title}</td>
                    <td>{data.projectGroup}</td>
                    <td>{data.date}</td>
                    <td>{data.attendees}</td>
                    <td>{data.generatorName}</td>
                    {#if data.status == "done"}
                        <td class="actions">
                            <a
                                class="btn btn-primary"
                                href="#/VoirCR/{data.id}"
                                >Voir <i class="bi bi-eye" />
                            </a>
                            <DeleteButton idCR={data.id} index={i} on:reload_hist={handleMessageDelete}/>
                        </td>
                    {:else}
                        <td class="actions">
                            <div class="actions-loading">
                                <Circle
                                    size="1.7"
                                    unit="em"
                                />
                            </div>

                            En cours de traitement ...
                        </td>
                    {/if}
                </tr>
            {/each}
        </table>
    </div>
</div>