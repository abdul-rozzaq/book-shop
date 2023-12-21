

let nav = document.querySelector('#nav')
let navContainer = document.querySelector('#nav .container')
let space = document.querySelector('.space')

let searchForm = document.querySelector('form.search')
let searchFormButton = document.querySelector('form.search i')



searchFormButton.addEventListener('click', () => searchForm.submit());




window.addEventListener('scroll', (e) => {

    if (window.scrollY > 150) {
        space.style.height = nav.clientHeight + 'px'
        nav.classList.add('fixed')

    } else {
        space.style.height = 0
        nav.classList.remove('fixed')
    }
})


