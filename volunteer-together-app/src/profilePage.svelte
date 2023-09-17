<script>
    import { collection, setDoc, doc, getDoc, query } from 'firebase/firestore';
import MenuBar from './MenuBar.svelte';
import { onMount, onDestroy } from 'svelte';
import { auth, db } from './firebase.js';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { writable } from 'svelte/store';

let firstName = writable('');
let lastName = writable('');
let email = writable('');
let phoneNumber = writable('');
let userUid = writable('');

async function fetchUserProfile(uid) {
    const userDocRef = doc(db, 'users', uid);
    const userProfile = await getDoc(userDocRef);
            
    if (userProfile.exists()) {
        const data = userProfile.data();
        // $userUid = data.userUid || '';
        $firstName = data.firstName || '';
        $lastName = data.lastName || '';
        $email = data.email || '';
        $phoneNumber = data.phoneNumber || '';
    } else {
        console.warn('No profile found for the current user');
    }
}

async function saveProfile() {
    const userUpdate = {
        firstName: $firstName,
        lastName: $lastName,
        email: $email,
        phoneNumber: $phoneNumber
    };

    if ($userUid) {
        try {
            await setDoc(doc(db, 'users', $userUid), userUpdate, { merge: true });
            console.log("Profile updated!");
        } catch (e) {
            console.error("Error updating profile: ", e);
        }
    } else {
        console.warn("No UID available for saving.");
    }
}

let unsubscribe;

onMount(() => {
    unsubscribe = onAuthStateChanged(auth, user => {
        if (user) {
            console.log("Before setting UID:", $userUid);  // Log before setting
            $userUid = user.uid;
            console.log("After setting UID:", $userUid);   // Log after setting

            $userUid = user.uid;
            fetchUserProfile(user.uid);
        } else {
            console.warn("No user is currently authenticated.");
        }
    });
});

onDestroy(() => {
    unsubscribe();
});





</script>


<MenuBar items={[{ href: "/dashboardMap", label: "Map" },{ href: "/feed", label: "Feed" }, { href: "/profilePage", label: "Profile" }]}/>

<div class="profile-container">
    <h1>Your Profile</h1>
    
    <input bind:value={$userUid} readonly />
    <input bind:value={$firstName} placeholder="First Name" />
    <input bind:value={$lastName} placeholder="Last Name" />
    <input bind:value={$email} placeholder="Email" />
    <input bind:value={$phoneNumber} placeholder="Phone Number" />

    <button on:click={saveProfile}>Save Profile</button>
</div>

<style>

   


    .profile-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 70vh;
        margin: 30px auto;
        padding: 20px;
        padding-top: 150px;
        border: 1px solid #2e0707;
        border-radius: 5px;
        height: 50vh; /* This assumes you want to vertically center them on the entire screen. Adjust as needed. */
    }

    button {
        align-self: flex-end;
        padding: 5px 10px;
    }
    input[readonly] {
    background-color: #f3f3f3;
    border: 1px solid #ccc;
    cursor: not-allowed;
}


</style>
