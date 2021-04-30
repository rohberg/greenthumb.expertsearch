<script>
  import { scale } from "svelte/transition";
  import { flip } from "svelte/animate";
  import { SyncLoader } from 'svelte-loading-spinners'

  const regions = [
    'all regions',
    'Zürich',
    'Basel',
    'Winterthur'
  ]

  const apiUrl = process.env.isProd ? '/' : 'http://localhost:8080/Plone/';
  const searchApiUrl = apiUrl + '@search?portal_type=dexterity.membrane.member&fullobjects=1&sort_on=last_name&sort_order=ascending';

  // state of component
  let searchstring = '';
  let region = 'all regions';
  $: searchUrl = ((region == 'all regions') ? searchApiUrl : searchApiUrl + '&region=' + encodeURI(region))
      + (searchstring ? ('&SearchableText=' + searchstring + '*') : '');
  let experts = [];
  let isLoading = false;

  $: getExperts(searchstring, region);

  async function getExperts(mysearchstring, myregion) {
    isLoading = true;

    // search from 3 letters on
    // search also for empty searchstring to get all
    if ([1,2].includes(mysearchstring.length)) {
      return
    }

    fetch(searchUrl, {
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
    })
    .finally(() => isLoading=false);
  };

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
<p><i>Results{#if searchstring}{' '}for {searchstring}{/if} in {region}</i></p>

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
  {#if isLoading}
    <div class="spinner">
      <SyncLoader size="30" color="#007cbf" unit="px" duration="2s"></SyncLoader>
    </div>
  {/if}
</div>

<style>

  h2 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  input {
    margin: .2rem;
  }

  .cards {
    display: flex;
    flex-wrap: wrap;
    margin-top: 2rem;
  }
  .card {
    width: 15rem;
    min-height: 10em;
    background: white;
    margin: 0 1rem 1rem 0;
    padding: 1.5rem 1rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    border-radius: 3px;
  }
</style>