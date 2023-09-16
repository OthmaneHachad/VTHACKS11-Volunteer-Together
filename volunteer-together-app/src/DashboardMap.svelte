

<script>
    //import mapStyles from './map-styles'; // optional
    import { onMount } from 'svelte';
    import MenuBar from './MenuBar.svelte';


    let container;
    let map;
    let zoom = 8;
    let location = {lat: -34.397, lng: 150.644};
    
    
    
    onMount(async () => {
        const {Map} = await google.maps.importLibrary("maps"); 
        map = new Map(container, {
            zoom: 4,
            center: location
            //styles: mapStyles // optional
        });
    });
    </script>

    <style>
    .full-screen {
    width: 100vw;
    height: 100vh;
    }
    </style>

    <div class="full-screen" bind:this={container}></div>
    <MenuBar items={[{href: '/dashboardMap', label: 'Map'},{href: '/feed', label: 'Feed'}]} />