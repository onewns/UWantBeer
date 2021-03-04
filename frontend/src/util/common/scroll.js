const hasScrolledDown = function() {
    let lastY = window.scrollY

    return new Promise((resolve) => {
        const scrollInterval = setInterval(() => {
            let nowY = window.scrollY
            if (Math.abs(lastY - nowY) > 50) {
                if (lastY < nowY) {
                    resolve(true)
                }else{
                    resolve(false)
                }
                lastY = nowY
                clearInterval(scrollInterval)
            }
        }, 250)
    })
}

/**
 * @param {Number} targetY - 이동하고자 하는 scrollY값
 */
const smoothScrollTo =  function (targetY) {
    let n = 1
    if (window.scrollY > targetY) {n = -1}
  
    const scrollInterval = setInterval(() => {
        window.scrollBy(0, n)        
        if (Math.abs(n)<100) {
            n += 0.5 * n
          }
          if ((n < 0 && window.scrollY <= targetY) |
              (n > 0 && (
                  window.scrollY >= targetY | 
                  window.scrollY >= document.body.scrollHeight-window.innerHeight-1)) 
              ) {
                  window.scrollTo(0, targetY)
                  clearInterval(scrollInterval)
              }
      }, 15)
  }


export { hasScrolledDown, smoothScrollTo }