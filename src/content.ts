import styles from './styles.css'

const link = document.getElementsByTagName('a')[0]
if (link) {
  const color = window.getComputedStyle(link).color
  document.documentElement.style.setProperty('--linkflags-color', color)
}

const style = document.createElement('style')
style.textContent = styles
document.head.appendChild(style)
