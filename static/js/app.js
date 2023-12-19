

let nav = document.querySelector('#nav')


window.addEventListener('scroll', () => {
    window.scrollY > 150 ? nav.classList.add('show') : nav.classList.remove('show');
})





