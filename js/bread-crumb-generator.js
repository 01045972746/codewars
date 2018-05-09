const f_regex = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]

function generateBC(url, seperator) {
  url = url.replace('https://', '').replace('http://', '')
  var urlArr = url.split('/')
  var path = ''
  var resultArr = []
  if(urlArr.length == 1)
    resultArr.push('<span class="active">HOME</span>')
  else {
    urlArr.map((item, index) => {
      if(item == "")
        return
      if(!index) {
        path += '/'
        if(urlArr.length == 2) {
          if(urlArr[index+1] == "")
            resultArr.push('<span class="active">HOME</span>')
          else
            resultArr.push(`<a href="${path}">HOME</a>`)  
        }
        else
          resultArr.push(`<a href="${path}">HOME</a>`)
      } // First URL
      else if(index == urlArr.length -1) {
        let i1 = item.indexOf('.')
        let i2 = item.indexOf('?')
        let i3 = item.indexOf('#')
        let urlStr = ''
        if(i1 != -1)
          urlStr = item.substring(0, i1)
        else
          if(i2 != -1)
            urlStr = item.substring(0, i2)
          else
            urlStr = item
        
        if(i3 != -1)
          urlStr = urlStr.substring(0, i3)

        if(urlStr.length > 30) {
          resultArr.push(
            `<span class="active">${urlStr.split('-')
                .filter(p => !f_regex.includes(p))
                .map(p => {
                  return p.substring(0, 1).toUpperCase()
                }).join('')}</span>`
          )
        }
        else {
          if(urlStr == "index") {
            let previous = resultArr.pop()
            previous = previous.substring(previous.indexOf('>')+1)
            previous = previous.substring(0, previous.indexOf('<'))

            resultArr.push(`<span class="active">${previous}</span>`)
          }
          else
            resultArr.push(`<span class="active">${urlStr.replace(/-/gi, ' ').toUpperCase()}</span>`)
        }
          
      }
      else {
        path += `${item}/`
        if(item.length > 30) {
          resultArr.push(
            `<a href="${path}">${item.split('-')
              .filter(p => !f_regex.includes(p))
              .map(p => {
                return p.substring(0, 1).toUpperCase()
              }).join('')}</a>`
          )
        }
        else
          resultArr.push(`<a href="${path}">${item.replace(/-/gi, ' ').toUpperCase()}</a>`)
      }
        
    })
  }
  return resultArr.join(seperator)
}


// Clever
// function generateBC(url, separator) {
//   url = url.replace(/(^http.*\/\/|\/index\..*$|\/$)/g, '' );
//   let crumbs = url.split("/").map( c => rmvAnchorsAndParams(c) ), last = '<span class="active">'+labelize(crumbs.pop().replace(/\..*$/,''))+'</span>', path = "/";
//   return crumbs.length ? crumbs.map( (crumb,i) => i? (path=path+crumb+"/") && `<a href="${path}">${labelize(crumb)}</a>` : '<a href="/">HOME</a>' ).concat(last).join(separator) : '<span class="active">HOME</span>'
// }

// const IGNORABLE = /^(the|of|in|from|by|with|and|or|for|to|at|a)$/;
// let labelize = (str) => (str.length>30 ? str.split("-").map( s => IGNORABLE.test(s)? '' : s[0] ).join('') : str.replace(/\-/g, ' ') ).toUpperCase();
// let rmvAnchorsAndParams =  (str) => str.replace( /#.*/, '' ).replace( /\?.*/, '' );



// generateBC("mysite.com/pictures/holidays.html", " : ")
// generateBC("www.codewars.com/users/GiacomoSorbi", " / ")
// generateBC("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > ")
// generateBC("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ")
// generateBC("www.microsoft.com/important/confidential/docs/index.htm#top", " * ")
// generateBC('https://github.com/from-or-immunity-by-bladder-and-eurasian-research-meningitis/most-downloaded/from-the-immunity-meningitis-uber-paper-pippi-a-bladder/the-skin-paper-with-of-kamehameha-bioengineering-pippi?source=utm_pippi', ' . ')
// generateBC("http://www.agcpartners.co.uk/", " * ")
generateBC('twitter.de/users/files/files/profiles#people', ' >>> ')