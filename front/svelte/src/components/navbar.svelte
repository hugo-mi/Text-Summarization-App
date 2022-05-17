<script>
  let logo_aubay = "img/aubay.png";
  let logo = "Aubay logo";
</script>

<div class="d-block px-3 py-2 text-center text-bold text-dark" style="background-color: #EDEDF3 !important;">
  Ceci est une version <div href="#" class="badge badge-light"> Bêta</div>
</div>

<nav style="z-index: 100 !important;" class="navbar sticky-top navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <div class="d-inline-block align-text-top">
      <a class="navbar-brand" href="/#"
        ><img class="logo_aubay" src={logo_aubay} alt={logo} /> AubaySum
      </a>
    </div>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarText"
      aria-controls="navbarText"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon" />
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="navbar-brand" href="/#"
            ><i
              class="bi bi-house-door-fill"
              style="color:#ec771e !important; margin-left: 60px !important;"
            /> Accueil</a
          >
        </li>
        <li class="nav-item" />
        <li class="nav-item" />
      </ul>
      <span class="navbar-text">
        <a class="btn btn-primary" href="#/GeneratorCR/"
          >Générer un CR <i class="bi bi-gear-fill" /></a
        >
      </span>
      <span class="navbar-text" href="#/HistoriqueCR">
        <a class="btn btn-outline-secondary" href="#/HistoriqueCR"
          >Historique des CR <i class="bi bi-file-text" /></a
        >
      </span>
      <span style="margin-left: 10px !important;" class="navbar-text" href="#/SearchCR">
        <a class="btn btn-outline-secondary" href="#/SearchCR"
          >Rechercher un CR <i class="bi bi-search" /></a
        >
      </span>
    </div>
  </div>
</nav>

<style>
  .btn-primary:hover {
    color: #ec771e !important;
    border-color: #ec771e !important;
    background-color: white !important;
  }

  .btn-primary {
    color: white !important;
    background-color: #ec771e !important;
    border-color: #ec771e !important;
    margin-right: 10px !important;
  }

  .btn-outline-secondary {
    color: #ec5646 !important;
    border-color: #ec5646 !important;
  }

  .btn-outline-secondary:hover {
    color: white !important;
    background-color: #ec5646 !important;
    border-color: #ec5646 !important;
  }
</style>