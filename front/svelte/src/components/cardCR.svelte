<script>

    import { beforeUpdate } from "svelte";

    import {
      Button,
      Card,
      CardBody,
      CardFooter,
      CardHeader,
      CardSubtitle,
      CardText,
      CardTitle,
      Badge,
    } from 'sveltestrap';

    export let data;

    let extractAbs;
    let extractExt;

    function strongString(string, start, end){
        let before = string.substring(0, start)
        let inner = string.substring(start, end)
        let after = string.substring(end, string.len)
        const STRONGOPEN = "<strong>"
        const STRONGCLOSE = "</strong>"
        return before+STRONGOPEN+inner+STRONGCLOSE+after

    }

    function formattingCR(){
        if (typeof(data.matches.extractive) != "undefined"){

            if (typeof(data.matches.extractive.edited) != "undefined"){
                extractExt =  data.matches.extractive.edited.extract;
                extractExt = strongString(extractExt, data.matches.extractive.edited.start, data.matches.extractive.edited.end);
            }
            else{
                extractExt =  data.matches.extractive.raw.extract;
                extractExt = strongString(extractExt, data.matches.extractive.raw.start, data.matches.extractive.raw.end);
            }
        }
        
        if (typeof(data.matches.abstractive) != "undefined"){
            if (typeof(data.matches.abstractive.edited) != "undefined"){
                extractAbs =  data.matches.abstractive.edited.extract;
                extractAbs = strongString(extractAbs, data.matches.abstractive.edited.start, data.matches.abstractive.edited.end);
            }
            else{
                extractAbs =  data.matches.abstractive.raw.extract;
                extractAbs = strongString(extractAbs, data.matches.abstractive.raw.start, data.matches.abstractive.raw.end);
            }
        }
    }

    beforeUpdate(formattingCR);
</script>

<Card class="mb-3">
    <CardHeader>
        <div class="row">
            <div class="col">
                <CardTitle>{data.title}</CardTitle>
            </div>
            <div class="col text-right">      
                <Badge seondary>{data.projectGroup}</Badge>
            </div>
        </div>
    </CardHeader>
    <CardBody>
        {#if typeof(data.matches.extractive) != "undefined"}
            <CardSubtitle>Extractif</CardSubtitle>
            <CardText>
                {@html extractExt}
            </CardText>
        {/if}
        {#if typeof(data.matches.abstractive) != "undefined"}
            <CardSubtitle>Abstractif</CardSubtitle>
            <CardText>
                {@html extractAbs}
            </CardText>
        {/if}
      <a class="btn btn-primary" href="#/VoirCR/{data.id}">Voir <i class="bi bi-eye" /></a>    
    </CardBody>
    <CardFooter>{data.date}</CardFooter>
</Card>