console.log("INSIDE firebase.js")

import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import {setPersistence, browserLocalPersistence } from 'firebase/auth';



console.log("imported firebase")

//Your web app's Firebase configuration
	// For Firebase JS SDK v7.20.0 and later, measurementId is optional


const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);


// Set persistence
setPersistence(auth, browserLocalPersistence);



export { auth, db };
