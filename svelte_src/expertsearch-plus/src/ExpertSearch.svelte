<script>
    import { onMount } from "svelte";
    import { scale } from "svelte/transition";
    import { flip } from "svelte/animate";

    let searchstring = '';
    let region = 'all regions';
    const menuregions = [
      'all regions',
      'Zürich',
      'Basel',
      'Winterthur'
    ]

    let apiURL = process.env.isProd ? '/' : 'http://localhost:8080/Plone/';
  apiURL = apiURL + '@search?portal_type=dexterity.membrane.member&fullobjects=1&sort_on=last_name&sort_order=ascending';

  let experts = [];

  async function getExperts(url=apiURL) {
    fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      }
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      experts = data?.items || [];
      return experts;
    })
    .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
    });
  };

  onMount(() => {
    getExperts()
  }) 

  const handleClickRegion = (event) => {
    region = event.target.value;
    getExperts((region == 'all regions') ? apiURL : apiURL + '&region=' + encodeURI(region));
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

  <div class="cards">
    {#each experts as expert, i (expert['@id'])}
      <div class="card" transition:scale animate:flip={{ duration: 300 }}>
        <span class="fullname">{expert.first_name} {expert.last_name}</span>
        <br>
        <span class="competence">{expert.competence}</span>
        <br>
        <span class="organisation">{expert.organisation}</span>
        <br>
        <span class="region">{expert.region}</span>
      </div>
    {:else}
      <p>no experts found</p>
    {/each}
  </div>
