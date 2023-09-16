<script>
    
    import { db } from './firebase.js'; // assuming you have initialized Firebase here
    import { collection, addDoc, query, getDocs } from 'firebase/firestore';
    import MenuBar from './MenuBar.svelte';
    import { onMount } from 'svelte';

    //creating posts
    let newTitle = '';
    let newContent = '';
    let poster_uid = '';

    let posts = [];

    const postsCollection = collection(db, 'posts'); // pointing to the 'posts' collection in Firestore

    async function addPost() {
        const newPost = {
            title: newTitle,
            content: newContent,
            poster_uid: poster_uid,
            timestamp: Date.now() // this will help in ordering posts by creation time
        };
        try {
            await addDoc(postsCollection, newPost);
            newTitle = ''; // reset the title
            newContent = ''; // reset the content
        } catch (e) {
            console.error("Error adding document to database: ", e);
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


<MenuBar items={[{href: '/dashboardMap', label: 'Map'},{href: '/feed', label: 'Feed'}]} />

<div class="post-form">
    <input bind:value={newTitle} placeholder="Post Title" />
    <textarea bind:value={newContent} placeholder="Post Content"></textarea>
    <!-- Assuming the user is authenticated and you can get their UID, otherwise you might want to handle this differently -->
    <input type="hidden" bind:value={poster_uid} />
    <button on:click={addPost}>Add Post</button>
</div>

<section class="posts">
    {#each posts as post}
        <div class="post">
            <h2>{post.title}</h2>
            <p>{post.content}</p>
            <small>Posted by: {post.poster_uid}</small>
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
</style>
