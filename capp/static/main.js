const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.nav__link');
const postbtn = document.getElementById("myForm");
const spinner = document.getElementById('spinner');




navToggle.addEventListener('click', () => {
    document.body.classList.toggle('nav-open');
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
    })
})

window.addEventListener("scroll", function(){
    const header = this.document.querySelector("header");
    header.classList.toggle("sticky" ,window.scrollY > 0);
});

postbtn.addEventListener('submit',function(){

    postbtn.classList.toggle('fade-out');
    spinner.classList.toggle('show');

    let elements = this.elements;
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].type == 'submit'){
            elements[i].disabled = true;
        }
    }
});




// // 3秒後にopacityを0にする
// setTimeout(() => {
//     loader.style.opacity = 0;
//    }, 3000);
  
//    // アニメーションが終わると、要素を取り除く
// loader.addEventListener("transitionend", () => {
//     loader.remove();
// });

