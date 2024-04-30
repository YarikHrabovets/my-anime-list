const banners = [
	'banner_1.jpg',
	'banner_2.jpg',
	'banner_3.jpg',
	'banner_4.jpg',
]

const header = document.querySelector('header')
const nav = document.querySelector('.header-container') 

document.querySelector('#open-menu').onclick = () => {
	document.querySelector('.small-nav').classList.remove('small-nav-hidden')
	document.querySelector('.small-nav').style.display = 'block' 
	document.querySelector('.bg').style.display = 'block'  
}

document.querySelector('#close-menu').onclick = () => {
	document.querySelector('.small-nav').classList.add('small-nav-hidden')
	document.querySelector('.bg').style.display = 'none'  
}

addEventListener('scroll', (e) => {
	const boundingNav = nav.getBoundingClientRect()
	const boundingHeader = header.getBoundingClientRect()

	if (boundingNav.top <= -boundingNav.height) {
		nav.classList.add('fixed-header')
	} else if (boundingHeader.bottom >= 0) {
		nav.classList.remove('fixed-header')
	}
})

const changeBanner = () => {
	header.style.backgroundImage = `url(/static/main/imgs/${banners[0]})`
	banners.splice(banners.length, 0, banners[0])
  	banners.splice(0, 1)
}

setInterval(changeBanner, 12000)
onload = changeBanner