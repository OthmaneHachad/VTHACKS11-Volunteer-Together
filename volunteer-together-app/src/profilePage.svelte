<script>
    import { collection, setDoc, doc, getDoc, addDoc, query } from 'firebase/firestore';
   
    import MenuBar from './MenuBar.svelte';
    import { onMount } from 'svelte';
    import { auth, db } from './firebase.js';

    // Creating a Profile 
    let firstName = '';
    let lastName = '';
    let email = '';
    let phoneNumber = '';

    const userCollection = collection(db, 'users'); // pointing to the 'posts' collection in Firestore

    async function saveProfile() {
        const newUser = {
            firstName: firstName,
            lastName: lastName,
            email: email,
            phoneNumber: phoneNumber
        };
        try {
            await addDoc(userCollection, newUser);
            firstName = ''; // reset the title
            lastName = ''; // reset the content
            email = ''; // reset the location
            phoneNumber = 0;
        } catch (e) {
            console.error("Error adding document to database: ", e);
        }
    }






    let userUid = null; // Initialize userUid variable

    onMount(async () => {
    // Make sure the user is authenticated
    if (auth.currentUser) {
        userUid = auth.currentUser.uid; // Get the UID of the currently authenticated user

        try {
            // Create a reference to the user's document in Firestore
            const userDocRef = doc(db, 'users', userUid);

            // Fetch the document
            const userProfile = await getDoc(userDocRef);
            
            if (userProfile.exists()) {
                const data = userProfile.data();
                firstName = data.firstName;
                lastName = data.lastName;
                email = data.email;
                phoneNumber = data.phoneNumber;
            } else {
                console.warn('No profile found for the current user');
            }
        } catch (e) {
            console.error("Error fetching profile: ", e);
        }
    } else {
        console.warn('No user is currently authenticated');
    }
});

</script>

<MenuBar items={[{ href: "/dashboardMap", label: "Map" },{ href: "/feed", label: "Feed" }, { href: "/profilePage", label: "Profile" }]}/>

<div class="profile-container">
    <h1>Your Profile</h1>
    
    <input bind:value={firstName} placeholder="First Name" />
    <input bind:value={lastName} placeholder="Last Name" />
    <input bind:value={email} placeholder="Email" />
    <input bind:value={phoneNumber} placeholder="Phone Number" />

    <button on:click={saveProfile}>Save Profile</button>
</div>

<style>
    

    .profile-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 300px;
        margin: 20px auto;
        padding: 20px;
        padding-top: 150px;
        border: 1px solid #2e0707;
        border-radius: 5px;
    }

    button {
        align-self: flex-end;
        padding: 5px 10px;
    }

</style>