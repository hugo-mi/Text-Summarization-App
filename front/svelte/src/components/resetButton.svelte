<script>
  import { crJSON } from '../components/store.js';
  import { onMount , createEventDispatcher} from "svelte";
  import {
    Button,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
    Tooltip
  } from 'sveltestrap';
  let open = false;
  const toggle = () => (open = !open);

  const dispatch = createEventDispatcher();

  export let params = {};
	console.log(params);
	export let idCR;
  export let crType;
  console.log(idCR);

    function Reset(){
        console.log($crJSON.id);
        fetch("http://localhost:8080/api/summary/"+crType+"/"+idCR, 
                {
                    method : 'post',
                    headers: { "Content-Type": "application/json" },
                    redirect: 'follow'
                }).then((response) => {
                    console.log("CR Ext reseted");
                    dispatch('reset_cr');
                }) 
    }

</script>

<div>
  <Button id="resetButton{crType}" secondary on:click={toggle}>Reset <i class="bi bi-arrow-counterclockwise"></i></Button>
  <Tooltip target="resetButton{crType}" bottom>Revenir au CR original</Tooltip>
  <Modal isOpen={open} {toggle}>
    <ModalHeader {toggle}>Reset du CR</ModalHeader>
    <ModalBody>
      Souhaitez-vous revenir au CR original ? <br>
      <p><i class="bi bi-exclamation-circle-fill"></i> Attention tous vos changements seront perdus</p>
    </ModalBody>
    <ModalFooter>
      <Button color="primary" on:click={Reset}>Oui <i class="bi bi-check-circle"></i></Button>
      <Button color="secondary" on:click={toggle}>Non <i class="bi bi-x-circle"></i></Button>
    </ModalFooter>
  </Modal>
</div>
