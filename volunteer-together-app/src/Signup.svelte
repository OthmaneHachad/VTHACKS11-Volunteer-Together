<script>
    import { onMount, onDestroy } from 'svelte';
    import { auth, db } from './firebase.js';
    import { createUserWithEmailAndPassword,signInWithEmailAndPassword, onAuthStateChanged } from 'firebase/auth';
    import {doc, setDoc} from 'firebase/firestore'
    import { navigate } from 'svelte-routing';

    let emailSignUp = '';
    let passwordSignUp = '';
    let emailLogIn = '';
    let role = "volunteer" ;
    let passwordLogIn = '';

    let roleOptions = ['volunteer', 'host', 'delivery'];  // Added a default option

    const handleDropdownChange = (event) => {
        role = event.target.value;
    };


    const signUp = async () => {
        try {
            const userCredential = await createUserWithEmailAndPassword(auth, emailSignUp, passwordSignUp);
            console.log("User signed up:", userCredential.user);
            // Store the role in the Firebase Firestore
            const userRef = doc(db, 'users', userCredential.user.uid);
            await setDoc(userRef, {
                role: role
            });
            navigate("/dashboardMap");  // Or use svelte-routing's navigate
        } catch (error) {
            console.error("Error signing up:", error);
        }
    };

        const login = async () => {
            try {
                const userCredential = await signInWithEmailAndPassword(auth, emailLogIn, passwordLogIn);
                console.log("User logged in:", userCredential.user.uid);
                navigate("/dashboardMap");
            } catch (error) {
                console.error("Error logging in:", error);
            }
        };

        /**
         * call-back function that makes sure the event-listener doesn't get updated
         * anymore
         * */ 

        let unsubscribe;

        onMount(() => {
            unsubscribe = firebase.auth().onAuthStateChanged(newUser => {
                user = newUser;
            });

        });

        //onDestroy(() => {
        //    unsubscribe();
        //});
</script>

<h1>Volunteer Together !</h1>
<p>This web app lets people come together and help those in need. Spread awareness and help your fellow brothers and sisters. The idea originates from the late earthquakes Morocco has faced. It seemed like people were unable to support the victims of those disastrous events other than through professional organization.
     Here, you can choose to be a volunteer and participate in donations, be a host and lend some space to store those donations, or be a delivery person and make sure those donations are brought to those who need it.
</p>
<div class="container">
    <div class="connectUser" id="createUser">
        <h1>Start volunteering now !</h1>
        <input bind:value={emailSignUp} placeholder="Email" />
        <input type="password" bind:value={passwordSignUp} placeholder="Password" />
        <!-- Role dropdown -->
        <div class="roleDropdown">
            <select bind:value={role} on:change={handleDropdownChange}>
                {#each roleOptions as roleOption}
                    <option value={roleOption}>{roleOption}</option>
                {/each}
            </select>
        </div>
        
        <button on:click={signUp}>Sign Up</button>
    </div>

    <div class="connectUser" id="SignInUser">
        <h1>Already a volunteer ?</h1>
        <input bind:value={emailLogIn} placeholder="Email" />
        <input type="password" bind:value={passwordLogIn} placeholder="Password" />

        <button on:click={login}>Log In</button>
    </div>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh; /* This assumes you want to vertically center them on the entire screen. Adjust as needed. */
    }

    .connectUser {
        margin: 0 50px; /* Increased space between the two divs */
        display: flex;
        flex-direction: column; /* Stack children vertically */
        align-items: flex-start; /* Align items to the left */
    }

    .connectUser input {
        width: 100%;
        margin-bottom: 10px; /* Add space between input fields and button */
    }

    .connectUser button {
        align-self: stretch; /* Stretch the button to the full width of its container */
    }
</style>