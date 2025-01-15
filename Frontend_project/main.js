/*-------- SHOW NAVBAR --------*/
const showMenu = (headerToggle, navbarId) =>{
    const toggleBtn = document.getElementById(headerToggle),
    nav = document.getElementById(navbarId)
    
    // Validate that variables exist
    if(headerToggle && navbarId){
        toggleBtn.addEventListener('click', ()=>{
            // We add the show-menu class to the div tag with the nav__menu class
            nav.classList.toggle('show-menu')
            // change icon
            toggleBtn.classList.toggle('bx-x')
        })
    }
}
showMenu('header-toggle','navbar')

/*-------- LINK ACTIVE --------*/
const linkColor = document.querySelectorAll('.nav__link')

function colorLink(){
    linkColor.forEach(l => l.classList.remove('active'))
    this.classList.add('active')
}

linkColor.forEach(l => l.addEventListener('click', colorLink))
// --------




// JS CODE
// Function to adjust the page width based on screen width
function adjustPageWidth() {
    const screenWidth = window.innerWidth;

    // Get the body or wrapper element
    const pageWrapper = document.body;

    if (screenWidth >= 992 && screenWidth <= 1600) {
        // Shrink to 90% if the screen width is between 992px and 1600px
        pageWrapper.style.transform = "scale(0.9)";
        pageWrapper.style.transformOrigin = "top left"; // Keep the scaling from the top-left corner
    } else if (screenWidth >= 700 && screenWidth <= 767) {
        // Shrink to 80% if the screen width is between 700px and 767px
        pageWrapper.style.transform = "scale(0.8)";
        pageWrapper.style.transformOrigin = "top left";
    } else if (screenWidth >= 600 && screenWidth < 700) {
        // Shrink to 75% if the screen width is between 600px and 700px
        pageWrapper.style.transform = "scale(0.75)";
        pageWrapper.style.transformOrigin = "top left";
    } else if (screenWidth <= 600) {
        // Shrink to 50% if the screen width is 600px or smaller
        pageWrapper.style.transform = "scale(0.5)";
        pageWrapper.style.transformOrigin = "top left";
    } else {
        // No scaling for screens larger than 1600px
        pageWrapper.style.transform = "scale(1)";
    }
}

// Add an event listener to adjust the page size when the window is resized
window.addEventListener('resize', adjustPageWidth);

// Call the function initially to set the page width correctly on page load
adjustPageWidth();
