

<script>
    //import mapStyles from './map-styles'; // optional
    import { onMount } from "svelte";
    import MenuBar from "./MenuBar.svelte";
    import { db } from './firebase.js'; 
    import { collection, query, getDocs } from 'firebase/firestore';
    //import {useParams} from 'svelte-routing';

    let container;
    let map;
    let zoom = 6;
    //let {params} = useParams();
    let location = {lat: 31.055732146452986, lng: -8.377009998795002};

    let posts = [] ;
    const postsCollection = collection(db, "posts"); // posts collection in Firestore

    console.log("starting mounting....");
    onMount(async () => {
        // Ensure the Google Maps library is loaded
        if (typeof google === 'undefined' || typeof google.maps === 'undefined') {
            console.error('Google Maps library is not loaded properly.');
            return;
        }
        
        map = new google.maps.Map(container, {
            zoom: zoom,
            minZoom: zoom - 3,
            center: location
            //styles: mapStyles // optional
        });

        // Fetch posts from Firestore
        const q = query(postsCollection);
        const querySnapshot = await getDocs(q);
        posts = querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));

        // Place pins for each geolocation from the fetched posts
        posts.forEach(post => {
            if (post.location_coordinates) {
                const location = post.location_coordinates;

                // Parse the lat and lng as floats to ensure they are numbers
                const lat = parseFloat(location.lat);
                const lng = parseFloat(location.lng);


                if (!isNaN(lat) && !isNaN(lng)) { // Ensure they are valid numbers
                    const marker = new google.maps.Marker({
                        position: { lat: lat, lng: lng },
                        map: map,
                        title: post.title
                    });

                    // Add an info window for each marker
                    const infoContent = `
                        <div>
                            <h4>${post.title}</h4>
                            <p>${post.content}</p>
                        </div>
                    `;

                    const infoWindow = new google.maps.InfoWindow({
                        content: infoContent
                    });

                    marker.addListener("click", () => {
                        infoWindow.open(map, marker);
                    });
                }
            }
        });
    });
    /*onMount2(async () => {
        const {Map, Marker, InfoWindow} = await google.maps.importLibrary("maps"); 
        map = new Map(container, {
            zoom: 4,
            center: location
            //styles: mapStyles // optional
        });

        // Fetch posts from Firestore
        const q = query(postsCollection);
        const querySnapshot = await getDocs(q);
        posts = querySnapshot.docs.map(doc => ({
            id: doc.id,
            ...doc.data()
        }));

        // Place pins for each geolocation from the fetched posts
        posts.forEach(post => {
            const location = post.location_coordinates;
            const marker = new Marker({
                position: { lat: location.lat, lng: location.lng },
                map: map,
                title: post.title
            });

            // Add an info window for each marker
            const infoContent = `
                <div>
                    <h4>${post.title}</h4>
                    <p>${post.content}</p>
                </div>
            `;

            const infoWindow = new InfoWindow({
                content: infoContent
            });

            marker.addListener("click", () => {
                infoWindow.open(map, marker);
            });
        });

        console.log("after onMount....");
    });*/
</script>

<MenuBar items={[{ href: "/dashboardMap", label: "Map" },{ href: "/feed", label: "Feed" }, { href: "/profilePage", label: "Profile" }]}/>
<div class="full-screen" bind:this={container} />


<style>
    .full-screen {
        width: 100vw;
        height: 100vh;
    }
</style>
