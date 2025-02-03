import { initializeApp } from "firebase/app";

const firebaseConfig = {
    apiKey: "AIzaSyCiIs4ER3t5lvDpLiyzAcYhhnrW-FknuFg",
    authDomain: "tiktok-clone-ff907.firebaseapp.com",
    projectId: "tiktok-clone-ff907",
    storageBucket: "tiktok-clone-ff907.firebasestorage.app",
    messagingSenderId: "635562663949",
    appId: "1:635562663949:web:5b9506d38d5f4540dcb544",
    measurementId: "G-6NBBCD61PY"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export default app;
