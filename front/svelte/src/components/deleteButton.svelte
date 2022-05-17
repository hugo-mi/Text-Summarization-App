<script>
    import { onMount , createEventDispatcher} from "svelte";

    import {
    Button,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader
  } from 'sveltestrap';
  let open = false;
  const toggle = () => (open = !open);
  
  const dispatch = createEventDispatcher()
    export let idCR;
    export let index;

      onMount(async () => {
          console.log(index + ":" + idCR);
      });
  
    function Delete(id){
          console.log(id);
          fetch("http://localhost:8080/api/summary/"+id+"/delete", 
                  {
                      method : 'get',
                      headers: { "Content-Type": "application/json" },
                      redirect: 'follow'
                  }).then((response) => {
                      console.log("CR deleted");
                      dispatch('reload_hist')
                      
                      //window.location.reload();
                      //return false;
                  }) 
      }

  </script>
  
  <div>
    <Button outline danger on:click={toggle}>Supprimer <i class="bi bi-trash"></i></Button>
    <Modal isOpen={open} {toggle}>
      <ModalHeader {toggle}>Suppression du CR</ModalHeader>
      <ModalBody>
        Souhaitez-vous supprimer le CR ? <br>
        <p><i class="bi bi-exclamation-circle-fill"></i> Attention toutes les informations seront perdues</p>
      </ModalBody>
      <ModalFooter>
        <Button color="primary" on:click={Delete(idCR)}>Oui <i class="bi bi-check-circle"></i></Button>
        <Button color="secondary" on:click={toggle}>Non <i class="bi bi-x-circle"></i></Button>
      </ModalFooter>
    </Modal>
  </div>