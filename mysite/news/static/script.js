let del = document.querySelector('#delete')
let article = document.querySelector('#article')
del.addEventListener('click', (e) => {
    e.preventDefault
    article.classList.add('is-hidden')
})