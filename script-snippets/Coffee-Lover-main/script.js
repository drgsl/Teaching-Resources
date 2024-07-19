let leftElems = document.querySelectorAll(".fromLeft");
let rightElems = document.querySelectorAll(".fromRight");
let screens = document.getElementsByClassName("screen")
let topButton = document.getElementById("topButton");

window.onload = animateView;
window.onscroll = animateView;
window.onresize = animateView;

function animateView() {

  //Check for top button

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topButton.style.display = "block";
  } else {
    topButton.style.display = "none";
  }

    leftElems.forEach(leftElem => {
        let leftElemBound = leftElem.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        if (leftElemBound.top < windowHeight && leftElemBound.bottom > 0) {
            leftElem.classList.add("slideFromLeft");
        }else if(leftElem.classList.contains("slideFromLeft"))
        {
            leftElem.classList.remove("slideFromLeft")
        }
    });

    rightElems.forEach(rightElem => {
        let rightElemBound = rightElem.getBoundingClientRect();
        const windowHeight = window.innerHeight;

        if (rightElemBound.top < windowHeight && rightElemBound.bottom > 0) {
            rightElem.classList.add("slideFromRight");
        }else if(rightElem.classList.contains("slideFromRight"))
        {
            rightElem.classList.remove("slideFromRight")
        }
    });
}

function goToScreen (screenIdx) {
  
  //console.log(screens.length)
  screens[screenIdx].scrollIntoView({block: "center"});
}


function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}