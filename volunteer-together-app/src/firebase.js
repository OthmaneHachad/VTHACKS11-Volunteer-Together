console.log("INSIDE firebase.js")

import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

console.log("imported firebase")

//Your web app's Firebase configuration
	// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyC_NeDzkny-iC73KLNxPDF2W5wUdnWVQ24",
    authDomain: "vt-hacks-11-volunteer-together.firebaseapp.com",
    projectId: "vt-hacks-11-volunteer-together",
    storageBucket: "vt-hacks-11-volunteer-together.appspot.com",
    messagingSenderId: "564768052604",
    appId: "1:564768052604:web:8b91a2ca8bd6789ecb00f9",
    measurementId: "G-HB9R2HGPS3"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
export { auth, db };
