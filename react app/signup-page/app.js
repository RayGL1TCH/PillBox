import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-auth.js";
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-database.js";

// Your Firebase configuration

    const firebaseConfig = {
        apiKey: "AIzaSyChxFBB_GZxpTvee8YCDPKuoR2qKuy7f1w",
        authDomain: "pillbox2-bd85a.firebaseapp.com",
        projectId: "pillbox2-bd85a",
        storageBucket: "pillbox2-bd85a.appspot.com",
        messagingSenderId: "909255190762",
        appId: "1:909255190762:web:4684785cade65ae6674f93"
    
  };
// Initialize Firebase
const app = initializeApp(firebaseConfig);

const auth = getAuth(app);
const database = getDatabase(app);

const registerBtn = document.getElementById('register-button');

registerBtn.addEventListener('click', function (event) {
    event.preventDefault();
    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const email = document.getElementById('email').value;
    const newPassword = document.getElementById('new-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    createUserWithEmailAndPassword(auth, email, newPassword)
        .then((userCredential) => {
            const user = userCredential.user;
            const reference = ref(database, "users/" + user.uid);
            set(reference, {
                firstName: firstName,
                lastName: lastName,
                email: email,
                newPassword: newPassword,
                confirmPassword: confirmPassword,
            })
            console.log(user);
            alert("Your account has been created!");
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.log(errorCode, errorMessage);
        });
});
