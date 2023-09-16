

<script>
    //import mapStyles from './map-styles'; // optional
    import { onMount } from "svelte";
    import MenuBar from "./MenuBar.svelte";
    //import { Client } from "@googlemaps/google-maps-services-js";

    let container;
    let map;
    let zoom = 8;
    let location = { lat: -34.397, lng: 150.644 };

    console.log("starting mounting....");
    onMount(async () => {
        const {Map} = await google.maps.importLibrary("maps"); 
        map = new Map(container, {
            zoom: 4,
            center: location
            //styles: mapStyles // optional
        });

        console.log("after onMount....");
    });
</script>

<MenuBar items={[{ href: "/dashboardMap", label: "Map" },{ href: "/feed", label: "Feed" },]}/>
<div class="full-screen" bind:this={container} />


<style>
    .full-screen {
        width: 100vw;
        height: 100vh;
    }
</style>
