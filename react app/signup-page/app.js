import { initializeApp } from "firebase/app";
import { getAuth,GoogleAuthProvider, signInWithPopup } from "firebase/auth";


import {
    getDatabase,
    ref,
    set,
   
} from "firebase/database";


const firebaseConfig = {
    apiKey: "AIzaSyB2NsXCbCBttgEaFUUDPipFYA17tRbhGLE",
    authDomain: "pillbox-7ebe9.firebaseapp.com",
    projectId: "pillbox-7ebe9",
    storageBucket: "pillbox-7ebe9.appspot.com",
    messagingSenderId: "292374776797",
    appId: "1:292374776797:web:a6f57c5c3770312074c434",
    measurementId: "G-R7R45WB6BB"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth();
const provider = new GoogleAuthProvider();
const db = getDatabase(app);

const registerBtn = document.getElementById('register-button');
const loginBtn = document.getElementById('login-button');

registerBtn.addEventListener('click', function (event) {
    event.preventDefault();
    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const email = document.getElementById('email').value;
    const newPassword = document.getElementById('new-password');
    const confirmPassword = document.getElementById('confirm-password');




    
        signInWithPopup(auth, provider)
            .then((result) => {
                const credential = GoogleAuthProvider.credentialFromResult(result);
                const token = credential.accessToken;
                const user = result.user;

                const reference = ref(db, "users/" + user.uid);
                // window.alert("User registered successfully");
                set(reference, {
                    firstName: firstName,
                    lastName: lastName,
                    email: email,
                    newPassword: newPassword,
                    confirmPassword: confirmPassword,
                   
                  
                })
                    // .fire


            }).catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                console.log(errorCode + " " + errorMessage);
                window.alert("Error: " + errorMessage);
            });
    
});

// loginBtn.addEventListener('click', function (event) {
//     event.preventDefault();
//     signInWithPopup(auth, provider)
//         .then((result) => {
//             const credential = GoogleAuthProvider.credentialFromResult(result);
//             const token = credential.accessToken;
//             const user = result.user;
//             window.alert("Welcome Back!");
//             window.location.href = "./../index.html";
//         }).catch((error) => {
//             const errorCode = error.code;
//             const errorMessage = error.message;
//             console.log(errorCode + " " + errorMessage);
//             window.alert("Error: " + errorMessage);
//         });
// });



// //validate functions
