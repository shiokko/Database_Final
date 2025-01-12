console.log('index.js success');

//Signup or Login
function toggleForm(event) {
    event.preventDefault();

    // 連接到那些boxes
    const formTitle = document.getElementById('form-title');
    const toggleBtn = document.getElementById('toggle-btn');
    const toggleLink = document.getElementById('toggle-link');
    const nameBox = document.getElementById('name-box');

    // 切換條件
    if (formTitle.innerText === 'Log In') {
        // 切換到 Sign Up
        formTitle.innerText = 'Sign Up';
        toggleBtn.innerText = 'Sign Up';
        toggleLink.innerHTML = 'Already have an account? <a href="#" onclick="toggleForm(event)">Log In</a>';
        nameBox.style.display = 'block'; // 顯示 Name 欄位
    } else {
        // 切換到 Log In
        formTitle.innerText = 'Log In';
        toggleBtn.innerText = 'Log In';
        toggleLink.innerHTML = "Don't have an account? <a href='#' onclick='toggleForm(event)'>Sign Up</a>";
        nameBox.style.display = 'none'; // 隱藏 Name 欄位
    }
}

