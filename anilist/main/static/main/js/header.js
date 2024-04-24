const banners = [
	'banner_1.jpg',
	'banner_2.jpg',
	'banner_3.jpg',
]

const header = document.querySelector('header')

let index = 0

const changeBanner = () => {
	header.style.backgroundImage = `url(/static/main/imgs/${banners[index]})`
	banners.splice(banners.length, 0, banners[0])
  	banners.splice(0, 1)
}

setInterval(changeBanner, 12000)
onload = changeBanner