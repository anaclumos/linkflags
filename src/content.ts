const inject = () => {
  let styles: string = require('./index.css')
  const style = document.createElement('style')
  style.textContent = styles
  document.head.appendChild(style)
}
inject()
