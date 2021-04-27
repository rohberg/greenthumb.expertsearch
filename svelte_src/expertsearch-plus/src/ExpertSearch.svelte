<script>
  const regions = [
    'all regions',
    'Zürich',
    'Basel',
    'Winterthur'
  ]

  // state of component
  let searchstring = '';
  let region = 'all regions';
  const handleClickRegion = (event) => {
    region = event.target.value;
  }
</script>

<h2>Expert Search</h2>
<form action="">
  <input class="searchstring" bind:value={searchstring} placeholder="search">
  <br>
  {#each regions as rgn}
    <input 
      type=button
      class="regionbutton"
      on:click|preventDefault={handleClickRegion}
      value={rgn}>
  {/each}
</form>
<p>
  <i>Results{#if searchstring}{' '}for {searchstring}{/if} in {region}</i>
</p>
