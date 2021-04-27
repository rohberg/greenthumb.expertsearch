<script>
  let searchstring = '';
  let region = 'all regions';
  const menuregions = [
    'all regions',
    'Zürich',
    'Basel',
    'Winterthur'
  ]
  
  const handleClickRegion = (event) => {
    region = event.target.value;
    console.log(searchstring, region);
  }
</script>

<h2>Expert Search</h2>
<form action="">
  <input class="searchstring" bind:value={searchstring} placeholder="search">
  <br>
  {#each menuregions as region}
    <input 
      type=button
      class="regionbutton"
      on:click|preventDefault={handleClickRegion}
      value={region}>
  {/each}
</form>
<p><i>Search{#if searchstring}{' '}for {searchstring}{/if} in {region}</i></p>