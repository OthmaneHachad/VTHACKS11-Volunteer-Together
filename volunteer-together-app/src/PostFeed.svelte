<script>
    
    import { db } from './firebase.js'; // assuming you have initialized Firebase here
    import { collection, addDoc, query, getDocs } from 'firebase/firestore';
    import MenuBar from './MenuBar.svelte';
    import { onMount } from 'svelte';

    //creating posts
    let newTitle = '';
    let newContent = '';
    let posterUid = '';
    let locationAddress = '';
    let posts = [];

    const postsCollection = collection(db, 'posts'); // pointing to the 'posts' collection in Firestore

    async function addPost() {
        const newPost = {
            title: newTitle,
            content: newContent,
            poster_uid: posterUid,
            timestamp: Date.now(), // this will help in ordering posts by creation time
            location_address: locationAddress,
            location_coordinates: await geocodeAddress(locationAddress)
        };
        try {
            await addDoc(postsCollection, newPost);
            newTitle = ''; // reset the title
            newContent = ''; // reset the content
            locationAddress = ''; // reset the location
        } catch (e) {
            console.error("Error adding document to database: ", e);
        }
    }

    async function geocodeAddress(address) {
        const apiKey = 'AIzaSyAQdXjUnjQHJINv-x9Z_tLpSo7nL7_qo9o';
        const apiUrl = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(address)}&key=${apiKey}`;

        const response = await fetch(apiUrl);
        const data = await response.json();

        if (data.status === 'OK') {
            const location = data.results[0].geometry.location;
            return location; // Returns an object with { lat, lng }
        } else {
            throw new Error('Failed to geocode address');
        }
    }

    // Fetch posts only when component is mounted
    onMount(async () => {
        const q = query(postsCollection);
        const querySnapshot = await getDocs(q);
        const fetchedPosts = querySnapshot.docs.map(doc => ({
            id: doc.id, 
            ...doc.data()
        }));
        posts = fetchedPosts;
    });

</script>


<MenuBar items={[{ href: "/dashboardMap", label: "Map" },{ href: "/feed", label: "Feed" }, { href: "/profilePage", label: "Profile" }]}/>
<div class="post-form">
    <input bind:value={newTitle} placeholder="Post Title" />
    <textarea bind:value={newContent} placeholder="Post Content"></textarea>
    <!--Location where the action will be made-->
    <input bind:value={locationAddress} placeholder="Donation Address" />
    <!-- Assuming the user is authenticated and you can get their UID, otherwise you might want to handle this differently -->
    <input type="hidden" bind:value={posterUid} />
    <button on:click={addPost}>Add Post</button>
</div>

<section class="posts">
    {#each posts as post}
        <div class="post">
            <h2>{post.title}</h2>
            <p>{post.content}</p>
            <small>Posted by: {post.poster_uid}</small>
            <small>Location: {post.location_address}</small>
        </div>
    {/each}
</section>

<style>
    .post-form {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 300px;
        margin: 20px auto;
        padding-top: 150px;
    }

    .posts {
        display: flex;
        flex-direction: column;
        gap: 20px;
        width: 80%;
        margin: 20px auto;
    }

    .post {
        padding: 15px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    small {
        display: block;
    }
</style>
