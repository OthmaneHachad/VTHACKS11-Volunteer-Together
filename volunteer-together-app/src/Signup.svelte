<script>
    import { onMount, onDestroy } from 'svelte';
    import { auth } from './firebase.js';
    import { createUserWithEmailAndPassword, onAuthStateChanged } from 'firebase/auth';
    import { navigate } from 'svelte-routing';

    let email = '';
        let password = '';

        const signUp = async () => {
            try {
                const userCredential = await createUserWithEmailAndPassword(auth, email, password);
                console.log("User signed up:", userCredential.user);
                navigate("/dashboardMap");  // Or use svelte-routing's navigate
            } catch (error) {
                console.error("Error signing up:", error);
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

<input bind:value={email} placeholder="Email" />
<input type="password" bind:value={password} placeholder="Password" />
<button on:click={signUp}>Sign Up</button>