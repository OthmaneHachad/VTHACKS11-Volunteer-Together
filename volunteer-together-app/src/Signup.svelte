<script>
    import { onMount, onDestroy } from 'svelte';
    import { auth } from './firebase.js';
    import { createUserWithEmailAndPassword,signInWithEmailAndPassword, onAuthStateChanged } from 'firebase/auth';
    import { navigate } from 'svelte-routing';

    let emailSignUp = '';
    let passwordSignUp = '';
    let emailLogIn = '';
    let passwordLogIn = '';

        const signUp = async () => {
            try {
                const userCredential = await createUserWithEmailAndPassword(auth, emailSignUp, passwordSignUp);
                console.log("User signed up:", userCredential.user);
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

<div class="container">
    <div class="connectUser" id="createUser">
        <h1>Start volunteering now !</h1>
        <input bind:value={emailSignUp} placeholder="Email" />
        <input type="password" bind:value={passwordSignUp} placeholder="Password" />
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