import styles from './styles.css'

const setLinkflagsColor = () => {
  const links = document.getElementsByTagName('a')
  const link = links[Math.floor(links.length / 2)]
  if (link) {
    const color = window.getComputedStyle(link).color
    document.documentElement.style.setProperty('--linkflags-color', color)
  }
}

setTimeout(setLinkflagsColor, 1000)

const style = document.createElement('style')
style.textContent = styles
document.head.appendChild(style)
