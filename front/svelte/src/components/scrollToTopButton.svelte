<script>
    window.onscroll = function()
{
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20)
    {
    	document.getElementById("scroll-btn").style.display = "block";
    }
    else
    {
    	document.getElementById("scroll-btn").style.display = "none";
    }
};

function scrollToTop()
{
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox and Opera
}
</script>
<style>
    #scroll-btn{
    background-color: white;
    border: 1px solid #ec771e;
    border-radius: 20px;
    bottom: 20px;
    color: #ec771e;
    cursor: pointer;
    display: none;
    padding: 10px 15px 7px;
    position: fixed;
    right: 30px;
    z-index: 99;
    font-size: 20px;
    }

    #scroll-btn:hover{
    background-color: #ec771e;
    color:white;
    }

</style>

<button on:click={scrollToTop} id="scroll-btn" title="Go to top"><i class="bi bi-arrow-up-circle"></i></button>
