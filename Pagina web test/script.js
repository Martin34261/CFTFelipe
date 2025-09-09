const collapseElementList = document.querySelectorAll('.collapse')
const collapseList = [...collapseElementList].map(collapseEl => new bootstrap.Collapse(collapseEl))

titulo = document.querySelector("h1")
titulo.innerHTML = "Este contenido fue agregado con JavaScript"
